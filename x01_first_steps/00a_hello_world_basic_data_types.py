from datetime import datetime

print("Hello world!")   # ein Kommentar

a = 5                   # eine variable
print(a)
print(type(a))          # Typ wird zur Laufzeit ermittelt

a = "5"
print(a)
print(type(a))          # Typ wird zur Laufzeit ermittelt

a = True
print(a)
print(type(a))          # Typ wird zur laufzeit ermittelt

a = "5"
b = "1"
print(a+b)

# Datum
birthday = datetime(2021, 3, 8)
print(birthday.strftime("%a, %x"))   # https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
diff = datetime.now() - birthday
print(diff)
print("##### Geburtstag eingeben #####")
# jahr = input("Bitte Jahr eingeben: ")
# monat = input("Bitte Monat eingeben:")
# tag = input("Bitte Tag eingeben:")
#
# print("Eingaben über die Konsole sind immer vom Typ String! D.h. wir müssen die Eingaben"
#       " 'casten', um mit ihnen zu rechnen")
#
# jahr = int(jahr)
# monat = int(monat)
# tag = int(tag)
#
# birthday = datetime(jahr, monat, tag)
# diff = datetime.now() - birthday
# print("Sie sind heute ",diff," Tage alt")


'''
Aufgabe 1
Schreiben Sie ein kleines Skript, welches ein Geburtsdatum einliest
und den Wochentag des kommenden Geburtstags ausgibt
'''

# 1. Eingabe Geburtstag (Tag, Monat, Jahr) über die Console und Eingabedaten in Variablen speichern


# 2. aktuelles Jahr über datetime.now() abrufen und in einer Variable speichern,
#    --> https://docs.python.org/3/library/datetime.html#datetime.datetime.year


# 3. Jahr um 1 erhöhen (==> nächstes Jahr)


# 4. Ein datetime-Objekt mit dem kommenden Geburtstag erstellen
#    --> blub = datetime(jahr, monat, tag)


# 5. Wochentage ausgeben, Formatierung siehe:
#    --> https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior



