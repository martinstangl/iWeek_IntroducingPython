######### Funktionen ##########
'''
Bisher haben wir unseren Code einfach von oben nach unten geschrieben. Manchmal einige
Anweisungen in einer Schleife gebündelt, aber immer an einem Stück.
Das Konzept der Funktionen ist für aber aus aus mehreren Gründen unabdingbar:

    Der Code wird sonst sehr schnell unübersichtlich (Spaghetticode). Ein Portionieren von
    Code in kleine logische Blocke verhindert das.

    Funktionen verhindern Redundanz im Code. Wird ein  Block mit Anweisungen mehrmals
    in einem Programm verwendet, ist es sinnvoll, diesen nur einmal zu programmieren um
    dann an verschiedenen Stellen im Programm auf diesen Block zu verweisen.

    Wir können Codeblöcke von fremden Entwicklern in unserem Code aufrufen (Stichwort: API).
'''

print("hello world")    # beim print(...) - Befehl handelt es sich bereits um eine
                        # interne Funktion


def ausgabe():
    print("Hallo Welt")
    print("Hallo Welt")


ausgabe()


'''
Funkktion mit Übergabeparameter und ohne Rückgabewert
Mittels dem Schlüsselwort "global" kann eine Variable aus
dem übergerodneten Scope verwendet werden
'''
def mult(zahl1, zahl2):
    result = 0
    while zahl1 >= 1:
        result += zahl2
        zahl1 -= 1
    print(result)


mult(3, 4)

'''
Funktion mit Übergabeparameter und Rückgabewert
'''
def is_prime(n):
    factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factors = factors + 1
    if factors == 2:
        return True
    else:
        return False


n = 23
print("Ist {} eine Primzahl? {}".format(n, is_prime(n)))

'''
Welche Syntax definiert eine korrekte Funktion in Python?:

function(a):
    print(a)

def(a):
    print(a)

def console(a):
    print(a)

'''

'''
Aufgabe 1a:
Schreiben Sie eine Funktion, die den Gesamtpreis der Produkte im Warenkorb berechnet.
Vervollständigen Sie dazu die Funktion "list_sum", welcher als Parameter eine Liste mit den
Preisen übergeben wird. Die Funktion soll dann die Summe der Zahlen aus der Liste
ausgeben.
'''


def list_sum(l):
    summe = 0
    # hier kommt der Code hin
    return summe
    pass


cart_prices = [20, 3.5, 6.49, 8.99, 9.99, 14.98]
print("Der Warenkorb beläuft sich auf: ", list_sum( cart_prices))


'''
Aufgabe 1b:
Schreiben Sie eine Funktion, der Sie einen Artikelnamen und den Verkaufspreis
übergeben können. Daraus soll die Funktion eine Liste erstellen, in der die
Preise von einem, zwei, drei,... bis zehn Einheiten des Artikels stehen. 
Genauer soll jedes Element in der Liste so aussehen: "Anzahl x Artikel: Preis".
'''


def prices_list(name, price):
    result = []
    # hier kommt der Code hin
    return result


print(prices_list("Wunderkeks", 0.79))  # Folgende Ausgabe wird erwartet:
                                        # ['1 x Wunderkeks: 0.79', '2 x Wunderkeks: 1.58', ...]

'''
Aufgabe 2:
Recherchieren Sie, welche Eigenschaften ein Schaltjahr haben muss. Erstellen Sie dann
die Funktion is_schaltjahr. Testen Sie etwa so (siehe unten):
'''


def is_schaltjahr(jahr):
    # hier kommt der Code hin
    pass


# Testcode der Funktion is_schaltjahr()
for j in range(1950, 2050):
    if is_schaltjahr(j):
        print ("Das Jahr "+str(j)+" ist ein Schaltjahr")


'''
Zusatzaufgabe:
Auf allen Banknoten ist eine eindeutige Seriennummer aufgedruckt. Bei Euro-Scheinen haben
diese Nummern das folgende Format: "N15000723228". Dabei ist das erste Zeichen ein Ländercode 
(N steht z.B. für Österreich). Es folgen 10 Nutzziffern und zuletzt die Prüfziffer 
(im Beispiel 8). Diese Prüfziffer wird wie folgt berechnet:

(a). Schreiben Sie anstelle des Läandercodes die Position des Buchstabens im Alphabet 
     (startend mit 1 für A). Hier 14 für N. Die neue Seriennummer liest sich so 1415000723228.

(b). Bilden Sie die Quersumme aller Stellen ausser der Prüfziffer. Hier also 1 + 4 + ... = 27.

(c). Bilden Sie den Neunerrest von der Quersumme: 27 : 9 = 3 Rest 0. Dazu verwenden Sie am besten
     den %-Operator: 27 % 9 = 0.
     
(d). Zählen Sie den Rest von 8 ab. Ist das Resultat Null, so ist die Prüfziffer gleich 9.
     In allen anderen Fällen entspricht diese Differenz (8 - Rest) der Prüfziffer.
     Hier also: 8 - 0 = 8.

Schreiben Sie ein Programm, das eine Euro-Seriennummer entgegen nimmt und prüft, ob die
Seriennummer korrekt ist. Googeln Sie ein paar Seriennummern und prüfen Sie Ihr Programm
damit.
'''


def check_euro_serial(serial):
    # hier kommt der Code
    pass


# Testcode der Funktion check_euro_serial()
serial_to_check = "N15000723228"
print("Check {}: {}".format(serial_to_check,check_euro_serial(serial_to_check)))

