# we can know length of string
a = "asdfasdlkfnlkvaoinewoi32n320r9un32nfewvsdjhosan3209"
print (f'lenth of string a is : {len(a)}')

# try couple of cancanator 
a = "hello" + "world"
a = "silver"
a += "chen"
print (f'a value is: {a}')

# you can use + to concatenator , you need to consider to use str.join for large data as it's more .
# efficient. may cause temporary memory leak

# str.join() inserts a separator between old string and new string or collection of strings.
# call join() on the separator (eg: ;) string
colors = ';'.join(['hello','world','this','is','Silver'])
print (f'color is {colors}')
print (f'color split is {colors.split(";")}')

# another way to join
true_colors = ''.join(["red","blue","green"])
print (f'true_colors is {true_colors}')

# partition 
a = "unforgetable"
print (f'a partition is {a.partition("forget")}')

# travel plan
depature,separator,arrival = "Melbourne:Shanghai".partition(':')
print (f'departure is {depature}, arrival is {arrival}')

# we use _ as dummy value or unused value
orgin, _, destination = "Seattle-Boston".partition("-")
print (f'origin is {orgin}, destination is {destination}')

# String formatting with replacement fields
a = "{0} north {1} east".format(59.1,10.04)
print (f'a is {a}')
b = "The age of {0} is {1}. {0}'s birthday is on {2}".format('Fred',24,'October 31')
print (f'b is {b}')

# if you use all argment is exactly once, then number can be ommitted
a = "Reciculating spline {} of {}.".format(4,23)
print (f'a is {a}')

b = "Current position {latitude} {longitude}".format(latitude = "60N", longitude = "5E")
print (f'b is {b}')

c = "Galactic position x ={pos[0]}, y={pos[2]}, z={pos[1]}".format(pos=(56.2,23.1,82.2))
print (f'c is {c}')

import math
a = 'Math constants: pi = {m.pi:.3f},e={m.e:.3f}'.format(m=math)
print (f'a is {a}')

value = 4 * 20
s = 'The value is {value1}'.format(value1 = value)
print (f's is {s}')

# F-string syntax
print (f'one plue one is {1+1}')

import datetime
print (f'The current time is {datetime.datetime.now().isoformat()}')