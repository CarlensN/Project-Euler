'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
found = False
target = 1000
a = 0
b = 0
c = 0

for a in range(1, int(target/3)):
    for b in range(a, int(target / 2)):
        c = target - a - b
        if( a*a + b*b == c*c):
            found = True
            break
    if found == True:
        break
print(a)
print(b)
print(c)
print(a*b*c)


