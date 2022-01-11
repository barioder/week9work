# for loops
for i in range(5):
    print("hello")

for i in range(5):
    print(i)

tup1 = ('Red', 'Blue', 'Yellow', 'Green')

for i in tup1:
    print(i)

list1 = [1, 2, 3, 4]

for i in list1:
    print(i)
dict1 = {'name': 'Derrick',
         'game': 'Soccer'}
# prints only keys
for i in dict1:
    print(i)

# prints only values
print("-------only values----")
for i in dict1.values():
    print(i)

print("-------keys and values----")
# prints keys and values
for i, j in dict1.items():
    print(i, j)


for i in range(1,15,1):
    print("*")
    for j in range(1, i+1):
        print("*", end='')

row = 12
#
# for i in range(12):
#     print(''*(rows-i-1), end='')
