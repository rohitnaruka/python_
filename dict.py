# nested dictionary-: nested dictionary means putting a dictionary inside another dictionary.
# its a collections of dictionaries into a single dictionary.
#
# course={
#     'english':{'duration':'3 months','fess':15000},
#     'hindi':{'duration':'2 months','fess':200},
#     'math':{'duration':'1 months','fess':100},
#     }
# print(len(course))
# print(course['english']['fess'])
# # for k,v in course.items():
# #     print(k,v['duration'],v['fess'])
# #     #print(k,v)
#
# products ={
#     "mystock1":{
#     "product":'iphone',
#     "price":150000,
#     "quantity": 100,
#     "instock": "yes"
#     },
#     "mystock2":{
#     "product":"airphone",
#     "price": 38888,
#     "quantity": 100,
#     "instock": 'no',
#     }
# }
# # if "mystock1" in products:
# #     for  in products:
# print(products['mystock1'],["price"],["instock"])
# B=products["mystock1"]["instock"]
# print(A,B)

# print(products)
# for i in products.items():
#     print(products)
# for k,v in products .items():
#     if "mystock1" in products:
#        print(k,v["product"],v["price"])
# print(products["mystock2"]["instock"])


# data = {
#     'student 1': {'name':'rahul','rn':3, "age":12},
#     'student 2': {'name':'rockey','rn':2, "age":11},
#     'student 3': {'name':'luckey','rn':1, "age":13},
# }
# for i in data['student 2']:
#     #print(data[i])
#     print(data["student 2"].values())

# people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
#           2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
# people[3]={'name': 'rohit', 'age': '19', 'sex': 'male'}
# print(people[3])
# people[3]['name']='rohit'
# people[3]['age']='19'
# people[3]['sex']='male'
# print(people[3])
# print(people)

# pepole={1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
#           2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
# pepole[2]['sex']='male'
# print(pepole)

