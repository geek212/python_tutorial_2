''' 
return statement = This function send python values/objects back to the caller,
These values/objects are known functions return values

'''

# Lets write a function :

def multiply(numb1,numb2):
    result = numb1 * numb2
    return result

x = multiply(67, 8)
print(x)



# Now with less line of code without variables like result used previously now we use return statement :

def multiply(numb1,numb2):
    return numb1 * numb2

x = multiply(6,7)
print(x)


# In this example, the get_name_and_age function returns two values, 
# name and age, as a tuple.

def get_name_and_age():
    name = "Alice"
    age = 30
    return name, age
 
result = get_name_and_age()

print(result)

# we are using the result variable (renamed to name and age) to store the return 
# value of the get_name_and_age() function, and then we are using those values in 
# the print statement. This allows us to use the values returned by the function 
# elsewhere in our code
 



# In Python, the return statement is used to exit a function and return a value to the caller. 
# When a return statement is encountered in a function, the function execution is stopped, and the specified
#  value is returned to the caller.

# A function can have zero or more return statements. If a return statement is not used, the function will 
# still execute but will not return any value. In this case, the function will return a special value called 
# None.