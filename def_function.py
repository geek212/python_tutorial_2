"""
When a program is getting bigger with every new line of code were you have to repeat code
again and again , offcourse it will get complex for a programmer . how can we fix this issue !



What will be the solution ?

def(short for definition) is a builtin function in python

To access the task that the function performs, you just call the function from your 
code. You do this in exactly the same way you call a built-in function like print: 
You just type the name into your code. You can make up your own function names 
too. So, think of functions as a way to personalize the Python language so its commands
fit what you need in your application




Syntax of def() : 

def function_name ( ) :  

    # Example
    def hello ():


When you define a function using def, you create a reusable block of code that performs a specific task. 
This allows you to write code that is more modular and easier to understand, since you can break down 
complex tasks into smaller, more manageable pieces.


"""


# lets write length code lines
a = 9
b = 43
c = 56
print(a - b)
print(b - a)
print(c + b)
print(c - a)
print(c % b)
print(a + b + c)
print(a / b + c)
print(b + c + a * 2 % 34 + a)


# lets take one more example
print("Happy brithday joe")
print("Happy brithday harry")
print("Happy brithday ken")
print("Happy brithday mike")
print("Happy brithday luke")
print("Happy brithday tyson")
print("Happy brithday mATT")
print("Happy brithday JERRY")
print("Happy brithday 619")
print("Happy brithday brock lesnar")
print("Happy brithday triple h")
print("Happy brithday the rock")
print("Happy brithday jhon cena")
print("Happy brithday mike tyson")
print("Happy brithday eddie")
print("Happy brithday edge")
print("Happy brithday stone cold steve austin")
#  u have to write this shit multiple times

"""When a program gets bigger in size its complexcity grows eventually , meanwhile
to keep track every line of code gets diffcult for a programmer / dev while working in IMP projects """


# i have to write code multiple times and it will get complex beyond this which i have written
# at sometime it will get confuseing


"So def function Saves time for you with a twist its just like print which u can revoke any line of code"
"This function is reusable any number of times ........"


#  create a function

# def hello () : #
# This is a function However,it doesn’t do anything to make the function do
# something, you have to write the Python code that tells it what to do on subsequent lines.
# To ensure that the new code is “inside” the function, indent each of
# those lines.


# Like this :


# Eg : 1
def hello():
    print("Hello")


hello()  # output "Hello"


# Eg 2
def Hi():
    print("ola")


Hi()  # output "ola"


# Eg 3
def user():
    print("Cart")


user()  # output "Cart"


# Eg 4
def username():
    print("Ashwin")


username()  # output "Ashwin"


# There is no output of this code without good_evening() argument
def good_evening():
    print("ashwin")


# output none , be careful while writeing


def HeLLoO():  # i used uppercase and lower case to see how it reacts ,
    print("How are you")


HeLLoO()  # output was same "How are you"


def yu():
    print(567)


yu()  # output is 567


# def 345678():
#     print(kl)
# 345678()

# output def 345678():
#         ^^^^^^
# SyntaxError: invalid syntax


# def function call

""" This (def function) can be called any number of times anywhere of program """
# Whenever we reliaze that we have to use function  , we call function with
# the name of the function following parenthesis .

# function_name (): this called function call


# Lets create a greetings with function


# function name greetings
def greetings(name):  # name is a temp variable with function
    print("Greetings " + name)


greetings("Ashwin")


# function_name hello
def hello(name):
    print("Hello , how are you " + name)


hello("Harry")
hello("Jerry")
hello("ken")
hello("jacky")

hello("78ihidfgui")  # u can add any "String statement"


# function_name interview
def interview(name):
    print("Theirs urgent schduled interview with " + name)


interview("peter parker")


# function_name ok
def ok(meeting):
    print("ok i will be their at sharp 6:00 AM" + meeting)


ok("  at lonvala")


# function named airport
def airport(airline):
    print("Your flight have arrived in mumbai airport" + airline)


airport(" rahul")
airport(" jacky")


# function name spacestation
def spacestation(ISS):
    print("Hello earth we can see our planet from space and its beautiful" + ISS)


