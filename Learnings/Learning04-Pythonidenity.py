# remember int and string are immutable
x = 1000
x = 500
print (f'x is {x}')

# Let's get Y involved
y = x 
# now, let's reassign x
x = 3000
print (f'x is {x} and y is {y}')

# using id() to show the pointer
print (f'x id is {id(x)} y id is {id(y)}')

# you can use is function to test id
if y is x:
    print ("y id is same as x")
else:
    print ("no, y id is not same as x")

# the ground run is assigning object is always bind object with name not value. 

# mutable object is different
r = [2,4,5]
print (f'r is {r}')
s = r
print (f's is {s}')
r[1] = 9
print (f'after change, r is {r}')
print (f'after change, s is {s}')


# Python doesn't have variables in the same sense of boxes holding a value
# Python has named references to objects. 

# Value vs identity Equality
p = [4,7,11]
q = [4,7,11]
if p==q:
    print ('p is equal q, we actually compare the value')
else:
    print ('p is NOT equal q')

if p is q:
    print ('p and q are pointing same object')
else:
    print ('p and q are NOT pointing same object')

# value equality and identity equality are different concepts. 
