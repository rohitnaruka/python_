# # # Write a program that takes a list of numbers and prints the sum of the positive numbers.
# # # [-2, 5, -10, 8, 3]
#
# # def add_positive_numbers(input: list) -> int:
# #     sum = 0
# #     for i in input:
# #         if i > 0:
# #             sum += i
# #     return sum
# # print(add_positive_numbers(input = 1))
#
# #     return l[index]
# # [3, 8, 2, 7, 4, 9]
# # Write a program that takes a list of integers and returns all the even numbers.
# def find_all_even(input: list):
#     even = []
#     odd = []
#     sum = 0
#     for i in input:
#         if i % 2 == 0:
#             even.append(i)
#         elif i % 2 != 0:
#             sum += i
#             odd.append(i)
#     return odd, sum
# odd_numbers,sum_of_odd = find_all_even(input=[3, 8, 2, 7, 4, 9])
# print(odd_numbers)
# print(sum_of_odd)
#
# def longest_string(input_list):
#     longest = ""
#     for string in input_list:
#         if len(string)>len(longest):
#             longest=string
#     return longest
# input_list = ['apple','banana','kiwi','orange','pear','pineapple']
# print(longest_string(input_list))
#
#
# def longest_string(input_list):
#     longest = ""
#     second_max = ""
#     for string in input_list:
#         if len(string)>len(longest):
#             second_max = longest
#             longest = string
#         elif len(string) > len(second_max):
#             second_max = string
#     return longest,second_max
# input_list =['apple','banana','kiwi','orange','pear',]
# print(longest_string(input_list))


a = 1
b = 2
c = 3

print(max(i))

#nested list-:
#
# a=[[24,30,36],[28,35,42]]
# for i in range(6,8):
#     for j in range(4,7):
#         pass
# lst =[[i*j for j in range(4,7)] for i in range(6,8)]
# print(lst)
#
# #
# a=[[25,34,45],[21,34,22]]
# for i in range(4,5):
#     for j in range(6,5):
#         pass
# list=[[i*j for j in range(4,5)] for i in range(6,5)]
# print(list)
# #
# # #
# students_rec = [
#     [1,'rohit',19,95880],
#     [2,'ritu',18,72024],
#     [3,'kuldeep',20,903454]
# ]
# for x in students_rec:
#     for y in x:
#      print(y,end=' ')
#     print()

# def average_ratings(books):
#     result = []
#     for book in books:
#         reviews = book['reviews']
#         num_review = len(reviews)
#         print(len(reviews))
# #
#         if num_review == 0:
#             avg_rating = 0
#             print(avg_rating)
#         else:
#             total_rating = sum(review['rating'] for review in reviews)
#             avg_rating = total_rating / num_review
#             print(total_rating)
#
#         result.append({
#             'title': book['title'],
#             'author': book['author'],
#             'avg_rating': avg_rating,
#             'num_reviews': num_review
#         })
#     return result
#
#
# books = [
#     {
#         "title": "The Great Gatsby",
#         "author": "F. Scott Fitzgerald",
#         "reviews": [
#             {"name": "John Doe", "rating": 4, "comments": "Great book!"},
#             {"name": "Jane Smith", "rating": 3, "comments": "Good read."},
#             {"name": "Bob Johnson", "rating": 5, "comments": "Amazing!"},
#         ]
#     },
#     {
#         "title": "To Kill a Mockingbird",
#         "author": "Harper Lee",
#         "reviews": [
#             {"name": "Alice Chen", "rating": 4, "comments": "Very well-written."},
#             {"name": "Tom Smith", "rating": 4, "comments": "Enjoyed reading it."},
#         ]
#     },
#     {
#         "title": "1984",
#         "author": "George Orwell",
#         "reviews": []
#     }
# ]
#
# result = average_ratings(books)
# print(result)
#
#
#
#
#
#
# # def book_ratings(book_list):
# #     book_ratings = []
# #     for book in book_list:
# #         sum_rating =0
# #         num_reviews =len(book["reviews"])
# #         if num_reviews > 0:
# #             for review in book["reviews"]:
# #                 sum_rating+=review["rating"]
# #             average_ratings = sum_rating/num_reviews
# #         else:
# #             average_ratings=0
# #
# #         book_ratings.append({
# #             "title": book["title"],
# #             "author":book["author"],
# #             "average_rating": sum_rating,
# #             "total_reviews":num_reviews
# #             })
# #     return book_ratings
# books = [
#     {
#         "title": "The Great Gatsby",
#         "author": "F. Scott Fitzgerald",
#         "reviews": [
#             {"name": "John Doe", "rating": 4, "comments": "Great book!"},
#             {"name": "Jane Smith", "rating": 3, "comments": "Good read."},
#             {"name": "Bob Johnson", "rating": 5, "comments": "Amazing!"},
#         ]
#     },
#     {
#         "title": "To Kill a Mockingbird",
#         "author": "Harper Lee",
#         "reviews": [
#             {"name": "Alice Chen", "rating": 4, "comments": "Very well-written."},
#             {"name": "Tom Smith", "rating": 4, "comments": "Enjoyed reading it."},
#         ]
#     },
#     {
#         "title": "1984",
#         "author": "George Orwell",
#         "reviews": []
#     }
# ]
#book_ratings=book_ratings(books)
#print(book_ratings)
# #
#
# def group_hobbies_by_age(input_list):
#     hobbies_by_age = {}
#     for i in input_list:
#         age = i['age']
#         hobbies = i['hobbies']
#         if age in hobbies_by_age:
#             hobbies_by_age[age].append(hobbies)
#         else:
#             hobbies_by_age[age]=hobbies
#     return hobbies_by_age
# person=[{'name': 'Alice', 'age': 25, 'hobbies': ['reading', 'hiking']},
# {'name': 'Bob', 'age': 30, 'hobbies': ['running', 'swimming', 'cooking']},
# {'name': 'Charlie', 'age': 25, 'hobbies': ['painting', 'gardening', 'music']},
# {'name': 'David', 'age': 28, 'hobbies': ['traveling', 'yoga']}]
# x = group_hobbies_by_age(input_list=person)
# print(x)
