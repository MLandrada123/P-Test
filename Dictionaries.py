#a dictionary is  a changeable,unordered collection of unique key:value pairs.{}
#these are fast because they use hashing,allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}
capitals.update({'Germany':'Berlin'})#this adds newvalues in our dictionary since it is changed
capitals.update({'USA':'Las Vegas'})#this updates an existing key.value in the dictionary
capitals.pop('China')#this removes an existing keyvalue in the dictionary
#capitals.clear()# to clear the dictionary

#print(capitals['Russia'])#here we dont use index numbers when we want to print a certain value , we use instead the key :value pair of the value
#print(capitals['Germany'])#incase we enter a key value that doesnot exist in our dictionary hence an error
#print(capitals.get('Germany'))#this get method enables us to safely search whether as value in our dictionary exists without errors with a "none" answer

#other useful dictionary methods
#print(capitals.keys())#this shows only keys not their values
#print(capitals.values())
#print(capitals.items())#this prints all items in the dictionary

for key,value in capitals.items():#another way to print all items in the dictionary
    print(key,value)

import shutil
shutil.copyfile('Dictionaries.py','C:\\Users\\User\\Desktop\\folder python\\Dictionaries.py')
