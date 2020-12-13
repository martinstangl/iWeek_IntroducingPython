import socket
from _thread import *

from pong_network.settings import Settings
from pong_network.ball import Ball
from pong_network.data_object import DataObject


import pickle



server = Settings.config["server_ip"]
port = Settings.config["port"]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


players = Settings.config["players"]
print(players)
do = DataObject()


game_start = False


def threaded_client(conn, player):
    #global do
    do.player = players[player]

    conn.send(pickle.dumps(do))
    reply = ""
    while True:
        #print(game_start)
        if game_start:
            do.ball.check_collision(players[0], players[1])
            do.ball.move()
            try:
                data = pickle.loads(conn.recv(2048))

                if data is None:
                    print("Disconnected")
                    break
                else:
                    players[player] = data.player
                    if player == 0:
                        do.player = players[1]
                        reply = do
                    elif player == 1:
                        do.player = players[0]
                        reply = do

                    #print("Received: ", data)
                    #print("Sending : ", reply.ball.visual.x)

                    conn.sendall(pickle.dumps(reply))
            except:
                break

    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    client_list = []
    conn, addr = s.accept()
    print("Connected to:", addr)
    do.ball = Ball(Settings.config["ball_size"], Settings.config["screen_width"], Settings.config["screen_height"])
    start_new_thread(threaded_client, (conn, currentPlayer))
    #client_list.append(conn)
    currentPlayer += 1
    if currentPlayer == 2:
        print("Start")
        game_start = True

