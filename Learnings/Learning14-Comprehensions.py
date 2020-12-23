# Concise syntax for describing lists, sets, and dictionaries.
words = "Why sometimes I have believed as many as six impossible things before breakfast".split()
print (words)
# List comprehension
[len(word) for word in words]
print ([len(word) for word in words])

# list comprehension Syntax
# [expr(item) for item in iterable]

# this is the same thing as below
# lengths = []
# for word in words:
#     lengths.append(len(word))
# it can be any Python expression
from math import factorial
f = [len(str(factorial(x))) for x in range(20)]
print (f)

# set comprehension - this removes duplication
from math import factorial
s = {len(str(factorial(x))) for x in range(20)}
print (s)

# Dict comprehension
country_to_capital = { 'United Kingdom': 'London',
                       'Brazil': 'Brasilia',
                       'Morocco': 'Rabat',
                       'Sweden': 'Stockholm' }

# key:value for assign key,value with tuple and in iterate with .item() which is special thing about dictionary comprehensions.
captial_to_country = { capital: country for country, capital in country_to_capital.items()}

from pprint import pprint as pp
pp (captial_to_country)

words = ["hi","hello","foxtrot","hotel"]
newList = {x[0]: x for x in words}
pp(newList)


# Filtering Comprehensions
from math import sqrt
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) +1):
        if x % i ==0:
            #print (f'x is {x} and is NOT a prime')
            return False
        #print (f'x is {x} and is prime')
    return True

newList = [x for x in range(101) if is_prime(x)]
print(newList)

# Iteration Protocols
iterable = ['Spring','Summer','Autumn','Winter']
iterator = iter(iterable)
print(next(iterator))

# Generator functions
def gen123():
    yield 1
    yield 2
    yield 3

g = gen123()
print(type(g))
# generator is itertor
print (next(g))
print (next(g))

for v in gen123():
    print (v)

# each time you call generator, it generates a new instance of generator
h = gen123()
i = gen123()
print (id(h))
print (id(i))

def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6

g = gen246()
next(g)
next(g)
next(g)
#next(g)

