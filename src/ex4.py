people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    {'name': 'gigi',    'age': 22, 'weight': 110, 'sex': 'female', 'id': 4},
]

def get_people(people_list):
    list = [p for p in people_list if p['age'] >= 15]
    return list

new_list = get_people(people_list)
print(new_list)
