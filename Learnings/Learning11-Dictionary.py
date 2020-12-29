# here comes example of dictionary
urls = {'Google': 'http://www.google.com',
        'Pluralsight': 'http://pluralsight.com',
        'Sixty North': 'http://sixty-north.com',
        'Microsoft': 'http://microsoft.com'}

print (f'urls["Google"] is {urls["Google"]}')

# the key must be immutable. so string, tuple are fine, but for the list.
# value object however may be mutable or immutable.
# Do NOT rely on the order of dictionary essentially its a random order.

# use dict.get(key) which returns the value or None if the key is not present (or get(key, not-found) allows you to specify what value to return in the not-found case).

# convert tuple object to dictionary.
names_and_ages = [('Alice',32),('Bob',48),('Charlie',28),('Daniel',33)]
d = dict(names_and_ages)
print (f'd value is {d}')

# or you can use direct method
phonetic = dict(a='alfa',b='bravo',c='charlie')
print (f'phonetic is {phonetic}')

# just like list, dictionary has shallow copy.
e = phonetic.copy()
print (f'e value is {e}')
# you can also pass existing dictionary as parameter
f = dict(e)

# you can extend one dictionary from another dictionary
# if new value is there, the old value will be replaced by new one.
g = dict(wheat=0xF5DEB3,khaki=0xF0E68C,Alice=42)
f.update(g)
print (f'f.update is : {f}')

# Dictionary is iterable. so you can use for loops
# Dictionaries yield the next key on each iteration.
# Values can be retrived using the square brackets.
for key in f:
    print(f'the key is : {key} => {f[key]}')
# notice the order of result is sorted by the key

for value in f.values():
    print (value)

for key in f.keys():
    print (key)

# using tuple unpacking
for key,value in f.items():
    print (f'{key} => {value}')

if "Alice" in f:
    print ('Yes, Alice is in the Dictory')
if 42 in f:
    print ('Yes, 42 is in the words)')
# looks like you can only use in, not in with key not the value.

# we can delete key with del
del f['Alice']
print (f'the dict is : {f}')

# you can modify the value of dict, but not key. but you can delete key or add
m = {'H': [1,2,3],
     'He': [3,4],
    'Li': [6,7]}
m['H'] +=[4,5,6]
print (f'm is : {m}')
m['N'] = [13,41,15]

# use pretty print, you must overwrite byusing as otherwise, you can't access orgiinal contenet of pp

from pprint import pprint as pp
pp(m)
