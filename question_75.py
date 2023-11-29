#given the code below,insert the correct methood on line 3 in order to convert the first letter of each word in the string to uppercase.

my_string="In 2010, someone paid 10k Bitcoin for two pizzas."
strlist = my_string.split()
new_string = ""
for val in strlist:
    new_string +=val.capitalize()+' '
print(new_string)
