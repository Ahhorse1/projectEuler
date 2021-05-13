def factorCounter(a):
    counter = 0
    for i in range(1,a+1):
        if a%i == 0:
            counter = counter + 1
    return counter


foundTriangleNumber = False
j = 1
triangleNumber = 0
while foundTriangleNumber != True:
    triangleNumber = triangleNumber + j
    if factorCounter(triangleNumber) >= 500:
        foundTriangleNumber = True
    j = j + 1

print(triangleNumber)