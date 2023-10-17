#1.write a program and find out the avrage_value.

# my_list=[10,10,10]
# def find_avrage(my_list):
#     sum = 0
#     for i in my_list:
#         sum=i+sum
#         0=10+0=10=10+10=20=10+20=30
#         sum+=i
#         #0+=10,10+=10,20+=10,30
#         avrage =sum / len(my_list)
#     return avrage
# print(find_avrage(my_list))


#2 multiplie the numbers
# my_list = [1,2,8,5,8]
# def multiplie_num(my_list):
#     x = 1
#     for i in my_list:
#          x=i*x
#          #1=1*1,1=2*1,2=8*2,16=5*16,80=8*80,=640
#          #x*=i
#         #1*=1,1*=2,2*=8,16*=5,80*=8,=640
#     return x
# print(multiplie_num(my_list))

#3convert the two list in one dict.
# list1 = ["r","n","p","x"]
# list2 = [10,20,30,40]
# def lists_to_dict(keys,values):
#     result_dict={}
#     for i in range(len(keys)):
#         if len(keys) !=len(values):
#             result_dict[keys[i]]=values[i]
#     return result_dict
# print(lists_to_dict(keys=["r","n","p","x"],values=[10,20,30,40]))

#
# # 4 write a  Python program to print positive numbers in a list.
# my_list=[1,2,5,6,8,7,4,10,30,50]
# def find_positive_numbers(my_list):
#     positive_num =[]
#     for i in my_list:
#         if i > 0:
#             positive_num.append(i)
#     return positive_num
# print(find_positive_numbers(my_list))
#
# #5.write a  Python program to print negetive numbers in a list.
# my_list=[10,-2,34,3,-3,4,-5,6,8,-1]
# def negitive_numbers(my_list):
#     sum=0
#     negitive_numbers=[]
#     for i in my_list:
#         if i <0:
#             sum+=i
#             negitive_numbers.append(i)
#     return negitive_numbers,sum
# print(negitive_numbers(my_list))
# #
# # 6.write a python program to count all positive number ,\
# my_list = [1,-2,-3,3,4,-5,6,-5,-4,-6,5,9,4,9]
# def count_positive_num(my_list):
#     count = 0
#     positive_num=[]
#     for i in my_list:
#         if i>0:
#           count+=i
#           positive_num.append(i)
#     return positive_num,count
# print(count_positive_num(my_list))
#
# #7.write a python program find average value of a dictionary.
# names = {"ritu": 20, "ridhi": 30, "nidhi": 40}
# def average_value(my_list):
#     sum = 0
#     average=[]
#     for i in my_list:
#         sum+=i
#         average=sum/len(my_list)
#     return average
# print(average_value(my_list))
#
# #8.write a pyton program a find even number in a given dictionary and output show be in list.
# nums = {"x":1,"y":2,"z":3,"a":4,"b":5,"c":6}
# def find_even_numbers(nums):
#     even_numbers=[]
#     for i in nums.values():
#         if i % 2==0:
#             even_numbers.append(i)
#     return even_numbers
# print(find_even_numbers(nums))
#
# #9.write a pyton program a find odd number in a given dictionary and output will be show in a list.
# nums = {"x":1,"y":2,"z":3,"a":4,"b":5,"c":6}
# def find_odd_numbers(nums):
#     odd_numbers=[]
#     for i in nums.values():
#         if i % 2!=0:
#             odd_numbers.append(i)
#     return odd_numbers
# print(find_odd_numbers(nums))
#
#
# #10.wite a python program and find max number in a given dictionary.
# def find_max_in_dict(input_dict):
#     max_value=None
#     for value in input_dict.values():
#         if max_value is None or value > max_value:
#             max_value=value
#     return max_value
# my_dict = {'x':1,'y':2,'z':3,'a':4,'b':5,'c':6}
# result = find_max_in_dict(my_dict)
# print(result)
#
#
# #11.wite a python program and find min number in a given dictionary.
# def find_min_in_dict(input_dict):
#     min_value=None
#     for value in input_dict.values():
#         if min_value is None or value < min_value:
#             min_value=value
#     return min_value
# my_dict = {'x':1,'y':2,'z':3,'a':4,'b':5,'c':6}
# result = find_min_in_dict(my_dict)
# print(result)
#
#
# # 12.write a program and marge two python dictionary into one.
# dict1 = {"r": 12, 'k' : 13,"n": 10}
# dict2 = {"x": 1, "y": 2, "z": 3}
# def merge_two_dict(dict1,dict2):
#     merged_dict=dict1
#     for key,value in dict2.items():
#         merged_dict[key]=value
#     return merged_dict
# print(merge_two_dict(dict1,dict2))
#
# #13.write a python program and find sum_of_dictionary_values.v
# dict = {"r":1,"k":2,"n":3,"s":9,"g":6}
# def sum_of_dictionary(dict):
#     sum=0
#     for values in dict.values():
#         sum+=values
#     return sum
# print(sum_of_dictionary(dict))
#
# # 14.write a python program and find sum of key and value in pyhton dictionary
#

