

def ex1():
    class Person:
        def __init__(self, name, age, weight):
            self.name = name
            self.age = age
            self.weight = weight

    people = [
        Person('John', 25, 70),
        Person('Alice', 30, 65),
        Person('Bob', 20, 75)
    ]

    sorted_people = sort_people(people, 'age', 'asc')
    for person in sorted_people:
        print(person.name, person.age, person.weight)
ex1()


