''' This program will print The factorial of n natural number.
    For Example, you input 12
    then it would add 1 x 2 x 3 x ... up to 12 = 479001600
'''
n = int(input('Enter a Number: '))
i = 1
factorial = 1
while i <= n:
    if n < 20:
        print(i, end=' ')           # Optional Line For print 1 + 2 + 3 + 4 + .....
        if i != n:                  # Optional lines
            print('x', end=' ')    # Optional Lines
    factorial = factorial * i
    i += 1

print('=', factorial)
