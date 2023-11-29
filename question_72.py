#given the code below,insert the correct methood on line 3 in order to split the entire string in two parts ,using the comma as a delimiter
import re
def split_and_join(string):
    split_string = re.split(r'[^a-zA-Z]',string)
    joined_string = ''
    for i split_and_join() in enumerate(split_and_join()):
        if i > 0:
            joined_string += '_'
        joined_string+=split_and_join()
    return split_string,joined_string
string="In 2010, someone paid 10k Bitcoin for two pizzas."
split_string,joined_string =split_and_join(string)
print(split_string)
print(joined_string)