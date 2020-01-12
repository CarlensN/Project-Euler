def isPrime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return False
    return True


primeNum = []
max = 10001
i = 2
while len(primeNum) < max:
    if isPrime(i):
        primeNum.append(i)
    i = i + 1

#index max - 1 since we want the 10001st prime number and the array starts at index 0
print(primeNum[max - 1])



