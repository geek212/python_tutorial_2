# What is class ?
'''
 Class is a blueprint or u can say its a template  for cerating the objects
it enscapsulates data ans methods that operate on that data allowing for the
Creation of reusble and modular code . 

'''




"""

Class: A piece of code from which you can generate a unique object, where 
each object is a single instance of the class. Think of it as a blueprint or factory 
from which you can create individual objects.

# """

# You can cerate your own classes like you create your own functions. You are free to 
# name the class whatever you want, so long as it’s a legitimate name that starts 
# with a letter and contains no spaces or punctuation.


# Define new class named Member 
class Member:
    '''defined new member of class'''

# It’s customary to start a class 
# name with an uppercase letter to help distinguish classes from variables. To get 
# started, all you need is the word class followed by a space, a class name of your 
# choosing, and a colon (:) . For example, to create a new class named Member




# You can create any name with class until its valid diffrent from variable 

# Define new class named username
class Username:  # passcalcase Username : means frist letter in capital 
        '''Defines new Username of class'''

# Defines new class named address
class addRess :  # camelCase addRess : means capital letter starts from 3rd letter 
        """Defined new addRess of class"""


# However, it isn’t useful until you specify what 
# attributes you want each object that you create from this class to inherit from the class





''' How to Class Cerates instance ? '''

# To grant to your class the ability to create instances (objects) for you, you give 
# the class an init method.





" What is init method  ? "

# The word init is short for (initialize) . As a method, it’s 
# really just a function that’s defined inside of a class. But it must have the specific 
# name __init__ — that’s two underscores followed by init followed by two more 
# underscores.

# That __init__ is sometimes spoken as “dunder init.” The dunder part is short for double underline




"The syntax for creating an init method is"
# def __init__(self[Username,id_no,....])
# def __init__(self[fullname,age,location,.....])
# def __init__(self[sold_unit,Clients_id,country,....])


# The def is short for define, and __init__ is the name of a built-in Python method 
# that’s capable of creating objects from within a class. The self part is just a variable name,
# and it is used to refer to the object being created at the moment. You can use the name of your own 
# choosing instead of self. But self would be considered by most a good “best practice” since it’s 
# explanatory and customary .








# Giving an Object Its Attributes #


# Now that you have a new, empty Member object, you can start giving it attributes 
# and populate (store values in) those attributes. For example, let’s say you want 
# each member to have a .username attribute that contains the user’s username 
# (perhaps for logging in). You have a second attribute named fullname, which is 
# the member’s full name



'''
self.username = uname
self.fullname = fname 

'''



# The first line creates an attribute named username for the new instance (self) 
# and puts into it whatever was passed into the uname attribute when the class was 
# called. The second line creates an attribute named fullname for the new self
# object, and puts into it whatever was passed


# lets define with class
class member :

    """ Cerate a new member """
    def __init__(self, username , fullname):
        
       # define the attributes give them value
        self.username = username
        self.fullname = fullname

# The __init__ line creates a new empty object named self. Then the self.username = uname line adds 
# an attribute named username to that empty object, and puts into that attribute whatever was 
# passed in as uname. Then the self.fullname = fname line does the same thing for 
# the fullname attribute and the fname value that was passed in.




# Creating an instance from a class #

# When you have created the class, you can create instances (objects) from it using 
# this simple syntax:

New_member = member("Ashwin" , "Nair")

# But to make sure, you can print the object or its attributes
print(New_member)
print(New_member.username)
print(New_member.fullname)
print(type(New_member))


# To understand class is bit diffcult some times even its simple
# Some times i get confuse between  attributes and values while codeing it 







# Lets make class with car and also we gonna use def __init__
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

my_car = Car("Toyota", "Corolla", 2021)
print(my_car.get_make())  # output: Toyota


''' In the above example the __init__ method is used to set the initial state
of the Car Object .

The object has the attributes to make, model, year .

The method takes these attributes as arguments and assigns them to the 
object attributes.

finally , the my_car object is created with provided arguments and we can
get the make attributes value by calling get_make or get_model , get_year method


'''




# IMP


''' When that def __init__ line executes, you have an empty object, named self, 
inside of the class. The make , model , and year parameters just hold whatever data you 
pass in, and you’ll see how that works in a moment.

An empty object with no data doesn’t do you much good. What makes an object 
useful is the information it contains that’s unique to that object (its attributes). 
So, in your class, the next step is to assign a value to each of the object’s attributes '''









" What is get_make() method ? "

# Its is a simple getter method , is a method that gets the value of an instance
# Variable in a class .

# Example 
''' class MyClass:
     def __init__(self, variable):
         self._variable = variable
        
     def get_variable(self):
         return self.  '''

