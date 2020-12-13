class Person:
    def __init__(self, vorname, name, alter, gewicht):
        self.vorname = vorname
        self.name = name
        self.alter = alter
        self.gewicht = gewicht

    def get_name(self):
        return self.vorname + " " + self.name

    def print_name(self):
        print(self.get_name())

