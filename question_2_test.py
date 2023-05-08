first of all i created a function its name group hobbies by ages
def group_hobbies_by_age(input_list):
#then i created an variable named group_hobbies_by_age = {}
    hobbies_by_age = {}
#then i ran the forloop over the input list
    for i in input_list:
#then i created a variable and checked it all in one go
        age = i['age']
# then i created a variable and checked it all in one go
        hobbies = i['hobbies']
        if age in hobbies_by_age:
#then i put a condition with hobbies_by_age.
            hobbies_by_age[age].append(hobbies)
#then we appended all the hobbies
        else:
            hobbies_by_age[age]=hobbies
#then i put a condition
    return hobbies_by_age
#then i return hobbies_by_age
person=[{'name': 'Alice', 'age': 25, 'hobbies': ['reading', 'hiking']},
{'name': 'Bob', 'age': 30, 'hobbies': ['running', 'swimming', 'cooking']},
{'name': 'Charlie', 'age': 25, 'hobbies': ['painting', 'gardening', 'music']},
{'name': 'David', 'age': 28, 'hobbies': ['traveling', 'yoga']}]

x = group_hobbies_by_age(input_list=person)
#then i made one named x inside that we put our function
print(x)
#then i print x