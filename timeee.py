from random import randint

N = 10
A = [0] * N
for i in range(N):
    A[i] = randint(-1000, 1000)
B=A
print(B)
from sorts import bubble_sort
import time
N = 1000
A = [0] * N
for i in range(N):
    A[i] = randint(-1000, 1000)
B=A
print(B)
start=time.time()
bubble_sort(B)
finish=time.time()
Res=(finish - start)*1000
print(Res)