spacestation(" : Astranout mark over")


"Its fun to write def function in python , its simple yet saves time best of world"


# Error is vital in def function remember that dont over do it
# function named id
# def id (number): avoid this type of code
# print(input("enter your number"))
# print("your id number ")

# id()  ERROR


"""     Avoiding Argument Errors:

When you start to use functions, don’t be surprised if you encounter errors 
about unmatched arguments. Unmatched arguments occur when you 
provide fewer or more arguments than a function needs to do its work. 

"""


# Function is a reuseable code lets write some multiple code with def functions , which make some sense in
# my way (- _ -) :


# Eg : 1
def happy_brithday():  # with no parameters in () which we used in previous code with hello(name)
    print("Happy brithday ,\nHappy brithday")
    print("Happy brithday to you \nAshwin")
    print("Your getting old as f**k ")
    print("Deal with it you pig")


happy_brithday()


# Eg : 2
def uip():  # u can put any Function_name with def
    print("welcome to mumbai !")


uip()


# Eg : 3
# Now with some parameters with multiple line codes
def meeting(manager):
    print("Their is a meeting")
    print("To attend today asap")
    # i have used f string with {place holder named manager}
    print(f"plz call {manager}")


meeting("Harry")  # u have arrgument "Harry","Ashwin", "jacob" to invoke

# meeting("Ashwin"40) u will find error cuz we have 2 arrguments here

meeting("jacob")


# Now you see i have two parameters name,surname
def best_of_luck(name, surname):  # positions of parameters matters
    print("Congrats for your achivement in tata")
    print("We have high hopes for you")
    print(f"once again congrats \n{name} {surname}")


best_of_luck("Rahul", "Nair")


# Eg : 4
def best_of_luck(surname, name):  # positions of parameters matters
    print("Congrats for your achivement in tata")
    print("We have high hopes for you")
    print(f"once again congrats {surname} {name}")


best_of_luck("nair", "rahul")


# Lets write some def function  for a users
def display_invoice(username, amount, due_date):
    print(f"Greetings Mr {username}")
    print(f"Their is pending bal of ${amount} is due {due_date}")


display_invoice("Harry", 45, "2/2/23")


# Eg : 5
def bank_bal(username, amount, date):
    print(f"Hello mr {username} \nthis mail is from valley bank ")
    print(
        f"This is a E-report of your bank a/c,\nAmount is withdrawn ${amount} from your debit card"
    )
    print(f"on {date} ")


bank_bal("Yash Naik", 78600, "2/3/23")

# f strings imp:
# fstrings are a convenient way to create formatted strings in Python, and they are particularly useful
# when you need to include the values of variables in a string. You can use f-strings to create complex
# messages that include calculations, conditions, and even function calls


# Default parameters


# Eg : 1
def hello(name=" BOB "):
    print("HEllo" + name)


hello()  # have not provided any value


# Eg : 2
def joke(name="Nil"):
    print("Welcome home brother  " + name)


joke()


# Eg : 3
def money(trade="put"):
    print("BSENIFTY_50")


money()


# Eg : 4
def navigation(google="linkin_park"):
    print("Thane west")


navigation()


""" When a function is defined, you can specify default values for its parameters, which will be used if 
the caller does not provide a value for that parameter. This can be useful for creating functions with 
flexible behavior, as it allows you to provide a default behavior that will be used if the caller does 
not specify anything different. """


# Eg : 1
def HI(YO=" nemo "):
    print("Where are you" + YO)


HI()


# Eg : 2
def station(bhandup="east"):
    print("Town of mumbai" + " " + bhandup)


station()


# Eg : 3
def live(located="punjab"):
    print("north west part of india is" + "  " + located)


live()


""" Return in def function """

# The return statement is used inside a function to send the function's result back to the caller.
# When a return statement is executed, the function terminates immediately and the value specified in the
# return statement is passed back to the caller. If no value is specified in the `return` statement or if
# there is no return statement at all, the function returns None.

# Here's an examples:


# Eg : 1
def add(a, b):
    result = a + b
    return result


sum = add(3, 4)
print(sum)  # 7 output


