

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



def sort_people(people_list, field, direction):
    people_list.sort(key=lambda p: p[field], reverse= (direction == 'desc'))


def filter_male(people_list):
    new_list = list(filter(lambda p: p['sex'] == 'male', people_list))
    return new_list


def calc_bmi(people_list2): 
    bmi_list = list(map(lambda person: {**person, 'bmi': round(person['weight_kg'] / person['height_meters'] ** 2, 1)}, people_list2)) 
    return bmi_list

