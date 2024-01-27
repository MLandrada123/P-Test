#list is used to store multiple items in a single variable

food = ["Pizza","Hamburger","Hotdog","Spaghetti"]#we can add multiple items under this variable by making the "food" a list with []
#print(food[0])#within these[]we put in the index of the items we nedd to be printed from 0
#we can always update,add or replace  the items on the list after printing it
food[0] = "Sushi"#this replaces pizza from being index 0 to Sushi
#print(food[0])

#Useful functions to do with Lists
##food.remove("Hotdog")#this removes hotdog from our list
#food.pop()#this removes the last element in the list
#food.insert(2,"cake")#this inserts an item in a given index
#food.sort()#this sorts food alphabetically
#food.clear()#this will clear all off on the elemnts in the list




for x in food:#this element prints all of the element found in our food list
    print(x)
import shutil
shutil.copyfile('Lists.py','C:\\Users\\User\\Desktop\\folder\\Lists.py')


