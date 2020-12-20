"""
Tuple is immutable sequence of arbitrary objects. 
Once created, you can't add/remove objects. 
Tuple is similar as List. but it's immutable instead of multable. 

"""
list01 = [1,"34",34.5]
print (f"I'm a list. {list01}")

t = ("Norway", 4.598, 3)
print (f'This is a tuple example: {t}')
print (f'This is a tuple example: {t[0]}')

# Here comes count number of members in the tuple
tnum01 = len(t)
print (f'number of tuple member is {tnum01}')

# we can iterate tuple by using a for loop
for item in t:
    print (item)

# we can cancatenate with + operator, but you have to + with same type (tuple with tuple)
print (f'the added t is {t+(33.888,"teststring")}')
print (f'the new t is {t}')

# Let's see what nested tuple look like
a = ((220,33),(444,55),("test1","test2"))
print (f'a[1,1] is {a[1][1]}')

# let's see whether I can have nested list
b = [ [33,44],["test1","test2"]]
print (f'b is {b[0][0]}')

# if we want to creat a single object tuple, we must add , at the end
a = (33,)
print (f'single a tuple is {a}')

# specify empty tuple ()
a = ()
print (f'a class is {type(a)}')

# you can specify tuple without ()
p = 1,3,4,5,6
print (f'p type is {type(p)}')

def minmax(items):
    return min(items), max(items)

print (f'minmax is {minmax(p)}')
# passing tuple as argument
print (f'minmax is {minmax((3,4,5,6,7,0))}')
# passing list as argument
print (f'minmax is {minmax([3,4,5,6,7,0])}')

# Tuple unpacking
# Destructuring operation taht unpacks data structures into named references
lower, upper = minmax([1,3,4,5,2,6])
print (f'lower is {lower}')
print (f'upper is {upper}')

# or assign triple nested integers to variables.
(a,(b,(c,d))) = (1,(2,(3,4)))
print (f'a,b,c,d are {a},{b},{c},{d}')

# let's try list
[a,[b,[c,d]]] = [11,[12,[13,14]]]
print (f'a,b,c,d are {a},{b},{c},{d}')

# we can also do a fast swap
a = 'jelly'
b = 'bean'
a, b = b, a
print (f'a,b is {a},{b}')


a = 'hello'
b = 'world'
[a, b] = [b, a]
print (f'a,b is {a},{b}')

a = 3
b = 4
a, b = b, a
print (f'a,b is {a},{b}')

# using tuple constructor to convert other variables

a = [54,6243,34]
b = tuple (a)
print (f'b is {b}')

# we can also use tuple to construct a string into a tuple 
a = "Hello Silver"
b = tuple(a)
print (f'b is {b}')


# we can use in and not in to test member of tuple
print (f'see whether 5 is in: {5 in (3,4,5,6)}')
print (f'see whether 5 is not in: {50 not in (3,4,5,6)}')
