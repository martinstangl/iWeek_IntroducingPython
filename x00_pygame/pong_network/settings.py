from pong_network.player import Player


class Settings:
    config = {
        "players": [
            Player(color=(255, 255, 0), pos={'x': 10, 'y': 200}, screen_width=600,screen_height=400),
            Player(color=(0, 255, 0), pos={'x': 580, 'y': 200}, screen_width=600,screen_height=400)
        ],
        "screen_width": 600,
        "screen_height": 400,
        "background_color": (128, 128, 128),
        "ball_size": 15,
        "server_ip": "10.12.32.116",
        "port": 5522
    }
