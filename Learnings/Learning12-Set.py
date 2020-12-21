# Set is unordered collection of unique elements
# Sets are mutable
# elements in a set must be immutable.
p = {6,23,44,46,2382839}
print (p)
print (type(p))
# if you want to create empty set, you have to use set constructor
e = set()
s = set([2,4,16,64,4096])
print (s)

# there is no duplicates in the set. That's common usage to use set to remove duplicates.
t = [1,4,2,1,7,9,9]
sj = set(t)
print (sj)

# if we want to iterate the element
for x in {1,2,4,8,16,32}:
    print (x)
q = {2,9,6,4}
print (f' is 3 in the q?: {3 in q}')
sj.add(54)
print (sj)
sj.update([33,55,33,9])

# you can use k.remove or k.discard to remove object.
# when you use remove, if element is not there, then it will trigger key error.
# if you use discard, then it won't show any error.
sj.discard(3223)
#sj.remove(3323)

# set support copy method which supports shallow copy.
j = sj.copy()
print (f'j value is: {j}')

# looks like reason to use set
# use set to remove duplicates
# use set to do set algebra
# set union(get set subset), set difference (get superset), set intersection ( get set disjoint)
blue_eyes = {'Olivia','Harry','Lily','Jack','Amelia'}
blond_hair = {'Harry','Jack','Amelia','Mia','Joshua'}
smell_hcn = {'Harry','Amelia'}
taste_ptc = {'Harry','Lily','Amelia','Lola'}
o_blood = {'Mia','Joshua','Lily','Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

if blue_eyes.union (blond_hair) == blond_hair.union(blue_eyes):
    print ('blue_eys and blond unition are the same')

# define people stay in both sets
blue_eyes.intersection(blond_hair)

# people is blond hair but no blue eye
print (blond_hair.difference(blue_eyes))

# you can collect both sets and look for people don't exist on both sets at same time
print (blond_hair.symmetric_difference(blue_eyes))

# see whether hcn is subset of blond_hair
print (smell_hcn.issubset(blond_hair))

# see 2nd set is supper set of first one.
print (taste_ptc.issuperset(smell_hcn))

# to see whether you are either A or B but never both
print (a_blood.isdisjoint(o_blood))


