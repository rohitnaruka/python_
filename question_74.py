#given the code below,insert the correct code on line 4 in order to concatenate my_string with the following string:
my_string1="In 2010, someone paid 10k Bitcoin for two pizzas."
my_string2="poor guy!"
new_string=my_string1+my_string2
print(new_string)


my_string="In 2010, someone paid 10k Bitcoin for two pizzas."
s="poor guy!"
for item in my_string:
    s += item
print(s)