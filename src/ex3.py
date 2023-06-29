people_list = [
    {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
    {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
]

def calc_bmi(people_list):
    bmi = list(map(lambda p: p['weight_kg'] / (p['height_meters'] ** 2), people_list))
    return bmi

new_list = calc_bmi(people_list)
print(new_list)


    # for p in p in people_list lambda p: p['weight_kg'] / (p['height_meters'] ** 2)
