n = 5
x = 0
while n != 0:

    print(' '*n, end='')
    print('*'*(x + (1 + (5-n))), end='')
    print()
    n -= 1
    x += 1

print('--------------------------------')

# create a start pattern that prints a latter using a while loop
x = 0

while x != 4:
    x += 1
    if x == 1:
        print('E'*5, end='')
        print()
    print('E')
    if x == 2:
        print('E' * 5, end='')
        print()
    if x == 4:
        print('E' * 5, end='')
        print()


print('---------------------------------')

students = {'001': 'Derrick',
            '002': 'Stevo',
            '003': 'Cedric'}
print(students)

students.pop('001')
print(students)


students.update({'004' : 'Tina'})
print(students)



# students['002'] = "Tim"
#
# print(students)