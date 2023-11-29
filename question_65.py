#Given the code below, insert the correct method on line 3 in order to return the number of occurrences of the letter o in the string
my_string ="In 2010, someone paid 10k Bitcoin for two pizzas."
def count_char(my_string):
    count=0
    for i in my_string:
        if i =='o':
            count=count+1
    return count
print(count_char(my_string))