#Write a Python function that takes a list of dictionaries, where each dictionary contains information about a person (name, age, and hobbies), and returns a dictionary where the keys are the ages of the people and the values are lists of hobbies for people of that age. Assume that all ages are integers. If a person has multiple hobbies, they should appear in the order in which they appear in the input list.
def group_hobbies_by_age(input_list):
    hobbies_by_age = {}
    for i in input_list:
        age = i['age']
        hobbies = i['hobbies']
        if age in hobbies_by_age:
            hobbies_by_age[age].append(hobbies)
        else:
            hobbies_by_age[age]=hobbies
    return hobbies_by_age
person=[{'name': 'Alice', 'age': 25, 'hobbies': ['reading', 'hiking']},
{'name': 'Bob', 'age': 30, 'hobbies': ['running', 'swimming', 'cooking']},
{'name': 'Charlie', 'age': 25, 'hobbies': ['painting', 'gardening', 'music']},
{'name': 'David', 'age': 28, 'hobbies': ['traveling', 'yoga']}]
x = group_hobbies_by_age(input_list=person)
print(x)