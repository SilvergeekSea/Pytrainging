
x = """ This is
    a test
    string"""
print (x)

y = 'This string\nspans multiple\nlines'
print(y)

strTest = '"Yes!", he said, "I agree!"'
print(strTest)


# Str is immutable in memory. 

# adjacent sentence will join together
strTest02 = "first" "second"
print (strTest02)
# Here comes multiple lines
# Multiline strings
""" This is 
    a multiline
    string"""

m = 'This string \nspans multiple\n lines'
print (m)
# Escape sequences
"This is a \" in a string"
'This is a \' in a strong'
# however, this maybe confusing
'This is a \" and a \' in a string'
k = 'A \\ in a string'

txt01 = "We are the so-called \'Vikings\" from the north."
print (f'txt01 = {txt01} ')

# Python supports raw string
txt02 = r'This is \ my raw string \\ \n How about a single quote\' " testing'
txt03 = r"This is another ' raw string' for testing single quote"
print (f'txt02 = {txt02}')
print (f'txt03 = {txt03}')

# Testing convert number and float to string
txt04 = str(458)
txt05 = str(5434.22)
print(f'txt04 = {txt04} and txt05 = {txt05}')

# We can access single character in the string by use []
s = 'parrot'
print (f's[1] = {s[1]}')

# in Python,there is no character type. Only string. so s[1] will be a string type as well
result = type (s[1])
print (f'result = {result}')


# string type has its own methods. You can use help(str) to find out.

# Let's capitalize the string

print (f'Let\'s print capitalize S variable: {s.capitalize()}')

# let's titlecase the string
print(f'Let\'s Title case the string {s.title()}')

# str is Unicode





# List is mutable. List is sequences of objects. 
# content of List can be int, float, string or another list
List01 = [1,9,8]
print (f'List01 is {List01}')
List02 = ["apple", "orange", "watermelon"]
print (f'List02 is {List02}')
print (f'List01[1] is {List01[1]}')
typeResult = type(List01[1])
print (f'List01[1] type is {typeResult} ')
List01[1] = "test33"
print (f'replaced List01[1] is {List01[1]}')

# Create an empty list
emptyList01 = []
emptyList01.append(1.638)
emptyList01.append("testAdd22")
print (f'Added list is {emptyList01}')

# Create a list from a string
List02 = list("Hello world")
print (f'List02 is {List02}')

# a fancy way to create a list
List03 = ["test",
          "truth",
          "is unpredictable",]
print (f'List03 is {List03}')