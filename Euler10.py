'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
def isPrime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return False
    return True

max = 2000000
sum = 0
for i in range(2,max+1):
    if isPrime(i):
        sum += i


print(sum)