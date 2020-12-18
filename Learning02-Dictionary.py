# Map Keys to Values
d = {'alice': '0438383', 'bob': '38938345', 'eve': '87373763'}
print (f'd is {d["alice"]}')

# assign alice with new value
d['alice'] = '9988988'
print (f'd[alice] is {d["alice"]}')

# add a new key
d['newcomer'] = '33348458'
print (f'print d is {d}')

# dict order is sorted by entry time

# create a new empty dict
e = {}


# for-loop
# create a new list and use for-loop to emulate 
cities = ["London", "New York", "Paris", "Osis", "Lijiang"]
for city in cities:
    print (f"City name is {city}")

# create a new dict and iterate them
colors = {'crimson': 0xdc143c, 'coral': 0xff7f50, 'teal': 0x008080}
for color in colors:
    print (f'The color is {color}, {colors[color]}')

