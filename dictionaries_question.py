#question_86:-
# Given the code below, use the correct code on line 3 in order to return the value associated with key 4. Do not use a method as a solution for this exercise!
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
x = crypto[4]
print(x)


#question_87-:
# Given the code below, use the correct code on line 3 in order to return the value associated with key 4. This time, use a method as a solution for this exercise!
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
x = crypto.get(4)
print(x)


#question_88:-
# Given the code below, use the correct code on line 3 in order to update the value associated with key 4 to "Cardano".
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
crypto[4] = "cardano"
print(crypto[4])


#question_89:-
# Given the code below, use the correct code on line 3 in order to add a new key-value pair to the dictionary: 6: "Monero"
def add_to_dict(key,value,my_dict):
    my_dict[key]=value
    return my_dict
my_dict = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
new_key='monero'
new_value = 6
my_dict=add_to_dict(new_key,new_value,my_dict)
print(my_dict)



#question_90:-
# Given the code below, use the correct code on line 3 in order to return the number of key-value pairs in the dictionary.
def dict_length(my_dict):
    count=0
    for key in my_dict:
        count+=1
    return count
my_dict = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
print(len(my_dict))




#question_92:-
#
# Given the code below, use the correct code on line 3 in order to delete the key-value pair associated with key 3. This time, use a method as a solution for this exercise!
my_dict = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
keys_value_to_delete = ["litecoin",3]
for key in keys_value_to_delete:
    my_dict.pop(key,None)
print(my_dict)


#Question_91:-
# Given the code below, use the correct code on line 3 in order to delete the key-value pair associated with key 3. This time, use a method as a solution for this exercise!
my_dict={1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
keys_value_to_delete=["litecoin",3]
for key in keys_value_to_delete:
    if key in my_dict:
        del my_dict[key]
print(my_dict)


#question_93:-
# Given the code below, use the correct code on line 3 in order to verify that 7 is not a key in the dictionary.
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
def is_key_present(x):
    for i in crypto:
        if x in crypto:
            print('Key is present in the dictionary')
        else:
            print('Key is not present in the dictionary')
print(is_key_present(7))

#question_94-:# Given the code below, use the correct method on line 3 in order to delete all the elements in the dictionary.
my_dict =  {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
for key in list(my_dict.keys()):
    del my_dict[key]
print(my_dict)


#question_95:-
#given the code below, use the correct code on line 3 in order to get a list of tuples, where each tuple represents a key-value pair in the dictionary.
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
result = crypto.items()
print(result)


#question_96:-
 #Given the code below, use the correct function on line 3 in order to get the sum of all the keys in the dictionary.
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4:"vb   r", 5: "XRP"}
def sum_all_keys(crypto):
    sum = 0
    for i in crypto.keys():
        sum += i
    return sum
print(sum_all_keys(crypto))


#question_97:-
# Given the code below, use the correct method on line 3 in order to get a list of all the values in the dictionary.
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
list = []
for i in crypto.values():
   list.append(i)
print(list)



# question_98
# Given the code below, use the correct function on line 3 in order to get the smallest key in the dictionary.
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
def smallest_key_in_dictionary(crypto):
    min = 0
    for i in crypto.keys():
        if min <= 0:
            min = i
    return min
print(smallest_key_in_dictionary(crypto))

#question_99:-
#Given the code below, use the correct method on line 3 in order to get a list of all the keys in the dictionary.
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
list = []
for i in crypto.keys():
    list.append(i)
print(list)


#question_100:-
# Given the code below, use the correct method on line 3 in order to return and remove an arbitrary key-value pair from the dictionary.
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
crypto.popitem()
print(len(crypto))


#question_101:-
# Given the code below, use the correct function on line 3 in order to convert value to a string.
value  = 10
conv = str(value)
print(type(conv))


#question_102:-
# Given the code below, use the correct function on line 3 in order to convert value to an integer.
value="10"
conv = str(value)
print(type(conv))


#question_103:-
#Given the code below, use the correct function on line 3 in order to convert value to a floating-point number.
values = 20
conv = float(values)
print(type(conv))




