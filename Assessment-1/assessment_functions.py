# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def total_item_cost(state, cost_amount, tax = 1.05):
    """
    This function takes in the tax, state abbreviation, and cost in order to calculate
    the total cost of an item, including the tax. 

    """

    if state == "CA" or "California":
       tax = 1.07

    total_cost = cost_amount * tax

    return total_cost

print total_item_cost("VA", 12,)

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

#------------------------------------ 1a --------------------------------------#

def is_berry(fruit_name):
    """
    function takes a fruit name as a string and returns a boolean if the fruit 
    is a "strawberry", "cherry", "blackberry"

    """

    return fruit_name in ("strawberry", "cherry", "blackberry")


print is_berry("apple")

#------------------------------------ 1b --------------------------------------#

def shipping_cost(fruit_name):
    """
    this function takes a fruit name as a string and utilizing the is_berry 
    function will return the shipping cost of the fruit

    """

    if is_berry(fruit_name):
        return 0
    else: 
        return 5

print shipping_cost("apple")

#------------------------------------- 2 -------------------------------------#

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

#----------------------------------- 2a --------------------------------------#

def is_hometown(town_name):
    """
    Takes a town name as a string and evaluates to 'True' if it is my hometown, 
    else 'False'.

    """
    hometown = "Charlottesville"
    return town_name == hometown

print is_hometown("Richmond")

#------------------------------------ 2b --------------------------------------#

def full_name(first_name, last_name):
    """
    Takes a first and last name as strings and returns the concatenation of the 
    two names in one string.

    """
    formal_name = first_name + " " + last_name
    return formal_name

print full_name("Cephra", "Stuart")

#------------------------------------- 2c -------------------------------------#

def hometown_greeting(hometown, first_name, last_name):
    """
    Takes a hometown, a first name, and a last name as strings, calls two
    functions is_hometown() and full_name() and prints "Hi, 'full name', we're
    from the same place!" or "Hi 'full name', where are you from? Depending on 
    the evaluation of is_hometown().

    """
    if is_hometown(hometown) == True:
        print "Hi " + full_name(first_name, last_name) + " we're from the same place!"
    else:
        print "Hi " + full_name(first_name, last_name) + " where are you from?"

hometown_greeting("Charlottesville", "Cephra", "Stuart")
hometown_greeting("Richmond", "Cephra", "Stuart")
#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#----------------------------------- 3a --------------------------------------#

def increment(x = 1):
    """
    This function takes an integer (or defaults to 1) and increments it by y, using an inner
    function, add().

    """
    def add(y):
        total = x + y
        return total
    return add(y)
    



#----------------------------------- 3b --------------------------------------#
y = 0
addfive = increment(5)
print addfive
y = 5
addfive = increment(5)
print addfive
y = 20
addfive = increment(5)
print addfive

#----------------------------------- 3c --------------------------------------#

def add_new_number(new_num, num_list):
    """
    This function takes in a number(new_num) and a list of numbers(num_list) and
    then adds new_num to num_list. 

    """ 
    num_list.append(new_num)
    return num_list

print add_new_number(8, [1, 2, 3, 4, 5])


#####################################################################