# inside a function write a python program that goes through 3 conditional statements
# until it gets its final output

def speed(x):
    if x < 40:
        print(str(x) + " slow and good speed")
    elif x < 80:
        print(str(x) + " not so fast and not a bad speed")

    else:
        print(str(x) + " is not good speed, slow down")

speed(120)

print('----------------------------------------------')

# create a if statement using the (or) (and) operator
x = 10
y = 5
if x < y or y!=x and y > 0:
    print("This is True")

print('----------------------------------------------')
# using the user input create a pyramid using number 1
n = int(input("Rows needed "))
for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')

    for j in range(2*i+1):
        print("1", end='')

    print()

print('----------------------------------------------')

# create a dictionary and add another item to the dictionary

students = {'001': 'Derrick',
            '002': 'Stevo',
            '003': 'Cedric'}
print(students)

students['004'] = 'Annet'

print(students)

print('----------------------------------------------')

# create a dictionary inside a dictionary inside a and use the nesting loop to print your out put

details = {'Derrick': {'class': "s1", 'color': 'red', 'sport': 'soccer'},
            'Stevo': {'class': "s2", 'color': 'green', 'sport': 'Chess'},
            'Cedric': {'class': "s4", 'color': 'yellow', 'sport': 'baseball'}}

for name, detail in details.items():
    print(name)
    for k,v in detail.items():
        print(k,v)
    print()