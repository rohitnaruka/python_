#question_171:-
#Implement a function called my_func() that simply prints out Hello Python! to the screen and call the function.

def my_func():
    print('hello rohit')
my_func()


#question_172:-
#Implement a function called my_func() that creates a variable add which stores the result of adding 10 and 20, and prints out the value of add. Don't forget to also call the function
def my_func():
    add =10+20
    print(add)
my_func()


#question_173:-
#Implement a function called my_func() that takes a single parameter x and multiplies it with 10, also returning the result when the function is called.
def my_func(x):
    return x * 10
result = my_func(7)
print(result)


#question_174:-
#Implement a function called my_func() that takes two parameters x and y and divides x by y, also returning the result when the function is called.
def my_func(x, y):
    return x / y
result = my_func(38, 19)
print(result)

#question_175:-
#Implement a function called my_func() that takes 3 parameters x, y and z and raises x to the power of y then adds z, also returning the result when the function is called.
def my_func(x, y, z):
    return x ** y + z
result = my_func(3, 3, 3)
print(result)


#question_176:-
#Implement a function called my_func() that takes a single parameter x and multiplies it with each element of range(5), also adding each multiplication result to a new (initially empty) list called my_new_list. Finally, the list should be printed out to the screen after the function is called.
def my_func(x):
     my_new_list = []
     for i in range(5):
      return my_new_list
result = my_func(2)
print(result)

#question_177:-
#Implement a function called my_func() that takes a single parameter x (a string) and turns each character of the string to uppercase, also returning the result when the function is called.
def my_func(x):
    return x.upper()
result = my_func("Satoshi Nakamoto")
print(result)


#question_178:-
#Implement a function called my_func() that takes a single parameter x (a list) and eliminates all duplicates from the list, also returning the result when the function is called.
def my_func(x):
    return list(set(x))
result = my_func([11, 12, 13, 11, 15, 18, 18, 22, 20, 16, 12])
print(result)


# question_179:-
# Implement a function called my_func() that takes a single parameter x (a tuple) and for each element of the tuple that is greater than 4 it raises that element to the power of 2, also adding it to a new (initially empty) list called my_new_list. Finally, the code returns the result when the function is called.
def my_func(x):
    my_new_list = []
    for i in x:
        if i > 4:
            my_new_list.append(i ** 2)
    return my_new_list
result = my_func((2, 3, 5, 6, 4, 8, 9))
print(result)


# question_180:-
# Implement a function called my_func() that takes a single parameter x (a dictionary) and multiplies the number of elements in the dictionary with the largest key in the dictionary, also returning the result when the function is called.
def my_func(x):
    return len(x) * sorted(x.keys())[-1]
result = my_func({1: 3, 2: 3, 4: 5, 5: 9, 6: 8, 3: 7, 7: 0})
print(result)


# question_181:-
# Implement a function called my_func() that takes a single positional parameter x and a default parameter y which is equal to 10 and multiplies the two, also returning the result when the function is called.
def my_func(x, y=10):
    return x * y
result = my_func(5)
print(result)


#question_182:-
# Implement a function called my_func() that takes a single positional parameter x and two default parameters y and z which are equal to 100 and 200 respectively, and adds them together, also returning the result when the function is called.
def my_func(x, y=100, z=200):
    return x + y + z
result = my_func(50)
print(result)

#question_183:-
# Implement a function called my_func() that takes two default parameters x (a list) and y (an integer), and returns the element in x positioned at index y, also printing the result to the screen when called.
def my_func(x, y):
    return x[y]
result = my_func(list(range(2, 25, 2)), 4)
print(result)

# question_184:-
# Implement a function called my_func() that takes a positional parameter x and a variable-length tuple of parameters and returns the result of multiplying x with the second element in the tuple, also returning the result when the function is called.
def my_func(x, *args):
    return x * args[1]
result = my_func(5, 10, 20, 30, 50)
print(result)

# question_185:-
# plement a function called my_func() that takes a positional parameter x and a variable-length dictionary of (keyword) parameters and returns the result of multiplying x with the largest value in the dictionary, also returning the result when the function is called.
def my_func(x, **kwargs):
    return x * sorted(kwargs.values())[-1]
result = my_func(10, val1=10, val2=15, val3=20, val4=25, val5=30)
print(result)

# question_186:-
# Add the correct line(s) of code inside the function in order to get 200 as a result of calling my_func() and have the result printed out to the screen.
var = 10
def my_func(x):
    print(x * var)
my_func(20)

# question_187:-
# Add the correct line(s) of code inside the function in order to get 100 as a result of calling my_func() and have the result printed out to the screen.
var = 10
def my_func(x):
    var = 5
    print(x * var)
my_func(20)

# question_188:-
# Make the necessary adjustment inside the function in order to get 120 as a result of calling my_func() and have the result printed out to the screen.
def my_func(x):
    var = 12
    print(x * var)
my_func(10)

# question_189:-
# Add the necessary line of code inside the function in order to get 80 as a result of calling my_func() and have the result printed out to the screen.
var = 8
def my_func(x):
    global var
    print(x * var)
    var = 12
my_func(10)

# question_190:-
# Write code that will import only the pi variable from the math module and then it will format it in order to have only 4 digits after the floating point. Of course, print out the result to the screen using the print() function.from math import pi
# print("%.4f" % pi)
