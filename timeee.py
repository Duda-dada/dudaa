from random import randint

N = 100
A = [0] * N
for i in range(N):
    A[i] = randint(-1000, 1000)
B = A
print(B)
from sorts import bubble_sort
import time

start=time.time()
print(bubble_sort(B.copy()))
finish=time.time()
Res=(finish - start)*1000
print(Res, 'b')

#3333

from sorts import selection_sort
print(B)
start=time.time()
print(selection_sort(B.copy()))
finish=time.time()
Res=(finish - start)*1000
print(Res, 's')

from sorts import insertion_sort
print(B)
start=time.time()
print(insertion_sort(B.copy()))
finish=time.time()
Res=(finish - start)*1000
print(Res, 'i')

