print(3 != 4)
print(4 == 4)

a = 6
b = 8
# and operator both conditions need to be true
print(a == 6 and b == 8)

print(a >= 5 and b <= 6)

print(a != b and b == 8)

# or operator only one condition needs to be true
print("or operator")
print(a != 7 or b == 10)
print(a < b or 9 < 5)
print(a > b or b == 9)

a = 6
b = 7

if a!=b:
    print('True')

elif a < b:
    print('could be true')
else:
    print('false')
print('-----------------------')
def myfunc(c):
    if c == 20:
        return True
    else:
        return False

print(myfunc(21))

# using boolean on lists

list1 = ["Man", 'Boy', 'Girl']

print('Boy' in list1)
# python being case sensitive
print('boy' in list1)
print('cow' in list1)
# using ! operator

print('cow' != list1)
print('-------------------------')
sportsbio = {
    'Name': 'Derrick',
    'Age' : 23,
    'sport': 'Soccer'
}

print('Derrick' in sportsbio.values())

if 'Derrick' not in sportsbio.values():
    print('I guess he is not')
elif 'Derrick' in sportsbio:
    print('oh, so he is in')
else:
    print('end of statement')