# The MyClass class has a instance variable called _variable , 
# __init__ method initialize the instance variable , the get_variable
# method returns the value of instance variable

# The variable name indiactes that its a convention that the variable
# should not be accessed directly , but through the getter method 

 




# if u want to use get_model() method instead , you frist need to 
# define it inside the car class just like get_make():

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
car1 = Car("Toyota", "Corolla", 2020)
model = car1.get_model()

print(model) # Output: Corolla





# Example 2 

# Class movie: dont use uppercase title for class , if u do it there will be no  vaild class function


# Now we will cerate class of movies with year, theme , country with def and init

class movie:
    def __init__ (self , year , country, theme):
        self.year = year
        self.country = country
        self.theme = theme

    def get_year(self):
        return self.year

    def get_country(self):
        return self.country

    def get_theme(self):
        return self.theme

my_movies = movie("1999", "india", "horror")
print(my_movies.get_year())  # output 1999
print(my_movies.get_theme())  # output horror
print(my_movies.get_country()) # output india




# example 3 

class Worldmap :
    def __init__(self, india , mexico , south_africa , russia):
        
        self.india =  india
        self.mexico = mexico
        self.south_africa = south_africa
        self.russia = russia

    def get_india (self):
        return self.india

    def get_mexico(self):
        return self.mexico

    def get_south_africa(self):
        return self.south_africa

    def get_russia(self):
        return self.russia


# My_worldmap = Worldmap("Asia", "America", "asia", "Euroasia")
# print(Worldmap,self.get_india()) :   i have used   worldmap, self.get_india()

# print(self.india) and also tired self.india 

# which following syntax given error output eventullay

# The following error that occured by me is that i try to see the output in classmethod
# with diffrent approcah 



My_worldmap = Worldmap("ASIA" , "America" , "Africa" , "Euroasia")
print(My_worldmap.get_india())


    
# Example 3

''' class Student_name :
    def __init__ (self , ashish , rohit , arun):

        self.ashish = ashish
        self.rohit = rohit
        self.arun = arun

    def get_ashish ():
       return self.ashish

    def get_rohit():
        return self.rohit

    def get_arun():
        return self.arun


Standards = Student_name("ashish", "rohit" , "arun")
print (Standards.get_ashish()) '''

# this previous code is error cuz i have not added the self parameters 
# and also the variable name is incorrect 





# Correction of previous code
class Student_name:
    def __init__(self, ashish, rohit, arun):
        self.ashish = ashish
        self.rohit = rohit
        self.arun = arun

    def get_ashish(self):
        return self.ashish

    def get_rohit(self):
        return self.rohit

    def get_arun(self):
        return self.arun

Standards = Student_name("ashish", "rohit", "arun")
print (Standards.get_ashish())



# Example 4 

class Trade :
    def __init__ (self , forex , binary , Crypto):

        self.forex = forex
        self.binary = binary
        self.Crypto = Crypto
        # if write wrong attributes like self.Cryptoo and froget use =
        # asign there will be error too

    def get_forex(self):
        return self.forex

    def get_binary (self):
        return self.binary

    def get_Crypto(self):
        return  self.get_Crypto



passive_income = Trade("34.345" , "3444.4", "45623.23")
print(passive_income.get_binary())


# Example 5

class Pets :
    def __init__(self, dog , cat , brids):

        self.dog = dog
        self.cat = cat
        self.brids = brids

    def get_dog(self):
        return self.dog

    def get_cat(self):
        return self.cat
   
    def get_brids(self): # avoid spelling mistakes 
        return self.brids

pet_foods_products = Pets("pedigree" ,"catnip" , "vobriding" )
print(pet_foods_products.get_dog())
print(pet_foods_products.get_cat())
print(pet_foods_products.get_brids())







# Changing the value of an attribute #

# When working with tuples, you can define key:value pairs, much like the 
# attribute:value pairs you see here with instances of a class. There is one major 
# difference, though: Tuples are immutable, meaning that after they’re defined, you 
# code can’t change anything about them. This is not true with objects. After you 
# create an object, you can change the value of any attribute at any time






# Defining attributes with default values #



# You don’t have to pass in the value of every attribute for a new object. If you’re 
# always going to give those some default value at the moment the object is created, 
# can just use self.attributename = value, the same as before, in which 
# attributename is some name of your own choosing. The value can be some value 
# you just set, such as True or False for a Boolean, or today’s date, or anything that 
# can be calculated or determined by Python without your telling it the value.



# Lets make a class

class Member :

    def __init__(self, username , fullname):

        self.username = username
        self.fullname = fullname

    # The class ends at this un_indited line


# Create a instance of the Member class named new_client

new_client = Member("Rambo", "Ashwin_nair")


# See what instance with the print

print(new_client.username)
print(new_client.fullname)
print()

# Change the