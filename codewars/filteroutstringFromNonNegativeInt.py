"""
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Examples:
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""
def filter_list(l):
    print (f'receive List is {l}')
    newList = l.copy()
    typeStr = type("hello")
    typeInt = type(3)
    for item in l:
        print (f'{item} is a guess ')
        if type(item) == typeStr:
            print (f'{item} is string')
            newList.remove(item)
    print (f'final List is {newList}')
    return newList


filter_list([1, 2, '1', '123', 123])
#filter_list([1,2,'a','b'])
