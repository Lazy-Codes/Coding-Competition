m = 12345.567
print(m)
print('===============')

# 55555 + 100**2

m = 55555 + 100**2
print(m)
print('=============')

a = 3
if a < 3 :
    print('True')
else :
    print('False')
print('===========')

a = True
print(type(a))
print('===========')

import numpy as np
a = np.array([1,2,3,4,5])
print(a.min())
print('==========')
print(a.max())
print('========')

# cos 90 + sin 90 / sqrt 99

import numpy as np 
a = 90
b = 90
c = 99
result = (np.cos(a) + np.sin(b) / np.sqrt(c))
print(result)
print('=============================')


# x ** 20 + 1 - 500/log10
# import numpy as np
# a = 10 
# b = print(np.log(a))
# c = (int(20 + 1 - 500) / b)
# print(c)

import numpy as np
a = 20 + 1 - 500
b = 10
x = 1
result = (x ** a / np.log(10)) 
print(result)
print('======================')


for floor in range (1,8)  :
    print(floor)
print('==========')

a = 1000.50
print(int(a))