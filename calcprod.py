# program to calculate how long it takes to calculate the product of first 1000000 numbers.

import time
import numpy

def calcProd():
	#calculates product of first 100,000 numbers
	product = 1
	for i in range(1, 100000):
		product = product * i
	return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))

print('Took %s seconds to calculate.' % (endTime - startTime))
