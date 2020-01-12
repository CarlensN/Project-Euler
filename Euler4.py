import math


def reverseNumber(n):
    reversedNumber = 0
    remainder = 0
    while n > 0:
        remainder = n % 10
        reversedNumber = (reversedNumber * 10) + remainder
        n = math.floor(n / 10)
    return reversedNumber


def isPalindromic(n):
    if n <= 10:
        return False
    if n == reverseNumber(n):
        return True
    else:
        return False

""" print(reverseNumber(181))
print(isPalindromic(181)) """

if __name__ == '__main__':
    arr = []
    pal = 0
    for i in range(10, 1000):
        for j in range(10, 1000):
            pal = i * j
            if isPalindromic(pal):
                arr.append(pal)
    print(max(arr)) 
