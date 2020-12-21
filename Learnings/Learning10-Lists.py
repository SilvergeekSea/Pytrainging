# Using -1 to get last itme of list
r = [1,3,4,5,-16]
print (f'last item is {r[-1]},2nd last item is {r[-2]}')

# Slicing is very important. It is extended form of indexing for referring to a portion of a list or other sequence.
# syntax: a_list[start:stop]
# remove first and last , use s[1:-1]
s = [1,2,3,4,5]
print (f's[1:3] is {s[1:3]}, s[1:-1] is {s[1:-1]}')
# from 2 to the end
print (f's[2:] is {s[2:]}')

# from beging to [2] but not include [2]
print (f's[:2] is {s[:2]}')

# retrieve all elements
print (f's[:] is {s[:]}')

# you can use it to copy a list
t = s
print (f't is s: {t is s}')
r = s[:]
print (f'r is s: {r is s}')
print (f'r == s: {r == s}')
# be aware the r content (each member) is still pointing same memory as s member.
u = s.copy()
print (f'u is s: {u is s}')
print (f'u == s: {u == s}')
# or you can do this
v = list(s)

# all those techniques perform a shallow copy (copy links or pointers, not the value)
# the new list contains same object references as source, but not value.
a = [[1,2],[3,4]]
b = a[:]
print (f'a is b: {a is b}')
print (f'a == b: {a == b}')
print (f'a[0] is b[0]: {a[0] is b[0]}')
print (f'a[0] == b[0]: {a[0] == b[0]}')

a[0] = [8,9]
print (f'a[0] is b[0]: {a[0] is b[0]}')
print (f'a[0] == b[0]: {a[0] == b[0]}')

# change a list object
a[1].append(5)
print (f'a is b: {a is b}')
print (f'a == b: {a == b}')
print (f'a[1] is b[1]: {a[1] is b[1]}')
print (f'a[1] == b[1]: {a[1] == b[1]}')
print (f'b[1] is {b[1]}')

# You can also do multiplication
c = [2,4]
d = c * 2
print (f'd is : {d}')

# You can initalize list with constant value
c = [0] * 9
print (f'c is: {c}')

# however, this replication will only repeat reference but not value
s = [[1,-1]] * 5
print (f's is : {s}')
s[2].append(5)
print (f's is : {s}')

# using list.index() too find the location of an object in a list
w = "the quick brown fox jumps over the lazy dog".split()
i = w.index("fox")
print (f'i is: {i}')
w.count("the")
print (f'the is in: {"the" in w}')

# use del to remove by index
del w[3]
print (f'sentence is {w}')

# or u can use remove method
w.remove('brown')
print (f'sentence is {w}')

# insert method list.insert()
a = 'I accicdentally the whole universe'.split()
a.insert(2,"destroyed")
print (f'a is : {a}')
' '.join(a)
print (f"a is : {' '.join(a)}")


# list operation
m = [2,1,3]
n = [4,7,11]
k = m + n
k += [18,28,40]
k.extend([33,55,66])
print (f'k is : {k}')

# list reverse and sorting (warning, it IN PLACE doing it)
g = [144,11,21]

print (f'g is: {g}')
g.reverse()
print (f'reverse g is: {g}')
g.sort()
print (f'sorted g is: {g}')
g.sort(reverse = True)
print (f'acending sorted g is: {g}')

# sort with key
h = 'not perplexing do hadwriting family where I illegibly know doctors'.split()
h.sort(key=len)
' '.join(h)
print(f'h is: {h}')

# you may want to use reversed() and sorted() are out of place which created a new list
x = [4,9,2,1]
y = sorted(x)
print (f'y is : {y}')

q = reversed(x) # only iterator, not new list.
y = list(q)
print (f'y is : {y}')

def silvertest():
   print "hello"