# #15. write a Python program and find the maximum value and its key in the dictionary and convert it into 
# #  list.(output will be show in list of dictionary)
dict = {
"ridhi":21,
"nidhi":12,
"raj": 19,
"dipti":51,
"swetae":13
 }
def find_maximum_value_key(dict):
    max_key = None
    max_value=None
    for key,value in dict.items():
        if max_value is None or value>max_value:
            max_key=key
            max_value=value
    return max_key,max_value
print(find_maximum_value_key(dict))


#
# #LIST-:
# # 1.print all positive numbers in a range:
# list=[5,7]
# def find_positive_numbers(list):
#     positive_numbers=[]
#     for i in range(5,7):
#         if i > 0:
#             # print(i)
#             positive_numbers.append(i)
#     return positive_numbers
# print(find_positive_numbers(list))
#
#
# #2.print all positive numbers in a range:
# def find_nagitive_numbers(start,end):
#     nagitive_numbers=[]
#     for i in range(start,end+1):
#         if i < 0:
#             # print(i)
#             nagitive_numbers.append(i)
#     return nagitive_numbers
# start_range=-17
# end_range=-98
# print(find_nagitive_numbers(start_range,end_range))
#
#
# #3.reverse all list.
list=[1,4,7,9,0,8,7,7,9]
def reverse_list(list):
    reversed_list = []
    for i in reversed(list):
        reversed_list.append(i)
    return reversed_list
print(reverse_list(list))
#
#
# # 4.find comman items from two list.
# list1=['white','black','red','green','yellow']
# list2=['sky','blue','white','red','dark']
# def find_comman_items(list1,list2):
#     comman_items = []
#     for item1 in list1:
#         for item2 in list2:
#             if item1 == item2:
#                 comman_items.append(item1)
#     return comman_items
# print(find_comman_items(list1,list2 ))
# None=the none is used to define a null variable or an object
#is =is used to test if two variables refer to the same object

# student = {
#     "ritu": {"age": 10, "address": "chandma"},
#     "sidhi": {"age": 20, "address": "jaipur"},
#     "ridhi": {"age": 13, "address": "ajmer"},
#     "hiyu":{"age":7, "address":"bikaner"}
# }
# def find_max_number(student):
#     max_number =
#     for value in student.items():
#             if max_number is
#                 max_number=value
#     return max_number
# print(find_max_number(student))


# student = {
#     "ritu": {"age": 10, "address": "chandma"},
#     "sidhi": {"age": 20, "address": "jaipur"},
#     "ridhi": {"age": 13, "address": "ajmer"},
#     "hiyu":{"age":7, "address":"bikaner"}
# }
# def find_max_number(student):
#     max_number = None
#     for i in student.keys():
#         if max_number is None or student[i]['age'] > max_number:
#             max_number = student[i]['age']
#     return max_number
# print(find_max_number(student))