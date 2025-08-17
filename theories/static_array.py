import sys
from core import Array
n = 5
a = Array(n)
for x in a:
    print(x)

b = Array(n, 'f')
for x in b:
    print(x)