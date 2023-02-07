# Define a function
def whoismostimportant(str):
    "This prints the most important person in your life"
    print(str)
    return;

# Call the whoismostimportant function
whoismostimportant("I first thought it is my highschool sweetheart")
whoismostimportant("Then I thought about it again, it is me")
whoismostimportant("Goodbey, sweetheart")

# Example of the reference inside the function is overwritten
# Define 
def change(mylist):
    "This changes a passed list into this function"
    mylist.append([1, 2, 3, 4]);
    print ('Values inside my funtions: ', mylist)
    return;

# Call
mylist = [1, 2, 3, 4, 10, 20, 30];
change(mylist);
print("Values after the function call: ", mylist)

# Example of keyword argument
# Define the function
def user_input(name, age, cardnumber):
    "This prints a passed info from customer"
    print ("Name: ", name)
    print("Age ", age)
    print("cardnumber: ", cardnumber)
    return;

# Call
user_input('janebunny', 18, 123456789)

# Example of default arguments
# Define the function
def whoisthemostimportant(Relationship = 'mum'):
    "This prints out who is the most important"
    print("Relationship: ", Relationship)
    return;

#Call
whoisthemostimportant() # Notice when no argument put in the call function, default value will be given

# Example of variable-length argements
# Define the function
def user_info(a1, *infot):
    "This prints out an input passed arguments"
    print("Output is: ", a1)
    for info in infot:
        print(info)
    return;

# Call
user_info('hello')
user_info(10)
user_info([1, 2, 3])
user_info({1, 2, 3})
user_info("hhh") # Notice that the argument is defined only as a (any name) tuple of infot

# Example of Lambda function
# Define the function
total1 = lambda a1, a2: a1 * a2;

# Call the function
print ('Value of total: ', total1(4, 5))

# Function definition is here
def sum( arg1, arg2 ):
   "Add both the parameters and return them."
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total;
# Call the function
print(sum(4, 5)) # Outside the function

# Example of global vs. local variables

total = 0; # Global variable
# Define the function
def sum( arg1, arg2 ):
   "Add both the parameters and return them."
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total;

# Call the function
sum(4, 5)
print(total) # Outside the function, the global variable is been accessed