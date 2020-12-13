# user_pass = "1234"
# admin_pass = "secret"
# password = input("Bitte Passwort eingeben: ")
#
# if password == user_pass:
#     print("Als User eingeloggt")
# elif password == admin_pass:
#     print("Als Admin eingeloggt")
# else:
#     print("Nicht authorisiert!")


# age = 20
# country = "US"
# if (country == "US" and age >= 21) or (country != "US" and age >= 18):
#     print ("Diese Person darf Alkohol trinken")
# else:
#     print("Diese Person darf KEIN Alkohol trinken")


'''
Kontrollfrage:
Welche der folgenden drei Selektionen funktioniert fehlerfrei?
(Es geht um den Syntax, nicht um die Semantik)

if num1 < num2:
print ("Erste Ausgabe")

if num1 * num2 >= 100:
    print ("Zweite Ausgabe")

if ( num1 != num2 ) {
    print ("Dritte Ausgabe")
}
'''


########## Aufgabe(n) Verzweigungen ############
'''
Aufgabe 1:
Lassen Sie den Benutzer eine Zahl eingeben:
--> zahl = input("Zahl: ")
Wir gehen für den Moment davon aus, dass der Benutzer eine ganze Zahl eingibt, die Sie mit
der int()-Funktion in eine Zahl umwandeln können.
Erstellen Sie eine if-Anweisung, die eine entsprechende Meldung ausgibt, wenn...
(a). ... die Zahl grösser als 10 ist
(b). ... die Zahl gerade ist
(c). ... das Quadrat der Zahl groesser als 1000 ist
'''

'''
Aufgabe2:
Lassen Sie den Benutzer eine Schweizer Stadt eingeben:
z.B. stadt = "Aarau"     # Benutzer gibt eine Stadt ein
Erstellen Sie eine if-Anweisung die prüft, ob es sich um eine Stadt mit 
mehr als 1000000 Einwohner handelt. Legen Sie dazu zunächst eine Liste an, 
und prüfen Sie anschliessend, ob sich die eingegebene Stadt in der Liste vorhanden ist:

s100k = ["Zürich","Genf","Basel","Lausanne","Bern","Winterthur"]

Hinweis: Mit dem Schlüsselwort "in" kann überprüft werden, ob ein Wert 
in einer Liste enthalten ist.
'''

# counter = 1
# while counter <= 10:
#     print(counter)
#     counter += 1    # counter = counter + 1
#
# for counter in range(1, 10):
#     print(counter)


# sus = ["jennifer", "marc", "thilo", "melvin"]
# for i in sus:
#     print(i)


# for i in range(4):  # range(4)--> [0, 1, 2, 3]
#     print(sus[i])
#     sus[i] = sus[i].capitalize()
#
# print(sus)

# name = "Seraina"
# for i in name:
#     print(i)

############ Aufgabe(n) Schleifen ################
'''
Aufgabe1:
Wir addieren mal die ersten 1000 natürlichen Zahlen:
(a) Ergänzen Sie den Code. Die Summe soll schliesslich ausgegeben werden.
(b) Erweitern Sie den Code. Wir wollen alle durch 10 teilbaren Zahlen ignorieren. 
    Wir gross ist dann die Summe noch? 
    Tipp: z % 10 == 0 überprüft, ob die Zahl durch 10 teilbar ist.
'''
summe = 0
for i in range(1, 1000):
    # addieren
    pass
# Resultat ausgeben

'''
Aufgabe2:
Die Fionacci-Folge beginnt mit 1,1,2,3,5,8,... Die nächste Zahl ist jeweils die Summe
seiner zwei direkten Vorgänger. Finden Sie mit einer Scheife die erste Fibonacci-Zahl,
die grösser als eine Million ist.
'''

fib_v1 = 1                  # erster Vorgänger
fib_v2 = 1                  # zweiter Vorgänger
fib_n = 0                   # Variable für die aktuelle Fibonacci-Zahl
# ToDo complete code
# solange fib_n noch kleiner gleich 10^6
# berechne nächste fib_n
# setze fib_v1 und fib_v2 korrekt
print(fib_n)

