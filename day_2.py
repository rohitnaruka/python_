#ages = {
#     "peter":10,
#     "isabel":11,
#     "anna":9,
#     "thomas":10,
#     "bob":10,
#     "joseph":11,
#     "maria":12,
#     "garbriel":10,
# }
# def length_ages(ages):
#     length = len(ages)
#     return length
# print(len(ages))
#
#
# ages = {
#     "peter":10,
#     "isabel":11,
#     "anna":9,
#     "thomas":10,
#     "bob":10,
#     "joseph":11,
#     "maria":12,
#     "garbriel":10,
# }
# def average_num(ages):
#     total = 0
#     for i in ages.values():
#         total += i
#     avg_val = total / len(ages)
#     return avg_val
# print(average_num(ages))
#
#
# ages = {
#     "peter":10,
#     "isabel":11,
#     "anna":9,
#     "thomas":10,
#     "bob":10,
#     "joseph":11,
#     "maria":12,
#     "garbriel":10,
# }
# def oldest_person(ages):
#     max_age = 0
#     max_age_name = ''
#     for name , age in ages .items():
#         # print(name,age)
#         if max_age_name is None or (age > max_age):
#             max_age = age
#             max_age_name = name
#     return max_age,max_age_name
# print(oldest_person(ages))
#
# #
# ages = {
#     "peter":10,
#     "isabel":11,
#     "anna":9,
#     "thomas":10,
#     "bob":10,
#     "joseph":11,
#     "maria":12,
#     "garbriel":10,
# }
# def function(ages,n):
#     new_ages = {}
#     for name , age in ages.items():
#         #print(x,y)
#         if age == n:
#             #age == n => 10==10true ya false
#             new_ages[name] = age
#     return new_ages
# ages = {
#     "peter":10,
#     "isabel":11,
#     "anna":9,
#     "thomas":10,
#     "bob":10,
#     "joseph":11,
#     "maria":12,
#     "garbriel":10,
# }
# n=10
# x = function(ages,n)
# print(x)
#
# students = {
#     "Peter": {"age": 10, "address": "Lisbon"},
#     "Isabel": {"age": 11, "address": "Sesimbra"},
#     "Anna": {"age": 9, "address": "Lisbon"},
# }
# def students_length(students):
#     total_length = len(students)
#     return total_length
# print(students_length(students))
#
#
#
# students = {
#     "Peter": {"age": 10, "address": "Lisbon"},
#     "Isabel": {"age": 11, "address": "Sesimbra"},
#     "Anna": {"age": 9, "address": "Lisbon"},
# }
# def function(student, x):
#     new_dictionary = {}
#     for p, q in students.items():
#               # print(x,y)
#         for a, b in q.items():
#             if x == b:
#                 new_dictionary[p] = b
#     return new_dictionary
# y = function(students, x='Lisbon')
# print(y)
#
# students = {
#     "Peter": {"age": 10, "address": "Lisbon"},
#     "Isabel": {"age": 11, "address": "Sesimbra"},
#     "Anna": {"age": 9, "address": "Lisbon"},
# }
# def average_student(students):
#     sum = 0
#     for i in students.keys():
#
#         sum += students[i]['age']
#     average = sum/len(students)
#     return average
# print(average_student(students))
