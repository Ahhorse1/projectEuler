import math

def factorCounter(num):
    totalFactors = 0
    # Check from 1 to Sqrt(Num)
    for i in range(1,math.floor(math.sqrt(num))):
        # if i == Sqrt(Num), then only 1 additional factor
        if num % i == 0:
            if num/i == i:
                totalFactors = totalFactors + 1
            else:
                totalFactors = totalFactors + 2
    return totalFactors

def calculateTriangleNumber(n):
    # Base Case
    if n == 1:
        return 1
    # Gauss Sum
    return (n*(n+1))/2

numFactors = 0
counter = 1
triNum = 0
# Check each triangle number until one with 500 factors is found
while numFactors < 500:
    triNum = calculateTriangleNumber(counter)
    numFactors = factorCounter(triNum)
    counter = counter + 1
print(triNum)