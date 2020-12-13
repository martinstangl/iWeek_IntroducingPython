from x01_first_steps.classes.person import Person

p1 = Person("John", "Doe", 30, 75)
p2 = Person("Jane", "Doe", 32, 55)
p1.print_name()
p2.print_name()

person_list = []
for i in range(10):
    person_list.append(Person("Jane_"+str(i), "Doe"+str(i), 32+i, 50+i))

print(person_list)

for p in person_list:
    p.print_name()

# berechne das Durchschnittsalter der Personen in person_list



