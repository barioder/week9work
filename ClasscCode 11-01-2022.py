# print a for lop that prints 8 rows of stars going right
for i in range(1, 8, 1):
    print("*")
    for j in range(1, i+1):
        print("*", end='')

# create a for loop that prints up to  20 but skips 15
print('\n')
list1 = []
for i in range(1, 21, 1):
    if i != 15:
        list1.append(i)

print(list1)

# Create a dictionary and using the for loop print only values

dict1 = {'name': 'Derrick',
         'game': 'Soccer'}

for i in dict1.values():
    print(i)
