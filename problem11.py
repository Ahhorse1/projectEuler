from numpy.core.fromnumeric import prod
import pandas as pd
import numpy as np

def getLargestAdjacentProduct(matrix, i, j):
    largestProduct = 0
    if i > 2:
        product = matrix[i][j]*matrix[i-1][j]*matrix[i-2][j]*matrix[i-3][j]
        if product > largestProduct:
            largestProduct = product
        if j > 2:
            product = matrix[i][j]*matrix[i-1][j-1]*matrix[i-2][j-2]*matrix[i-3][j-3]
            if product > largestProduct:
                largestProduct = product
        if j < 17:
            product = matrix[i][j]*matrix[i-1][j+1]*matrix[i-2][j+2]*matrix[i-3][j+3]
            if product > largestProduct:
                largestProduct = product
    if j > 2:
        product = matrix[i][j]*matrix[i][j-1]*matrix[i][j-2]*matrix[i][j-3]
        if product > largestProduct:
            largestProduct = product
        if i < 17:
            product = matrix[i][j]*matrix[i+1][j-1]*matrix[i+2][j-2]*matrix[i+3][j-3]
            if product > largestProduct:
                largestProduct = product
    if i < 17:
        product = matrix[i][j]*matrix[i+1][j]*matrix[i+2][j]*matrix[i+3][j]
        if product > largestProduct:
            largestProduct = product
        if j < 17:
            product = matrix[i][j]*matrix[i+1][j+1]*matrix[i+2][j+2]*matrix[i+3][j+3]
            if product > largestProduct:
                largestProduct = product
    if j < 17:
            product = matrix[i][j]*matrix[i][j+1]*matrix[i][j+2]*matrix[i][j+3]
            if product > largestProduct:
                largestProduct = product
    
    return largestProduct

file = open('matrix.txt', 'r')

matrix = [[0]*20]*20
matrix = np.array(matrix)

for i in range(0, 20):
    for j in range (0, 20):
        matrix[i][j] = int(file.readline(3))


largestProduct = 0
for i in range (0, 20):
    for j in range (0, 20):
        product = getLargestAdjacentProduct(matrix, i,j)
        if product > largestProduct:
            largestProduct = product

print(largestProduct)



