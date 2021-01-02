"""try:
    print(10/0)
except ZeroDivisionError as msg:
    print('error raised:',msg) """

'''# try with multiple except blocks

try:
    a = int(input('enter first number: '))
    b = int(input('enter second number: '))
    print(a/b)
except ZeroDivisionError:
    print('zero_division_error')
except ValueError:
    print('value_error') '''

# Single Except Block Can Handle Multiple Exceptions

'''try:
    m = int(input('enter first num: '))
    n = int(input('enter second num: '))
    print(m/n)
except (ZeroDivisionError,ValueError) as msg:
    print('pls provide only numbers: ',msg)'''

# Default Except Block

'''try:
    m = int(input('enter first num: '))
    n = int(input('enter second num: '))
    print(m/n)
except ZeroDivisionError:
    print('ZeroDivisionError: cant devide with zero')
except:
    print('default except: provide valid input')'''

# Finally
'''try:
    print('try')
    print(10/0)
# except ZeroDivisionError:
except ValueError:
    print('except')
finally:
    print('finally')'''


# in only one scenario finally block will not excecuted i.e. os._exit(0) it will shut down PVM
import os
try:
    print('try')
    os._exit(0)
    print(10/0)
except ValueError:
    print('except')
finally:
    print('finally')