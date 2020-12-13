'''
Aufgabe 1
Schreiben Sie ein kleines Skript, welches ein Geburtsdatum einliest
und den Wochentag des kommenden Geburtstags ausgibt
siehe:
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
'''

from datetime import datetime

print("------------ Bitte geben Sie ihr Geburtsdatum ein ------------")
jahr = input("Jahr eingeben: ")
monat = input("Monat eingeben: ")
tag = input("Tag eingeben: ")

actual_year = datetime.now().year
next_year = actual_year + 1
birthday = datetime(next_year, int(monat), int(tag))

print("Ihr nächster Geburtstag ist an einem", birthday.strftime("%A"))
