nested_dict = [
        {'name': 'Alice',
        'age': 30,
        'address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'state': 'CA'
        }
        },
        {
        'name': 'Bob',
        'age': 30,
        'address': {
            'street': '456 Elm St',
            'city': 'Sometown',
            'state': 'NY'
        }
        }
]

ages = {}
for i in nested_dict:
    age = i['age']
    name = i['name']
    
    if age in ages:
        ages[age].append(name)
    else:
        ages[age] = [name]
print(ages)


