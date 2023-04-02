
#question_36-:
#given the code below , use the correct method on line 3 in order to find out the number of elements in my_list.

my_list = [10, 10.5, 20, 30, 'python','java','ruby']
def find_elements(my_list):
    size =0
    for i in my_list:
        size +=1
    return size
print(find_elements(my_list))

#question_37-:
#given the code below,use the correct code on line 3 in order to remove the element of my_list locted at index 5.
my_list = [1,2,3,4,5,6,7,8,9,10]
#def remove_item(my_list):
for x in list(my_list):
    if x < 5:
        my_list.remove(x)
print(my_list)

#question_38-:
#given the code below,use the correct method on line 3 in order to add the element'c++'at the end of my_list.
my_list = [10, 10.5, 20, 30, 'python','java','ruby']
for i in range(1):
    my_list.append('c++')
print(my_list)

#question_39-:
#given the code below,use the correct method on line 3 in order to remove the element 30 from my_list.
my_list = [10, 10.5, 20, 30, 'python','java','ruby']
for i in range(1):
    my_list.pop(3)
print(my_list)

#question_40-:
#given the code below,use the correct method on line 3 in order to return the index of the elements10.5 in my_list.
my_list = [10, 10.5,10.5, 20, 30, 'python','java','ruby']
index = my_list.index(10.5)
print(index)

# #question_41-:
# # given the code below, use the correct method on line 3 in order to insert the element 77 at index 4 in my_list
# my_list = [10, 10.5, 20, 30, 'python', 'java', 'ruby']
# my_list.insert(4, 77)
# print(my_list)nmj
#
# # question_42-:
# # given the code below, use the correct method on line 3 in order to concatenate my_list with [100,101,102],by adding the latter at the end of my_list.
# my_list = [10, 10.5, 20, 30, 'python', 'java', 'ruby']
# for i in range(1):
#     my_list.extend(['100', '101', '102'])
# print(my_list)
#
# # question_43-:
# # given the code below, use the correct method on line 3 in order to find out how many tims does the element 20 occur in my_list
# my_list = [10, 10.5, 20, 30, 'python', 'java', 'ruby']
#
#
# def count(my_list, x):
#     count = 0
#     for ele in my_list:
#         if (ele == x):
#             count = count + 1
#     return count
#
#
# x = 20
# print(count(my_list, x))
#
# # question_44-:
# # given the code below, use the correct function on line 3 in order to sort the elements of my_list in ascending order.
# my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
# z = sorted(my_list)
# print(z)
#
# # question_45-:
# # given the code below, use the correct function(and argument) on line 3 in order to sort the elements of my_list in descending order.
# my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
# z = sorted(my_list, reverse=True)
# print(z)
#
# # question_46-:
# # given the code below, use the correct function on line 3 in order to find out the smallest numbers in my_list
# my_list = [10, 10.5, 11.01, 19.25, 20, 25.6, 29.99, 30]
#
#
# def min(my_list):
#     min = 0
#     for i in my_list:
#         if min <= 0:
#             min = i
#     return min
#
#
# print(min(my_list))
#
# # question_47-:
# # given the code below, use the correct function on line 3 in order to find out the smallest numbers in my_list
# my_list = [10, 10.5, 11.01, 19.25, 20, 25.6, 29.99, 30]
#
#
# def max(my_list):
#     max = 0
#     for i in my_list:
#         if max >= 0:
#             max = i
#     return max
#
#
# print(max(my_list))
#
# # question_48-:
# # given the code below ,use the correct function on line 3 in order to got the sum of all the elements of my_list.
# # my_list = [10, 10.5, 11.01,19.25,20,25.6,29.99,30]
# # def sum(my_list):
# #     sum = 0
# #     for i in my_list:
# #         if sum<=0:
# #             sum =i
# #     return sum
# # print(sum(my_list))
#
#
# # question_49-:
# # given the code below ,use the correct function on line 3 in order to delete all the elements from my_list and obtain an empty list.
# my_list = [10, 10.5, 11.01, 19.25, 20, 25.6, 29.99, 30]
# print(my_list)
#
# # question_50-:
# # given the code below ,use the correct operators on line 3 in order to add the elements of [30.10,30.02,30.03] to my_list and multiply the         list by.
# my_list = [10, 10.5, 11.01, 19.25, 20, 25.6, 29.99, 30]
# add = (my_list + [30.10, 30.02, 30.03])
# print(add)
#
# # question_51-:
# # given the code below ,use the correct operators on line 3 in order to return the element 20 from my_list based on its index.
# my_list = [10, 10.5, 20, 30, 'python', 'java', 'ruby']
# element = my_list[-2]
# print(element)
#
# # question_52-:
# # given the code below ,use the correct code  on line 3 in order to return the element java from my_list based on its index(negative)
# my_list = [10, 10.5, 20, 30, 'python', 'java', 'ruby']
# element = my_list[2]
# print(element)
#
# # question_53-:
# # given the code below,use the correct code on line 3 in order to return a slice made of [30,'python','java',] from my_list based on positive indexes.
# my_list = [10, 10.5, 20, 30, 'python', 'java', 'ruby']
# ele = my_list[3:6]
# print(ele)
#
# # question_54-:
# # given the  code below, use the correct code on line 3 in order to return a slice  made of [30,'python','java']from my_list based on negative index.
# my_list = [10, 10.5, 20, 30, 'python', 'java', 'ruby']
# ele = my_list[-4:-1]
# print(ele)
#
# # question_55-:
# # given the  code below, use the correct code on line 3 in order to return my_list except the first 3 elements ,using a single,positive index.
# my_list = [10, 10.5, 20, 30, 'python', 'java', 'ruby']
# ele = my_list[:3]
# print(ele)
#
# # question_56-:
# # given the  code below, use the correct code on line 3 in order to return my_list except the first 4 elements,using a single,negative index.
# my_list = [10, 10.5, 20, 30, 'python', 'java', 'ruby']
# ele = my_list[:-4]
# print(ele)
#
# # question_57-:
# # given the  code below, use the correct code on line 3 in order to return my_list except the first 3 elements,using a single,negative index.
# my_list = [10, 10.5, 20, 30, 'python', 'java', 'ruby']
# ele = my_list[:-4]
# print(ele)
#
# # question_58-:
# # given the  code below, use the correct code on line 3 in order to return my_list except the last 2 elements,using a single,positive index.
# my_list = [10, 10.5, 20, 30, 'python', 'java', 'ruby']
# ele = my_list[5:]
# print(ele)
#
# # question_59-:
# # given the  code below, use the correct code on line 3 in order to return every third element of my_list starting with the first element of the list.
# my_list = [10, 10.5, 20, 30, 'python', 'java', 'ruby']
# ele = my_list[::3]
# print(ele)
#
# # question_60-:
# # given the  code below, use the correct code on line 3 in order to return every fourth element of my_list starting with the last element of the list.
# my_list = [10, 10.5, 20, 30, 'python', 'java', 'ruby']
# ele = my_list[::-4]
# print(ele)

