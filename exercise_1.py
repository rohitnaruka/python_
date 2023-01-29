# question_1
# Given the code below, insert the correct negative index on line 3 in order to get the last character in the string.

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
last_charcter = my_string[-1]
print(last_charcter)

 # qestion_2
# Given the code below, insert the correct positive index on line 3 in order to return the comma character from the string.

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
char = (my_string[7])
print(char)

#question_3
# # Given the code below, insert the correct negative index on line 3 in order to return the w character from the string.

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
char = (my_string[10])
print(char)

# question_4
 # Given the code below, insert the correct method on line 3 in order to return the index of the B character in the string.
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
char = (my_string.index('B'))
print(char)


# question_5
# Given the code below, insert the correct method on line 3 in order to return the number of occurrences of the letter o in the string.

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def count_character(my_string):
    count = 0
    for i in my_string:
        if i == 'o':
            count = count + 1
    return count
# print(count_character(my_string))

#question_6
# Given the code below, insert the correct method on line 3 in order to convert all letters in the string to uppercase.

def letter(s):
    x=s.upper()
    print(x)
wxy = input("enter string:")
letter(wxy)


# question_7
# Given the code below, insert the correct method on line 3 in order to get the index at which the substring Bitcoin starts.

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.index("Bitcoin"))

#question_8
# Given the code below, insert the correct method on line 3 in order to check of the string starts with the letter X

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def check_elements(my_string):
    check = 'X'
    res = " "
    for i in my_string:
        if  "X" in i:
            print('true')
        else:
            print("False")
            res.join(i)
    return res
print(check_elements(my_string))

#question_9
# Given the code below, insert the correct method on line 3 in orderto convert all uppercase letters to lowercase and all lowercase letters to uppercase.

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def upper_to_lower_and_lower_to_uper(my_string):
    string = my_string.swapcase()
    return string
print(my_string.swapcase())

# question_10
# Given the code below, insert the correct method on line 3 in order to remove all spaces (single Space characters from the keyboard) from the string.
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def remove_spaces(my_string):
    string = my_string.replace(" ","")
    return string
print(remove_spaces(my_string))