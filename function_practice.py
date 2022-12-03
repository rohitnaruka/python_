# 1
# def add_two_numbers ():
#     number_one = 50
#     number_two = 80
#     total = number_one + number_two
#     print(total)
# add_two_numbers()
#
# 2
# def area_of_circle (r):
#     PI = 3.14
#     area = PI * r ** 2
#     return area
# print(area_of_circle(16))

#
#
# 3
# def add_all_nums(*nums):
#     total = 0
#     for i in nums:
#         total += i
#     return total
# # print(add_all_nums(2, 3, 5))
# print(area_of_circle(10))



# 4
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) +32
# print(celsius_to_fahrenheit(2))



# 5
# def  check_season(month):
#     if month in ['september','october','november']:
#         print('autumn')
#     if month in ['december','january','fabruary']:
#         print('winter')
#     if month in ['march','april','may']:
#         print('spring')
#     if month in ['june', 'july', 'august']:
#         print('summer')
#
#     # else:
#     #     print('summer')
# print(check_season('november'))

#6
# def calculate_slope(x1, x2, y1, y2):
#     m = (y2 - y1) / (x2 - x1)
#     return m
# print(calculate_slope(10,20,50,70))



#8
#
# n = [3,5,7]
#
# def print_list(x):
#     for i in range(0,len(x)):
#         print (x[i])
# print_list👎
#


# 9
#
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
# def reverse_of_list(reverse_list):
#     for i in reverse_list[::-1]:
#         print(i)
# reverse_list = [1,2,3,4,5,6]
# reverse_list.reverse()
# print(reverse_list)
#
#
# def reverse_of_list(reverse_list):
#     for i in reverse_list[::-1]:
#         print(i)
# reverse_list = ["A","B","C"]
# reverse_list.reverse()
# print(reverse_list)

#10
# n = ['rohit','singh']
# def capital_list_items(n):
#     for i in n:
#         n[n.index(i)] = i.capitalize()
#     return n
# print(capital_list_items(n))

# 11

# def add_items(food_staff):
#
#     for i in food_staff:
#         return i
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# food_staff.append('meat')
# print(food_staff)
#
#
# def add_items(numbers):
#     for i in numbers:
#         return i
#
# numbers = [2,3,7,9]
# numbers.append(5)
# print(numbers)
#
#
#
# 12
#
#
#
# def removed_items(food_staff):
#     for i in food_staff:
#         return i
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# food_staff.remove('Mango')
# print(food_staff)
#
#
# def removed_items(numbers):
#     for i in food_staff:
#         return i
# numbers = [2,3,7,9]
# numbers.remove(3)
# print(numbers)
#
#
#
# 13

#
#
# def sum_of_numbers(n):
#     total = 0
#     for i in range(n+1):
#         total+=i
#     print(total)
# print(sum_of_numbers(5))
# print(sum_of_numbers(10))
# print(sum_of_numbers(100))

# 15
# def add_of_evens(n):
#     evens = []
#     for i in range(n + 1):
#         if i % 2 == 0:
#             evens.append(i)
#     return evens
# print(add_of_evens(10))
# add_even_number = [0+2+4+6+8+10]
# print(add_even_number)
#
#
#
# #14
# def add_of_odd(n):
#     odd = []
#     for i in range(n + 1):
#         if i % 2 != 0:
#             odd.append(i)
#     return odd
# print(add_of_odd(10))
# add_odd_numbers = [1+3+5+7+9]
# print(add_odd_numbers)
#level 2



# 1
# def add_of_odd(n):
#     odd = []
#     for i in range(n + 1):
#         if i % 2 != 0:
#             odd.append(i)
#     return odd
#
# all_odd_numbers = add_of_odd(100)
# print(len(all_odd_numbers))


# 2
# def add_of_evens(n):
#     evens = []
#     for i in range(n + 1):
#         if i%2 == 0:
#             evens.append(i)
#     return evens
# all_evens_numbers = add_of_evens(100)
# print(len(all_evens_numbers))
#
#2
#     b = 1
#     for i in range(a + 1):
#         b *= 1
#     return a
# print(fectorial(1))
#3
# def is_empty(check):
#     if check:
#         return True
#     else:
#         return False
# print(is_empty(90))



#4
# list = [10,20,30, 50, 40, 50]
# def calculate_mean(list):
#
#     return sum(list)/len(list)
# c = calculate_mean(list)
# print(c)
#
#
# list = [10, 20, 30, 50 ,40 ,50]
# def calculate_midean(list):
#     data = sorted(list)
#     index = len(data)//2
#     if len(list)%2 != 0:
#         return data[index]
#     return (data[index - 1] + data[index])/ 2
# a = calculate_midean(list)
# print(a)

# list = [10,20,30,50,40,50]
# def calculate_mode(list):
#     mode = max(list,key = list.count)
#     return mode
# print(calculate_mode(list))



# for i in range(10):
#     print(i)



# list =  [10,20]
# def variance(list):
#     n = len(list)
#     mean = sum(list)/n
#     deviations = [(x - mean)**2for x in list]
#     variance = sum(deviations)/n
#     return variance
# print(variance(list))
#


#list = [10,20]
# def standard_deviation(list):
#
#     n = len(list)
#     mean = sum(list) / n
#     deviations = [(x - mean) ** 2 for x in list]
#     variance = sum(deviations) / n
#     standard_deviation = variance ** 0.5
#     return standard_deviation
# print(standard_deviation(list))
#




# level 3
# 1
# def is_prime(n):
#     for i in range(2,n):
#         if (n%i) == 0:
#             return True
#         return False
# #
# print(is_prime(4))



# 2

# list = ['apple','banana','orange']
# def function(list):
#
#     if (len(set(list)) == len(list)):
#         print("all elements are unique")
#     else:
#         print("all elements  are not unique")
# print(list)


#3
# list = [1,2,3,4,5,6]
# def check_list(list):
#     return len(set(list)) == 1
# list = [1, 1]
# if check_list(list) == True:
#     print('same')
# else:
#     print('not same')