# Eg : 2
def sub(c, d, y):
    result = (
        c - d
    )  # i have not added y with any following operators so the output still remains -2
    return result


sum = sub(4, 6, 3)
print(sum)  # -2 output


#  Eg : 3
def multiple(v, d, s, f, g):
    result = v - d + s * f - g
    return result


sum = multiple(34, 342, 78.3, 100, 34.3)
print(sum)  # 7487.7 output


# Eg : 4
# def  (gj,qw,rt):
#     result = gj + qw + rt * 5
#     return result
# sum = sub(4, 56, 78)

# print(sum) error output cuz i have not given any function


# The add , sub , multiple function takes two or more  arguments  adds them together and returns the
# result using the "return" statement. The returned value is then assigned to the variable sum and printed.


#  Returning a Simple Value


# intro code
def formatted_name(frist_name, middle_name, last_name):
    full_name = f"{frist_name} {middle_name} {last_name} "
    return full_name.title()  # we have used title method to captilze the frist letter


student_named = formatted_name("Ashwin", "Sudhakar", "Nair")
print(student_named)
# output Ashwin Sudhakar Nair


# Example 1


def bse_stocks(company_name, price, mid_cap):
    stocks = f"{company_name} {price} {mid_cap}"
    return stocks.title()


valueable_stocks = bse_stocks("Tata ", 45.3, "3456_cr")
valueable_stocks = bse_stocks("Mahaindra", 567.3, "100_cr")
valueable_stocks = bse_stocks("Maruti_suzuki", 2345.3, "54000_cr")

# only "Maruti_suzuki", 2345.3, "54000_cr" output as shown why ?
print(valueable_stocks)

# In the given code, the valueable_stocks variable is being overwritten each time the bse_stocks function
# is called, rather than appending each new stock listing to the previous ones. This means that only the
# last stock listing, "Maruti_suzuki", 2345.3, "54000_cr", is stored in the variable and printed.

# To fix this, you can modify the code to use the += operator to append each new stock listing to the existing
# value of valueable_stocks, instead of overwriting it with each new call to bse_stocks.


# Example 2


# This code defines a function called bse_stocks that takes three arguments: company_name, price,
# and market_cap. The function concatenates these three arguments into a string using an f-string, and
# then calls the title() method on the resulting string to convert it to title case. The function returns
# this title-cased string as its output.


def bse_stocks(company_name, price, market_cap):
    """following function are companys stocks that are listed in bse"""
    stocks = f"{company_name} {price} {market_cap}"
    return stocks.title()  # dont put bse_stocks.title()


valueable_stocks = bse_stocks("Tata", 45.3, "3456_cr")
valueable_stocks += "\n" + bse_stocks("Mahindra", 567.3, "100_cr")
valueable_stocks += "\n" + bse_stocks("Maruti Suzuki", 2345.3, "54000_cr")

print(valueable_stocks)


# Note that the += operator is used instead of simple assignment (=) when appending each stock listing
# to the valueable_stocks variable. This is because += modifies the existing valueable_stocks string by
# appending the new listing to the end, while = would overwrite the variable with the new listing each time
# it's called.


# In Python, the = operator is used to assign a value to a variable. For example, x = 1 assigns the
# value 1 to the variable x. If x already had a value, it would be overwritten with the new value.


# The += operator is a shorthand for concatenating a string or list to an existing variable.
# For example, x += "world" is the same as x = x + "world". This modifies the existing value of x by appending
# the string "world" to the end, rather than overwriting it completely.


"""
In the code example given, valueable_stocks is initially assigned the value of the first stock listing
returned by the bse_stocks function. However, the code needs to concatenate multiple stock listings into 
a single string, rather than overwriting the variable with each new listing.

Therefore, the += operator is used to append the new stock listings to the existing value of valueable_stocks
instead of overwriting it. This allows the code to build up the full list of stock listings as a single 
string, with each new listing appended to the end of the previous listings, separated by newline characters.

"""


# The Argument optional of def function

# In Python, you can specify default values for function arguments, making them optional.
# This means that when you call the function, you can either pass in a value for the argument or omit it.
# If you omit it, the default value will be used instead


