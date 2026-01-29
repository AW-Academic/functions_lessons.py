
# Indefinite Arguments (**kwargs) Practice #1
# Create a function called number_attributes that counts the number of parameters that are passed, and returns that number as the result.

def number_attributes(*args):
    #params_passed = 0
    #for value in args:
    #    params_passed += 1
    params_passed = len(args)
    return params_passed

# Spamming my keyboard to pass many parameters as a test.
print("Number of parameters passed:")
print(number_attributes(6, 8, 23, 234, 23,42,423,423,42,4,123431,32,32,231,14,1234,1234,4,234,2342,4234,234,1234,234,143,0))


# Indefinite Arguments (**kwargs) Practice #2
# Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords. The function must expect to receive any number of arguments of this type.

def list_attributes(**kwargs):
    empty_list = []








# Indefinite Arguments (**kwargs) Practice #3
# Create a function called describe_person, which takes his name as parameters and then an indeterminate number of arguments. This function should display on the screen:

# Characteristics of {name}:
# {argument_name}: {argument_value}
# {argument_name}: {argument_value}
# etc...
# For example:

# describe_person("Ash", eye_color="brown", hair_color="black")

# Will print to the screen:

# Characteristics of Ash:
# eye_color: brown
# hair_color: black