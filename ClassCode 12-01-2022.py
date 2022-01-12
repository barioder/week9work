# Create a upside down pyramid pattern using stars
n = 5
for i in range(n, 0, -1):
    for j in range(n-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*', end='')
    print()

print('-------------Creating N--------------')
# create a letter pattern using starts

n = ''
for row in range(0,9):
    for col in range(0,7):
        if col == 1 or col == 5 or (row == col and col != 0 and col != 6):
            n = n+"*"
        else:
            n = n + " "

    n = n + "\n"
print(n)
print("------------------------------------------")
# create a right side triangle using the user input

n = int(input("Enter number of rows "))

for i in range(n):
    for j in range(i+1):
        print('*', end='')

    print()

# using list comprehension print out even numbers

evenNum = [x for x in range(1, 10, 1) if x % 2 == 0]
print(evenNum)

# unsing the lamba function print out 2022

x = lambda a: a+22
print(x(2000))


