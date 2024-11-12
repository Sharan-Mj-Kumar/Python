import numpy as np
from numpy import random
import pandas as pd

li=random.randint(2,20,size=(12))
print("List of Values :",li)
print()

print("Maximum :",max(li))
print("Minimum :",min(li))
print()

print("Ascending Order :",np.sort(li))
print("Descending Order :",np.sort(li)[::-1])
print()

print("Mean :",li.mean())
print()

arr1=li.reshape(3,4)
print("3 x 4 Matrix :-")
print()
print(arr1)
print()

arr2=li.reshape(4,3)
print("4 x 3 Matrix :-")
print()
print(arr2)
print()

print("\n Multiple of Two matrix :\n",np.dot(arr1,arr2))

Output:-

List of Values : [18  8 10 13  9  6 16  4 17 12  7 14]

Maximum : 18
Minimum : 4

Ascending Order : [ 4  6  7  8  9 10 12 13 14 16 17 18]
Descending Order : [18 17 16 14 13 12 10  9  8  7  6  4]

Mean : 11.166666666666666

3 x 4 Matrix :-

[[18  8 10 13]
 [ 9  6 16  4]
 [17 12  7 14]]

4 x 3 Matrix :-

[[18  8 10]
 [13  9  6]
 [16  4 17]
 [12  7 14]]


 Multiple of Two matrix :
 [[744 347 580]
 [544 218 454]
 [742 370 557]]
