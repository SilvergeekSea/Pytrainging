"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""
def find_it(seq):
    for item in seq:
        testItem = item
        count = 0
        for subItem in seq:
            if item == subItem:
                count += 1
        if (count % 2 )== 1:
            print (f"the odd item is {item}")
            return item


find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])