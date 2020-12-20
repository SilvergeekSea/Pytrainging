# Sequence representing an arithmetic progression of integers
# call range constructor to build a range (stop)
a = range(5)
print (f'a is {a}')

# range can be used as loop counters
for i in range(5):
    print (i)

# we can also created 2 values range (start,stop)
a = range(5,10)
print (f'a is {list(a)}')

# you can also skip numbers by 2 range(start,stop,step)
a = range(5,10,2)
print (f'a is {list(a)}')

# Range doesn't support keyword arguments

# if you need to count the object, use enumerate option. 
# Constructs an iterable of (index, value) tuples around another iterable object

t = [3,44,662,3889,40485]
for p in enumerate(t):
    print (p)

for i, v in enumerate(t):
    print (f'i is {i}, v is {v}')