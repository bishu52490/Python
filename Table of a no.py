a = int(input('Please Enter a Number: '))
b = int(input('Enter the No of Multiples you want: '))
i = 1
while i <= b:
    multiple = a * i
    print(a, 'x', i, '=', multiple)
    i += 1
