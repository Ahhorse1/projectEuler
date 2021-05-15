import math

def factorCounter(num):

def isPrime(num):
    if num <= 3:
        return True
    
    for i in range(3,math.sqrt(num), 2):
        if num%i == 0:
            return False
    
    return True



def calculateTriangleNumber(n):
    return (n+(n+1))/2

foundTriangleNumber = False
j = 1
triangleNumber = 0
while foundTriangleNumber != True:
    triangleNumber = triangleNumber + j
    if factorCounter(triangleNumber) >= 500:
        foundTriangleNumber = True
    j = j + 1

print(triangleNumber)