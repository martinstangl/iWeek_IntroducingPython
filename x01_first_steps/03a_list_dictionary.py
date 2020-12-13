'''
Häufig braucht man in Programmen eine Menge von gleichen Objekten. Beim Speichern und
Verarbeiten solcher Objekte helfen in Python die Listen. Um deren Bedarf klar zu machen,
beginnen wir mit einem Beispiel, das ohne Liste arbeitet.
https://www.w3schools.com/python/python_lists.asp
'''

benutzer_1 = "Naveena"
benutzer_2 = "Cédric"
benutzer_3 = "Moritz"
benutzer_4 = "Fabian"

'''
Probleme: 
    - für jeden (zusätzlichen) Benutzer wird eine neue Variable benötigt
    - Funktionen müssen für jede Variable einzeln aufgerufen werden
    - ...
 '''
users = ["Naveena", "Cédric", "Moritz", "Fabian"]
print (users[0])    # erstes Element ausgeben
print(users)    # alle Elemente ausgeben
users.append("Seya Neal")   # ein neues Element hinten anfügen
users.sort()  # liste.sort(reverse=True)
print(users)
print("Anzahl Elemente: ", len(users))  # Achtung bei + --> print("Anzahl Elemente: " + len(liste))

'''
Uebung:
# Weshalb ist hier ein Fehler zu erwarten? Korrigieren Sie den Code.
animals = ["shark", "whale"]
print(animals[2])
'''


'''
Die Dictionary ist eine weitere Datenstruktur, die eine Erweiterung der Liste 
darstellt. Man speichert nicht Objekte, sondern Zuordnungen. Man speichert also
die Werte nicht per Index an einer Stelle, sondern ueber die Zuordnung zu einem 
beliebigen Schluessel. {key1:value1, key2:value2,...}
https://www.w3schools.com/python/python_dictionaries.asp
'''
dictionary = {"name": "Duck",
              "vorname": "Donald",
              "alter": 55,
              "ahv_nr": "170.334.776.123",
              "ledig": True,
              "neffen": ["Tick", "Trick", "Track"]
              }

# dictionary["vermoegen"] = 1000000000  # Key/Value Paar hinzufügen
print("############ Dictionary #############")
print(dictionary)
print(dictionary["vorname"])
print(dictionary["neffen"][0])

print("Ein Dictionary über die Keys iterieren:")
for key in dictionary:
    print(dictionary[key])
    # print(key, " : ", dictionary[key])

