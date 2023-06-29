
people_list = [
    {'name': 'tony',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'chris',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'ariana', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    {'name': 'kelly', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]

def filter_males(people_list):

    male_list = [p for p in people_list if p['sex'] == 'male']
    return male_list

male_list = filter_males(people_list)

print(male_list)



# newList = [{"id": c["id"],"make": c["make"],"on_sale":"yes"} for c in carList if c["price"] > 33000]