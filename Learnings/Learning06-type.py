# Python is very good to pick and choose type
x = [3,4]
x[1] = "hello"
# Names can be rebound to objects of any type
print (f'what x is now {x}')

def add (a,b):
    return a + b
print (f'a+b is {add(5,7)}')
print (f'a+b is {add(5.1,7.1)}')
print (f'a+b is {add("Hello ","World")}')
print (f'a+b is {add([1,3],[2,4])}')

# However, Python will not generally perform implicit conversions between types. 
# so if you add 3+"3", it won't work. 

""" There are 4 types of scopes in the Python. 
Local - Inside the current fucntion
Enclosing - Inside enclosing functions ???
Global - At the top level of the moduel (not function, but moduel level)
Built-in - In the special builtins module
It's called LEGB rule. 
"""

# __name__ dunder name is provided by Python runtime. Which means run at one time. 
# functions variables belongs to functions.
# module variables belongs to module

count = 0
def show_count():
    print (f'count is {count}')

def set_count(c):
        count = c

show_count()    
# When it runs, show_count has no value of count in the function scope. so it looks up in the module scope. 
set_count(5)
show_count()    
def set_count(c):
    global count
    count = c

set_count(5)
show_count()        