# Eg : 1
def greet(name, greetings="Hello"):
    """docs string describe the function"""  # use it
    print(f"{greetings} , {name}")


greet("Alice")


# Defining optional parameters with defaults

#  You can write a function so that passing in a parameter is optional,
# but you have to tell it what to use if nothing gets passed in. The syntax for that is:
# def functioname(paremetername = defaultvalue):
# The only thing that’s really different is the = defaultvalue part after the parameter name.


# Eg : 2
def introduction(name, greet="welcome to uio tech"):
    """docs string describe the function"""  # use it
    print(f"{greet} , {name}")


introduction("kunal")


""" Commenting a Function :

Comments are always optional in code. But it’s somewhat customary to make the 
first line under the def statement a docstring (text enclosed in triple quotation 
marks) that describes what the function does. It’s also fairly common to put a 
comment, preceded by a # sign, to the right of the parentheses in the first line. """


# Eg : 3
# just random function which came in my mind ignore it
def username(name, login_id="34567"):
    print(f"{name}  {login_id}")


username("Ashwin log id")


# Passing multiple values to a function

# Just provide a parameter name for each value,
# and separate the names with commas .


# Example 1
def function(fullname, surname):
    print(f"{fullname}  {surname}")


function("Ashwin", "nair")


# Example 2
def function1(Fruit, Vegetables):
    print(Fruit + " " + Vegetables)


function1("Manngo", "Brinjal")  # always use string with argument


# Example 3
def function2(fullname, std, division, school):
    print(f"{fullname}  \n{std} \n{division} \n{school}")


function2("Ashwin", "XII", "A", "DONBOSCO")


# Example 4
def function3(bank, location, city, area, country):
    print(bank + " " + location + " " + city + " " + area + " " + country)


function3("Kotak", "DADR", "MUMBAI", "SION", "INDIA")


# Example 5
def hello (fname,lname,date):

    msg = "Hello" + "  " + fname + " " + lname 
    msg += "\nAs u mentioned\n" +   date
    print(msg)

hello("Ashwin", "nair", "4/5/61")
hello("Sabin", "Nqa", "5/6/76")


# Example 6

def change_me(v):
      print ("function got:", v)
v = 10
print ("argument is now:", v)
myvar = 5
print ("starting with:", myvar)
change_me(myvar)
print ("ending with:", myvar)
 



# Example 7
def user():
    username = input("Enter your name\n")
    userid = input("Enter your userid \n")
 
     

user()
 
# Now useing def function with lists 
def lst1():
    a = [1,3,45,6,7,8]
    b = [3.5,7,8,943]
    a.reverse()
    b.index(8)
    print(a,b)
lst1()

# Now with dir
def dir1():
    a = {
        "Apple":34,
        "Mango":43,
        "violet":21
    }

    b = {"Brinjal":56,"Cabbage":32,"okra":90}

    print(a,b)

dir1()





# Default Values in def function
 

 
# When writing a function, you can define a default value for each parameter. 
# If an argument for a parameter is provided in the function call, Python uses 
# the argument value. If not, it uses the parameter’s default value. So when 
# you define a default value for a parameter, you can exclude the corresponding 
# argument you’d usually write in the function call. Using default values 
# can simplify your function calls and clarify the ways in which your functions 
# are typically used.




# Example 1
def describe_pet(pet_name, animal_type='dog'):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')

# Example 2
def Movies_you_luv(moviename='bhahubali',Theater='Mumbai'):
    print(f"I have going to watch\n{moviename}")
    print(f"Movie was in {Theater}")

Movies_you_luv()



#  Avoiding Argument Errors:

# When you start to use functions, don’t be surprised if you encounter errors 
# about unmatched arguments. Unmatched arguments occur when you 
# provide fewer or more arguments than a function needs to do its work.


# Example 1
# def describe_pet(animal_type, pet_name):
#  """Display information about a pet."""
#  print(f"\nI have a {animal_type}.")
#  print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet()
# # Error output shown n this program

# Python recognizes that some information is missing from the function 
# call, and the traceback tells us


 
