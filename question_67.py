my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
def find_Bitcoin(my_string):
    cheak ='Bitcoin'
    res=[]
    for i in my_string:
        if 'Bitcoin' in i:
            print('yes')
            res.append(i)
    return res
print(find_Bitcoin('my_string'))