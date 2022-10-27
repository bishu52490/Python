a = int(input('Enter a number: '))
i = 2
n=0

while i < a:
    if a % i == 0:
        print (a, 'is divisible by', i)
        n += 1
        i += 1
    else:
        i += 1
if n != 0:
    print(a, 'is not a Prime Number.')
else: print(a, 'is a Prime Number.')
