people = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "city": "New York"
    },
    {
        "first_name": "Alice",
        "last_name": "Smith",
        "age": 25,
        "city": "San Francisco"
    },
    {
        "first_name": "Bob",
        "last_name": "Johnson",
        "age": 30,
        "city": "Los Angeles"
    },
    {
        "first_name": "Eva",
        "last_name": "Brown",
        "age": 28,
        "city": "Chicago"
    }
]

se = {}

for i in people:
    if i['age'] not in se.keys():
        se[i["age"]] = [i['first_name']]
    elif i["age"] in se.keys():
        se[i["age"]].append(i['first_name'])

print(se)

