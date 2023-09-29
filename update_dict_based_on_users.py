nested_dict = [{'name': 'Bob',
        'age': 30,
        'address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'state': 'CA'
        }
        },
        {'name': 'Alice',
        'age': 30,
        'address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'state': 'CA'
        }
        }
        ]
n1 = [{'User': 'Alice',
        'gender': 'M',
        'current_address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'state': 'CA'
        }
        },
        {'User': 'Bob',
        'gender': 'M',
        'current_address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'state': 'CA'
        }
        }]


a = []
for i in nested_dict:
    for j in n1:
        if i['name'] == j['User']:
            i.update(j)
            i.pop('User')
            a.append(i)

print(a)