# Passing Arguments and Returning Values
m = [9,15,24]
def modify(k):
    k.append(39)
    print (f'inside of modify function, k list is {k}')
    return k
modify(m)
print (f'after modify function, m list is {m}')


# Test replace list
f = [14,23,37]
def replace (k):
    k = [22,44,66] # This assigned entire new list object rather than modify individual
    print (f'inside of replace function, k list is {k}')
    return k
replace(f)
print (f'after replace fucntion,  f list is {f}')


#  Test similar thing with string
strTest01 = "abcdefg"
def modify(k):
    k = "hello"
    print (f'inside of function, k string is {k}')
    return k
modify(strTest01)
print (f'after function, strTest01 list is {strTest01}')



# so in short, g[0] = 33 is replace individual list object. 
# g = [33,44,55] is binding g with new list object. 

# function arguments are object-reference (link or pointer)
# the reference (link or pointer) is copied but not value itself. 
# when function returns, it returns reference as well, not value. 

def f(d):
    return d

c = [1,3]
e = f(c)
if c is e:
    print ('c is e with same refernnence ')    

# we can setup a default value for function arguments
# the argument list must start with arguments without default value, otherwise, it will be syntax error. 
def banner(message, border='-'):
    line = border * len(message)
    print (line)
    print (message)
    print (line)

banner ("Critical Role stories")
banner ("hello world", "*")
banner ("This is a test 3", border="=")
# This is a test 3 is called position argument (as it doesn't have keyword) and border is called keyword argument 
# if all argments are keyword argements, then you can switch the positions.
banner (border="*",message="This is testing for switch position")

# When are default values evaluated? 
import time
print (f"current time is {time.ctime()}")
def show_default(arg=time.ctime()):
    print(f'arg with in the show_default function is {arg}')

show_default()

# We can run mutliple show_default(), it will show the same time. The reason for that is
# when the default value is evaluated when def is executed (only once) at run time. 
# then doesn't matter how many times you run function, def only run once. hence, the default value is the same. 
# immutable default values doesn't cause problem like str or int. 
# but list or other mutable values may cause confusing effect. 

def add_spam(menu=[]):
    menu.append("spam")
    return menu

breakfast = ['bacon','eggs']
print (f'add_spam function return is {add_spam(breakfast)}')

lunch = ['baked beans']
print (f'add_spam function return is {add_spam(lunch)}')

print (f'add_spam function with no arguments, return is {add_spam()}')
print (f'add_spam function with no arguments, return is {add_spam()}')

# ground rule: always use immutable objects for default value

def add_spam2(menu=None):
    if menu is None:
        menu = []
    menu.append("spam")
    return menu

print (f'add_spam function with no arguments, return is {add_spam2()}')
print (f'add_spam function with no arguments, return is {add_spam2()}')

