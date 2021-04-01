'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello World')

def my_filter( L, num ):
    new_L = [L.append(item) for item in L if item % num != 0]
    print(new_L)
    return new_L;

L = [1,2,3,4,5,6,7,8,9,10]
num = 2
my_filter( L, num )