pepole={1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
#x= pd.dataframe(pepole)




# course={
#     'english':{'duration':'3 months','fess':15000},
#     'hindi':{'duration':'2 months','fess':200},
#     'math':{'duration':'1 months','fess':100},
#     }
#
# del course['english']
# print(course)

#
# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male', 4: [2, 3, 5],
#               'john_friend': {'name': 'Marie', 'age': '22', 'sex': 'Female,', 9: [1, 2, 4, 5, 6]}},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
#           }
# def sum_pepole(pepole):
#     sum = 0
#     if 9 in people[1]["john_friend"]:
#         for i in people[1]["john_friend"][9]:
#             sum = sum + i
#             avrage=sum/len("john_frined")
#     return avrage
# print(sum_pepole(pepole))
#
# people={1:[2,3,4],
#         2:[1,2,3,4]
#         }
# def sum_pepole(pepole):
#     sum = 0
#     for i in people[]:
#             sum = sum + i
#             average=sum/len(people)
#     return average
# print(sum_pepole(pepole))



# course={
#     'english':{'duration':'3 months','fess':15000},
#     'hindi':{'duration':'2 months','fess':200},
#     'math':{'duration':'1 months','fess':100},
#     }
# print(course['english'],['duration'],['fess'])
#
# people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
#           2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
# for i in people[1].items():
#     print(people[1].values())



# nested_dict={
#     '1':{'a':5,'b':6,'c':7},
#     '2':{'x':1,'y':2,'z':3},
#     '3':{'m':8,'n':9,'o':10}
# }
# min_value=None
# min_key=None
# for i,j in nested_dict.items():
#     for j,value in j.items():
#         if min_value is None or value < min_value:
#             min_value = value
#             min_key = (i,j)
# print([min_value])
# print([min_key])
#
#

# nested_dict={
#     '1':{'a':5,'b':6,'c':7},
#     '2':{'x':1,'y':2,'z':3},
#     '3':{'m':8,'n':9,'o':10}
# }
# max_value=None
# max_key=None
# for i,j in nested_dict.items():
#     for i,j in j.items():
#         if max_value is None or value<max_value:
#             max_value=value
#             max_key=(i,j)
# print({max_value})
# print({max_key})
#
#
#
# #
# nested_dict={
#     '1':{'a':5,'b':6,'c':7},
#     '2':{'x':1,'y':2,'z':3},
#     '3':{'m':8,'n':9,'o':10}
# }
# min_value=None
# min_key=None
# for i,j in nested_dict.items():
#     for j,value in j.items():
#         if min_value is None or value < min_value:
#             min_value = value
#             min_key = (i,j)
# print([min_value])
#
#
#
# # nested_dictionary = {1:{'name': 'ritu','age':18,'ritu_friend':{'name':'rohit', 'age':20}},
# #                      2:{'name':'ridhi', 'age':20,}
# #                      }
#
# print(nested_dictionary[1]['ritu_friend'])


# people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
#           2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
# if 1 in people:
#     person1 = people[1]
# for key, value in person1.items():
#     print(f"{key},{value}")
# else:
#     print("not found")


# my_dict={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# def sorted_dict(my_dict):
#     new_sorted_dict={}
#     for i in sorted(my_dict.keys()):
#         new_sorted_dict[i]=my_dict[i]
#     return new_sorted_dict
# print(sorted_dict(my_dict))




# my_dict={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# def sorted_dict(my_dict):
#     new_sorted_dict={}
#     for key,value in sorted(my_dict.items(),key=lambda x:x[1]):
#         new_sorted_dict[key]=value
#     return new_sorted_dict
# print(sorted_dict(sorted_dict(my_dict)))
#
# my_dict={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# def sorted_dict(my_dict):
#     new_sorted_dict={}
#     for keys,value in sorted(my_dict.items()):
#         new_sorted_dict[keys]=value
#     return new_sorted_dict
# print(sorted_dict(my_dict))


#new

#1.how to add elements in nested_dict
# nested_dict={
#     'english_key1':{
#         'x_key1':'y1',
#         'x_key2':'y2'
#     },
#     'hindi_key2':{
#         'x_key3':'y3',
#         'x_key4':'y4'
#     }
# }
# nested_dict['english_key1']['new_x_key']='new_y'
# print(nested_dict)
#
#2.how to add another dict to nested_dict
# nested_dict={
#     'english_key1':{
#         'x_key1':'y1',
#         'x_key2':'y2'
#     },
#     'hindi_key2':{
#         'x_key3':'y3',
#         'x_key4':'y4'
#     }
# }
# new_dict={
#     'x_key5': 'y5',
#     'x_key6': 'y6'
# }
# for key ,value in new_dict.items():
#     nested_dict['english_key1']['new_key']=new_dict
# print(nested_dict)
#
#
#3.how to delete elements a nested_dict
# course={
#     'english':{'duration':'3 months','fess':15000},
#     'hindi':{'duration':'2 months','fess':200},
#     'math':{'duration':'1 months','fess':100},
#     }
#
# del course['english']['fess']
# print(course)
#
#4.how to delete dictionary in nested dict
# course={
#     'english':{'duration':'3 months','fess':15000},
#     'hindi':{'duration':'2 months','fess':200},
#     'math':{'duration':'1 months','fess':100},
#     }
#
# del course['english']
# print(course)
#
#find the sum of all items in a dict
# my_dict={ 1:10,3:21,4:32,7:20}
# def sum(my_dict):
#     total=0
#     sum=0
#     for key,value in my_dict.items():
#         sum += key
#         total += value
#     return total,sum
# print(sum(my_dict))
#
#
# #call the return sum() function with the dictionaryas input and print the result
# def sum_of_items(input_dict):
#     sum=0
#     total=0
#     for key,value in input_dict.items():
#         sum+=key
#         total+=value
#     return sum,total
# print(sum_of_items(input_dict={ 1:10,3:21,4:32,7:20}))
#
# #convert the dict values to a list using the list()function
# my_dict={ 'a':10,'b':21,'c':32,'d':20}
# def convert_value_list(my_dict):
#     value_list=[]
#     for value in my_dict.values():
#         value_list.append(value)
#     return value_list
# print(convert_value_list(my_dict))
#
#
#
#
# # import numpy as np
# #
# # my_list=[1,2,3,4,5]
# # my_array=np.array(my_list)
# # print(my_array)n



#Write a Python script to merge two Python dictionaries.
