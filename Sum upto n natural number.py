''' This program will print The sum up to n natural number.
    For Example, you input 12
    then it would add 1 + 2 + 3 + ... up to 12 = 78
'''
n = int(input('Enter a Number: '))
i = 1
sum = 0
while i <= n:
    print(i, end=' ')           # Optional Line For print 1 + 2 + 3 + 4 + .....
    if i != n:                  # Optional lines
        print('+', end=' ')     # Optional Lines
    sum = sum + i
    i += 1

print('=', sum)
