# question_11
# Given the code below, insert the correct method on line 3 in order to replace all the occurrences of letter i with the substring btc.

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def replace_character(my_string):
   string = my_string.replace("i", "btc")
   return string
print(replace_character(my_string))



# question_12
# Given the code below, insert the correct method on line 3 in order to split the entire string in two parts, using the comma as a delimiter.

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def split_string(my_string):
    string = my_string.split(",")
    return string
print(split_string(my_string))


#question_13
#given the code below,insert the correct methood on line 3 in order to join the characters of the string using the & symbol as a delimiter.

my_string="In 2010, someone paid 10k Bitcoin for two pizzas."
s = "&"
s= s.join(my_string)
print(s)

# question_14
# Given the code below, insert the correct code on line 4 in order to concatenate my_string with the following string:
# my_other_string = "Poor guy!"

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
my_other_string = "Poor guy!"
string = my_string + my_other_string
print(string)


 # question_15
#Given the code below, insert the correct method on line 3 in order to convert the first letter of each word in the string to uppercase.

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def first_letter_uppercase(my_string):
    string = my_string.title()
    return string
print(first_letter_uppercase(my_string))




#question_17
#given the code below,use string formatting with the format() method on line 3 to map the  corresponding formatting operators
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
char=my_string[3:7]
print(char)


#question_18
#Given the code below, use slicing and insert the correct code on line 3 in order to return the substring 2010 from the string. Use positive indexes!

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def slcing(my_string):
    string =  my_string[3:7]
    return string
print(slcing(my_string))




#question_19

#Given the code below, use slicing and insert the correct code on line 3 in order to return the substring Bitcoin from the string. Use negative indexes!my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def slicing(my_string):
    string = my_string[-23:-16]
    return string
print(slicing(my_string))

# # question_20
# # Given the code below, use slicing and insert the correct code on line 3 in order to return the first 12 characters in the string. Use a single, positive index!
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def slicing(my_string):
    string = my_string[:12]
    return string
print(slicing(my_string))


# # question_21
# # Given the code below, use slicing and insert the correct code on line 3 in order to return the last 9 characters of the string. Use a single, negative index!
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def slicing(my_string):
    string = my_string[-9:]
    return string
print(slicing(my_string))


#question_22
#Given the code below, use slicing and insert the correct code on line 3 in order to return the entire string in reversed order.

def reverse(my_string):
    reversed = ""
    count = len(my_string)
    while count > 0:
        reversed += my_string[count - 1]
        count = count - 1
    return reversed
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(reverse(my_string))


# # question_23
#given the code below, use slicing and insert the correct code on line 3 in order to return every 7th character of the string ,starting with the first character.
my_string = 'In 2010, some paid 10k Bitcoin for two pizzas.'
def slicing(my_string):
    string = my_string[::7]
    return string
print(slicing(my_string))


#question_24
#Given the code below, use slicing and insert the correct code on line 3 in order to return the string except the first 10 characters. Use a single, positive index!
my_string = 'In 2010, some paid 10k Bitcoin for two pizzas.'
def slicing(my_string):
    string = my_string[10:]
    return string
print(slicing(my_string))




# # question_25
# # Given the code below, use slicing and insert the correct code on line 3 in order to return the string except the last 4 characters. Use a single, negative index!
#
my_string = 'In 2010, some paid 10k Bitcoin for two pizzas.'
def slicing(my_string):
    string = my_string[:-4]
    return string
print(slicing(my_string))







