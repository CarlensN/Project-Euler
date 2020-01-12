sumOfSquares = 0
sum = 0

for i in range(1,101):
    sumOfSquares = i**2 + sumOfSquares
    sum+=i


print(sum**2 - sumOfSquares)