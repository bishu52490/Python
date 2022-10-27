
#                Approach 1
'''if x>y:
    if x > z:
        print(x, 'is the largest number.')
    
    if z > x:
        print(z, 'is the largest number.')

if y>x :
    if y > z:
        print(y, 'is the largest number.')

    if z > y:
        print(z, 'is the largest number.')'''

#               Approach 2

x = float(input('Enter first Number: '))
y = float(input('Enter second Number: '))
z = float(input('Enter third Number: '))
max = x
min = y
if y > max:
    min = max
    max = y

if z > max:
    max = z

if z < min:
    min = z
print(max, 'is the largest number.!! \n And', min, ' is the smallest number.')