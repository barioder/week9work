# stars right side

for i in range(10):
    print('')
    for j in range(i+1):
        print('*', end='')

print('\n')

# stars on left side

for i in range(6):
    for j in range(6-i-1):
        print('', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print()

for i in range(6):
    print(''*(6-i-1) + '*'*(i+1))

# pyramid stars

for i in range(6):
    for j in range(6-i-1):
        print(' ', end='')
    for j in range(2*i+1):
        print('*', end='')
    print()
