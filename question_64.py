my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def find_B(my_string):
    cheak ='B'
    res=[]
    for i in my_string:
        if "B" in i:
            print('yes')
            res.append(i)
    return res
print(find_B(my_string))
