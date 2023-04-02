#question_26-:
#given the code below,use the correct function on line 3 in order to convert num1 from integer to float.

num1 = 25
num2 = 1.87
print(type(num2))

#question_27-:
#given the code below,use the correct function on line 3 in order to convert num1 from float to integer.

num1 = 13.67
num2 = int(num1)
print(type(num2))


#question_28-:
#given the code below,use the correct math operator in between num1 and num2 on line 4 in order to obtain the result shown.

num1 = 25
num2 = 8
num3 = num1 %num2
print(num3==1)

#question_29-:
#given the code below,use the correct math operator in between num1 and num2 on line 4 in order to obtain the result shown.

num1 =10
num2 =3
num3= num1 ** num2
print(num3 == 250 * 4)

#question_30-:
#given the code below,use the correct math operator in between num1 and num2 on line 4 in order to obtain the result shown.

num1 = 5
num2 = 2
num3 = num1//num2
print(num3 == 5%3)

#question_31-:
#given the code below ,use the correct function on line 3 in order to obtain the distance between num1 and 0.

num1 = -11
num2 = abs(num1)
print(num2==11)

#question_36-:
#given the code below , use the correct method on line 3 in order to find out the number of elements in my_list.

my_list = [10, 10.5, 20, 30, 'python','java','ruby']
def find_elements(my_list):
    size =0
    for i in my_list:
        size +=1
    return size
print(find_elements(my_list))

