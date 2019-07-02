"""
检查变量的类型

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""
from functools import reduce

a = 100
b = 1000000000000000000
c = 12.345
d = 1 + 5j
e = 'A'
f = 'hello, world'
g = True
h = {
    'name': 'Tars',
    'age': 27,
    4: 'hello'
}
i = [2, 5, 7, 'string']
j = (2, 5, 7, 'string')
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(h[4])

sum_num = reduce(lambda x, y: x+y, [1,2,3,4,5])
print(sum_num)