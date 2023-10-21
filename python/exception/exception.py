# compile time : syntax, spelling 
# logical : no wrong with syntx, wrong o/p
# run time : user giving wrong i/p, 

a = 5
b = 8
x = 10

try:
    print(a/b)
    c = int(input('Enter Value : '))
    print(c)
    for i in range(x):
        print(i)
    print('No Error Occured')
except ValueError as v :
    print('ValueError Error Occured')
    print('ValueError : ', v )
except ZeroDivisionError as e :
    print('ZeroDivisionError Error Occured')
    print('ZeroDivisionError : ', e )
except Exception as r :
    print('Error Occured')
    print('Error : ', r )
finally:
    print('Resource Closed')

# user define exception
class MyException(Exception):
    pass

c = 25
if c > 5 :
    raise MyException("somrting went wrong")