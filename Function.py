#function is a block of code which is executed only when it is called
def hello(first_name,last_name,age):#inorder for our argument to be accepted we require the a parimeter therefore we express the value of the perimeter as "name".which you also apply to be printed
    #pass if you do not know what you want to function to do, then print pass and continue
    print("hello "+first_name+" "+last_name)#we can send our function information and it does something about it ie name is an unresolved reference
    print("You are "+str(age)+" years old")#the intergers must be converted to strings so that they can be printed togethe
    print("have a nice day!")#it can not only be a word but more........


import shutil
shutil.copyfile('Function.py','C:\\Users\\User\\Desktop\\folder\\Function.py')

#hello()#since we have our function already,inorder to execute it ,we type the name of the function ,when it is deleted,then the program will do nothing
#hello()#this is printed as much times you execute it
#hello("Landrada")#this new information  sent to a function is called an argument
#hello("Mia")#after inserting the perimeter we can now freely execute our function with different values to be printed down
#we can always
#name = "Giramata" # a new argument can be always sent as long as there is a parimeter that has a nickname
#hello(name)
#We can always send more than one argument what is important is that we need to have a matching perimeter tp the argument ie:
#hello("Landrada","Mia")#for thus argument to be accepted ,we adjust the perimeter to two nicknames  to match with the argument instead of only "name"
#we can also send other data values like intergers as below.therefor all you need to do is to adjustbmatching perimeters up
hello("Landrada","Mia",18)
