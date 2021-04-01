'''

Bridget Naylor
CECS 229 Lab 3 Part 1.7.1

'''
print ('Hello World')

def my_filter( L, num ):
    new_L = []
    [new_L.append(item) for item in L if item % num != 0]
    return new_L;

L = [1,2,3,4,5,6,7,8,9,10]
num = 2
print(my_filter( L, num ))
