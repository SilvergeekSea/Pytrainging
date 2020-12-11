"""
You live in the city of Cartesia where all roads are laid out in a perfect grid. 
You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
The city provides its citizens with a Walk Generating App on their phones 
-- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block,
 so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, 
 of course, return you to your starting point. Return false otherwise.


"""

import sys

def is_valid_walk(walk):
    #determine if walk is valid
    x=0
    y=0
    z=0
    print("This is inside is_valid_walk function")
    for direction in walk:
        z+=1
        if direction=='n':
            y+=1
            print ("direction is ",y)
        #print(direction)
        if direction=='s':
            y-=1
            print ("direction is ",y)
        if direction=='w':
            x-=1
            print ("direction is ",x)
        if direction=='e':
            x+=1
            print ("direction is ",x)
    print ("x = ", x)    
    print ("y = ", y)    
    print ("z = ", z)    
    if x==0 and y==0 and z==10:
        print("back to 0 with in 10 minutes")
        pass
        return True
    else:
        print("no, it's not working")
        return False

def main(walk):
    walk_distance = is_valid_walk(walk)
    print (walk_distance)


if __name__=='__main__':
    main(sys.argv[1])
else: 
    main(['w','e','w','e','w','e','w','e','w','e','w','e'])
