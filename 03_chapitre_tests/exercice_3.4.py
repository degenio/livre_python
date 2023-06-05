###### Solution 1 ###### 
a = int(input('Saisir a:'))
b = int(input('Saisir b:'))
c = int(input('Saisir c:'))
max = a
min = b
if b > a:
    max = b
    min = a

if max < c:
    max = c
elif min > c:
    min = c

print(min, max)


###### Solution 2 ###### 
a = int(input('Saisir a:'))
b = int(input('Saisir b:'))
c = int(input('Saisir c:'))
max, min = a, b

if b > a:
    max, min = b, a

if max < c:
    max = c
elif min > c:
    min = c

print(min, max)
