d = {}
print(type(d))

product1 = {'title': "Sony", 'price': 100}
print(product1)
product2 = dict(title="iPhone", price=200)
print(product2)

users = [
    ['bob@gmail.com', 'Bob'],
    ['tom@gmail.com', 'Tom'],
    ['kat@gmail.com', 'Kat'],
]
print(users)
d_users = dict(users)
print(d_users)

users_t1 = (
    ['bob@gmail.com', 'Bob'],
    ['tom@gmail.com', 'Tom'],
    ['kat@gmail.com', 'Kat'],
)
users_t2 = (
    ('bob@gmail.com', 'Bob'),
    ('tom@gmail.com', 'Tom'),
    ('kat@gmail.com', 'Kat'),
)
d_users_t1 = dict(users_t1)
d_users_t2 = dict(users_t2)
print(d_users_t1)
print(d_users_t2)

product3 = dict.fromkeys(['price1', 'price2', 'price3'], 50)
print(product3)

nums = {i: i + 1 for i in range(1, 10)}
print(nums)

product11 = {'title': "Sony", 'price': 100}
product21 = dict(title="iPhone", price=200)
print(product11['title'])
print(product11.get('title'))
print(product11.get('title1'))
print(nums[1])

for key in product21:
    print(key)
    print(product21[key])

key_value = product21.items()
print(key_value)
for key, value in product21.items():
    print(key, value)

products = [
    {'title': "Sony", 'price': 100},
    {'title': "iPhone", 'price': 1000},
    {'title': "Nokia", 'price': 10}
]
print(products)
for product in products:
    print(product['title'], product['price'])
