# for i in range (1,13) :
#     for n in range (1,13) :
#         print('{0} * {1} = {2}'.format(i,n,i*n))
#     print("=================")

# n = int(input("Input the first number : "))
# m = int(input("Input the second number : "))
# result = n * m
# print('{0} * {1} = {2}'.format(n,m,result))

m = 40
while m > 2 :
    m /= 4
    print(m)
print("==========")

# z = 5
# if z > 10 :
#     print("Z is a Big Number")
# elif z == 5 :
#     print("Figure is Equal")
# else :
#     print("Z is a Small Number")

# import numpy as np
# np.random.seed(234)
# coin = np.random.randint(1,7)

import numpy as np
m = np.array([1,2,3,4,5,6])
n = np.array([6,5,4,3,2,1])
print(m * n)
print("==========")

import numpy as np
a = np.arange(7)
print(a)
print("===========")


import numpy as np
a = np.empty(2)
print(a)
print("==========")

import numpy as np
a = np.linspace(0, 15, num = 6)
print(a)
print("===================================")

import numpy as np
arr = np.array([7,2,4,5,1,6,3])
print(np.sort(arr))
print("======================")

import numpy as np
# import random as rand
a = np.array([1,2,3,4,5,6,7])
print(np.random.choice(a))
print('============')

# a = int(input("Enter Your Number : "))
# while a < 7 :
#     a += 1
#     print(a)
# print("=========")

# for p in 'python' :
#     print(p.upper())
# print('=======')

# a = 5
# if a < 4 :
#     print('GAMEOVER')
# else :
#     print('PROCEED')
# print('==========')





