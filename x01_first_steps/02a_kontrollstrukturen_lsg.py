'''
Kontrollfrage:
Welche der folgenden drei Selektionen funktioniert fehlerfrei?
(Es geht um den Syntax, nicht um die Semantik)

if num1 < num2:
print ("Erste Ausgabe")         # nicht um 4 LZ eingerückt

if num1 * num2 >= 100:
    print ("Zweite Ausgabe")

if ( num1 != num2 ) {           # Java-Syntax
    print ("Dritte Ausgabe")
}
'''

########## Aufgabe(n) Verzweigungen ############
'''
Aufgabe1:
Lassen Sie den Benutzer eine Zahl eingeben:
--> zahl = input("Zahl: ")
Wir gehen für den Moment davon aus, dass der Benutzer eine ganze Zahl eingibt, die Sie mit
der int()-Funktion in eine Zahl umwandeln können.
Erstellen Sie eine if-Anweisung, die eine entsprechende Meldung ausgibt, wenn...
(a). ... die Zahl grösser als 10 ist
(b). ... die Zahl gerade (Hinweis: Modulo 2) 
(c). ... das Quadrat der Zahl groesser als 1000 ist
'''

zahl = input("Bitte Zahl eingeben: ")
zahl = int(zahl)
if zahl >= 10:
    print("Zahl ist >= 10")
if zahl % 2 == 0:
    print("Zahl ist gerade");
if zahl *zahl > 1000:
    print("Das Quadrat ist groesser als 1000")


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

s100k = ["Zürich", "Genf", "Basel", "Lausanne", "Bern", "Winterthur"]
stadt = input("Bitte Stadt eingeben: ")
if stadt in s100k:
    print("Stadt hat mehr als 100k Einwohner")
else:
    print("Stadt hat weniger als 100k Einwohner")


########## Aufgabe(n) Schleifen ############
'''
Aufgabe1:
Wir addieren mal die ersten 1000 natürlichen Zahlen:
(a) Ergänzen Sie den Code. Die Summe soll schliesslich ausgegeben werden.
(b) Erweitern Sie den Code. Wir wollen alle durch 10 teilbaren Zahlen ignorieren. 
    Wir gross ist dann die Summe noch? 
    Tipp: z % 10 == 0 überprüft, ob die Zahl durch 10 teilbar ist.
'''
summe = 0
a = 1
b = 1000
for i in range(a, b):
    if i % 10 != 0:
        summe += i
print("Die Summe von: {} bis {} ist {}".format(a, b, summe))    # Resultat ausgeben

'''
Aufgabe2:
Die Fionacci-Folge beginnt mit 1,1,2,3,5,8,... Die nächste Zahl ist jeweils die Summe
seiner zwei direkten Vorgänger. Finden Sie mit einer Scheife die erste Fibonacci-Zahl,
die grösser als eine Million ist.
'''

fib_v1 = 1
fib_v2 = 1
fib_n = 0
fib_liste = []
while fib_n <= 1000000:
    fib_n = fib_v1 + fib_v2
    fib_v2 = fib_v1
    fib_v1 = fib_n
    fib_liste.append(fib_n)
print(fib_liste)

