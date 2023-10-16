# def swaplist(newlist):
#     size = len(newlist)
#     temp = newlist[0]
#     newlist[0] = newlist[size - 1]
#     newlist[size - 1] = temp
#     return newlist
# newlist =[12,35,9,56,24]
# print(swaplist(newlist))
#
# list = []
# num =int(input("how many elements in list?:"))
# for x in range(num):
#     numbers = int(input('enter numbers'))
#     list.append(numbers)
# print("\nmaximum element in the list is :",max(list))
# print("minimum element in the list is:",min(list))
#
# list = [1,'ABC',2,3,'abc','XYZ',4]
# print("The first half of the list",list[:3])
# print("The second half of the list",list[3:])
#
# list1 = [1,'ABC',2,3,'abc','XYZ',4]
# length_to_split = [len(list1)//2]*2
# print(length_to_split)
# iterable_lst = iter(list1)
# res_list = [list((iterable_lst,elem)) for elem in length_to_split]
# print("initial list:",list1)
# print("List halves after splitting",res_list)
#
# list =['' ,'27','37','','45','24']
# print('original list:',str(list))
# while("" in list):
#     list.remove("")
#     print("list after removing empty strings:",str(list))
#
# list = ["",'ROHIT','SINGH','','NARUKA','RAJPUT']
# print("original list:",str(list))
# list = [x for x in list if x]
# print("list after removing empty strings:",str(list))
#
# list1 =['XYZ','ABC','xyz','abc']
# list1[0],list1[-1] = list1[-1],list1[0]
# print("list after swapping:",str(list1)
#
# def iterate(d):
#     for key, values in d.items():
#
#         print(key,values)
#
# print(iterate(d = {'Red': 1, 'Green': 2, 'Blue': 3}))
#
# copy:-
# def iterate(x):
#     for key,values in x.items():
#         print(key,values)
# print(iterate(x={'rohit':18, 'ritu':17, 'kuldeep':20}))
#
#
# def add(D):
# D = {1 : 4, 2 : 3,  5 : 6 }
# sum = 0
# total = 0
# for key ,values in D.items():
#     total+=values
#     sum+=key
# print(sum,total)
#
# copy
# x = {234 : 235, 123 : 132,231 : 312}
# sum = 0
# total =0
# for key,values in x.items():
#     total+=key
#     sum+=values
# print(sum,total)
#
# def remove(dict):
#     if 'a' in dict:
#         del dict['a']
#     return dict
#
# print(remove(dict = {1 : 4, 'a' : 3,  5 : 6 }))
#
# copy:-
# def remove(dict):
#     if  'b' in dict:
#         del dict['b']
#     return dict
# print(remove(dict={'b': 1 , 2:3 , 5:6 }))
#
#
# def merge_two(dict_1,dict_2):
#     x = dict_1.copy()
#     x.update(dict_2)
#     return x
# print(merge_two(dict_1=({'a': 10, 'b': 8}),dict_2 = {'d': 6, 'c': 4}))
#
# copy:-
# def add_two(dict_1,dict_2):
#     x=dict_1.copy()
#     x.update(dict_2)
#     return x
# print(add_two(dict_1=({'a':25, 'b':25}),dict_2={'d':25,'c':25}))
#
# m

# D1 = {'emp1': {'name': 'Jim', 'age': 26, 'job': 'developer'},
#       'emp2': {'name': 'Sam', 'age': 30, 'job': 'data analyst'},
#       'emp3': {'name': 'Dean', 'age': 29, 'job': 'data scientist'},
#       'emp4': {'name': 'Leo', 'age': 25, 'job': 'python developer'}}
#
# # Actual dictionary
# print("The actual dictionary is:", D1)
# # Change the value of a dictionary
# D1['emp3']['age'] = 24
# # Updated dictionary
# print("The updated dictionary is:", D1)
#
# keys = ['first_name', 'age', 'job', 'company']
# values = ['Jim', 23, 'developer', 'XYZ']
#
# # map using zip()
# D1 = dict(zip(keys, values))
# print(D1)
#
#
# D1 = {9,5,8,80,8,0,9,8,8}
#
# print("The actual dictionary is:", str(D1))
#
# # checking if empty or not
# result = not bool(D1)
# print("Is the given dictionary empty? :", result)
#
#
#
# D1 = {'Jim': 23, 'Sam': 29, 'Dean': 33, 'Micheal': 40}
#
# # Python code to find key with Maximum value in Dictionary
# Key_max = max(D1, key=lambda x: D1[x])
# Key_min = min(D1, key=lambda x: D1[x])
# print("The key with maximum value:", Key_max, ",& corresponding value:", D1[Key_max])
# print("The key with minimum value:", Key_min, ",& corresponding value:", D1[Key_min])
#
#
# D1 = {'Jim': 23, 'Sam Winchester': 29, 'Dean Winchester': 33, 'Micheal': 40}
#
# # search substring
# search_string = "Winchester"
# # Actual dictionary
# print("The actual dictionary is:", str(D1))
#
# res_string = dict(filter(lambda item: search_string in item[0], D1.items()))
#
# # Resultant dictionary
# print("The Key-Value pair for search keys ::", str(res_string))
#
#
# D1= {'Jim': 23, 'Sam Winchester': 29, 'Dean Winchester': 45, 'Micheal': 40}
#
# #
# def getKey(dict_val):
#     for dict_key, value in D1.items():
#         if dict_val == value:
#             return dict_key
#     return "key doesn't exist"
#
#
# print("Get key of value 40:", getKey(40))
# print("Get key of value 20:", getKey(45))
#
# D1 = {'Jim': 23, 'Jerry': 29, 'Micheal': 40, 'Merlin': 45, 'Antony': 34}
#
# D1 = sorted(D1.items())
# print(D1)
#
# x1={"rohit": 18, "ritu": 17, "bitu":21}
# keys = ("kuldeep":19,)
#
# list =["banana","apple","mango","cherry"]
# first_item =list[0]
# print(first_item)
#
# list =[]
#
#
# list = [1,2,34,56,7]
# print(len(list))
#
# list = [24,53,83,46,90]
# print(str(list))
#
#
# list =[23,45,67,8,9]
# list[4]=23
# list[0]=9
# print(list)
#
# list =[13,24,35,67]
# list[0]=35
# list[2]=13
# print(list)
#
# list =[1,2,3]
# def get_maxium(list):
#    max = 0
#    for i in list:
#       if i > max:
#          max = i
#    return max
# print(get_maxium([1,2,3,5]))
#
# def get_minium(list):
#    min = 7
#    for i in list:
#       if i < min:
#          min = i
#    return min
# print(get_minium([1,2,3,4,5,6,7]))

