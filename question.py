#1.
# my_string="how are you"
# print(my_string[-1])

#2
# my_string="how are you what are you doing"
# print(my_string[5])

#3.
# my_string="how are you what are you doing"
# print(my_string[-10])

#4.
# my_string="how are you what are you doing"
# print(my_string.index("w"))
# #5
# my_string="how are you what are you doing"
# print(my_string.count("r"))
#
# #6.
# my_string="how are you what are you doing"
# print(my_string.upper())
# #7
# my_string="how are you what are you doing"
# print(my_string.find("what"))
#
# #8
# my_string="how are you what are you doing"
# print(my_string.startswith("x"))

#9
# my_string="how are you what are you doing"
# print(my_string.swapcase())

#10.
# my_string="how are you what are you doing"
# print(my_string.replace( " ",""))
#
# #11
# my_string= "how are you what are you doing"
# print(my_string.replace("you","are"))
#
# #12
# my_string="how are you what are you doing"
# print(my_string.split(","))
#
# #13
# my_string="how are you what are you doing"
# print("$".join(my_string))
#14
# my_string="how are you what are you doing"
# other_string="hello rohit"
# print(my_string + other_string)
#
# #15
# my_string="how are you what are you doing"
# print(my_string.title())
#
# #16
# my_string="in %s someone paid %s %s for two pizzas."
# print(my_string%("2023","50k","bitcoin"))
#
# #17
# my_string="in {} someone paid {} {} for two pizzas."
# print(my_string.format("2023","50k","bitcoin"))
#
# #18
# my_string="how are you what are you doing"
# print(my_string[3:7])

#19
# my_string="in 2023 someone paid 50k bitcoin for two pizzas."
# print(my_string[-23:-16])
#
# #20
# my_string="in 2023 someone paid 50k bitcoin for two pizzas."
# print(my_string[:12])
#
# #21.
# my_string="in 2023 someone paid 50k bitcoin for two pizzas."
# print(len(my_string))
#print(my_string[-9:])

#22
# my_string="in 2023 someone paid 50k bitcoin for two pizzas."
# print(my_string[::-1])

#23
# my_string="in 2023 someone paid 50k bitcoin for two pizzas."
# print(my_string[::7])

#24
# my_string="in 2023 someone paid 50k bitcoin for two pizzas."
# print(my_string[10:])

#25
# my_string="in 2023 someone paid 50k bitcoin for two pizzas."
# print(my_string[:-4])



#NUMBERS-:
#26
# num1=25
# #num2=float(num1)
# print(type(num1))
#
# #27
# num1=45.64
# #num2=int(num1)
# print(type(num1))
#
# #28
# num1=24
# num2=8
# num3=num1%num2
# print(num3==0)
#
#
# #29
# num1=10
# num2=3
# num3=num1**num2
# print(num3==250*4)

#30
# num1=5
# num2=2
# num3=num1//num2
# print(num3==5%3)

#31
#abs()=return the absolute values
# num1=-11
# num2=abs(num1)
# print(num2 == 11)

#32
#pow= is used to calculate the power of numbers
# num1=10
# num2=5
# num3=pow(num1,num2)
# print(num3 == 100000)

#33
# result =((25%7+10/2)%3==0)and((abs(-19)/2-2)>9)
# print(result)

#34
# result=(min(pow(2, abs(3)),9)==3**2-1) or(66%20+2>2**3)
# print(result)

#35
#result=bool(150%(10**2/2))
#print(result)

#LIST:-
#36
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x=len(my_list)
# print(x)
#
# #37
# my_list=[1,2,3,4,6,7,9,7,6,5]
# my_list.pop(7)
# print(my_list)
#
# #38
# my_list=[1,2,3,4,6,7,9,7,6,5]
# my_list.append(10)
# print(my_list)
#
# #39
# my_list=[1,2,3,4,6,7,9,7,6,5]
# my_list.remove(5)
# print(my_list)
#
# #40
# my_list =[1,2,3,4,6,7,9,7,6,5]
# index=my_list.index(1)
# print(my_list)
#
# #41
# my_list=[1,2,3,4,6,7,9,7,6,5]
# my_list.insert(10 ,99)
# print(my_list)
#
# #42
# my_list = [1,2,3,4,6,7,9,7,6,5]
# my_list.extend([10,100,500])
# print(my_list)
#
# #43
# my_list =[1,2,3,4,6,7,9,7,6,5]
# x=my_list.count(7)
# print(x)
#
# #44
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x=sorted(my_list)
# print(x)
#
# #45
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x=sorted(my_list,reverse=True)
# print(x)
#
# #46
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x=min(my_list)
# print(x)
#
# #47
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x= max(my_list)
# print(x)
#
# #48
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x=sum(my_list)
# print(x)
#
# #49
# my_list=[1,2,3,4,6,7,9,7,6,5]
# my_list.clear()
# print(my_list)
#
# #50
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x = (my_list+[20.5,34.4,23.9])*2
# print(x)

#51
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x=my_list[2]
# print(x)
#
# #52
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x=my_list[-2]
# print(x)
#
# #53
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x=my_list[4:8]
# print(x)
#
# #54
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x=my_list[-8:-2]
# print(x)
#
# #55
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x=my_list[2:]
# print(x)
#
# #56
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x=my_list[:-3]
# print(x)
#
# #57
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x=my_list[-4:]
# print(x)
#
# #58
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x=my_list[:3]
# print(x)
#
# #59
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x=my_list[::2]
# print(x)
#
# #60
# my_list=[1,2,3,4,6,7,9,7,6,5]
# x=my_list[::-2]
# print(x)

#SETS:-
#61
# my_list=[1,4,6,8,9,67,8,5,4,7]
# my_set=set(my_list)
# print(type(my_set))

# #62
# my_list=[1,4,6,8,9,67,8,5,4,7]
# my_set=frozenset(my_list)
# print(type(my_set))

# #63
# my_set={1,4,6,8,9,67,8,5,4,7}
# check=11 in my_list
# print(check)

#64
my_set={1,4,6,8,9,67,8,5,4,7}
my_set.add(19)
print(my_set)

# #65
# my_set={1,4,6,8,9,67,8,5,4,7}
# my_set.remove(8)
# print(my_set)

# #66
# my_set1={1,4,6,8,9,67,8,5,4,7}
# my_set2={3,4,5,3,5,7,8,0,9}
# common=my_set1.intersection(my_set2)
# print(common)

#67
# my_set1={1,4,6,8,9,67,8,5,4,7}
# my_set2={3,4,5,3,5,7,8,0,9}
# x =my_set1.union(my_set2)
# print(x)
# #68
# my_set1={1,4,6,8,9,67,8,5,4,7}
# my_set2={3,4,5,3,5,7,8,0,9}
# x =my_set2.difference(my_set1)
# print(x)


#TUPLE:-
#69
# my_tup = ("india","chaina","pakistan","srilanka","butan","bharat")
# x = len(my_tup)
# print(x)
#
# #70
# my_tup = ("india","chaina","pakistan","srilanka","butan","bharat")
# x = my_tup.index("india")
# print(x)

#71
# my_tup = ("india", "chaina", "pakistan", "srilanka", "butan", "bharat")
# (sr,ch,pk) = my_tup
# print(sr+","+ch+","+pk)

#72
# my_tup = ("india", "chaina", "pakistan", "srilanka", "butan", "bharat")
# x =max(my_tup)
# print(x)
#
# #73
# my_tup = ("india", "chaina", "pakistan", "srilanka", "butan", "bharat")
# x=my_tup.count('srilanka')
# print(x)
#
# #74
# my_tup = ("india", "chaina", "pakistan", "srilanka", "butan", "bharat")
# x = my_tup[-5:]
# print(x)
#
# #75
# my_tup = ("india", "chaina", "pakistan", "srilanka", "butan", "bharat")
# x = my_tup[:-3]
# print(x)
#
# #76
# my_tup = ("india", "chaina", "pakistan", "srilanka", "butan", "bharat")
# x = my_tup[3:]
# print(x)
#
# #77
# my_tup = ("india", "chaina", "pakistan", "srilanka", "butan", "bharat")
# x = my_tup[:5]
# print(x)
#
# #78
# my_tup = ("india", "chaina", "pakistan", "srilanka", "butan", "bharat")
# x = my_tup[:-3]
# print(x)


#RANGE_QUESTION:-
#79
# x=range(0,10)
# print(list(x))
#
# #80
# x=range(456,653)
# print(list(x))
#
# #81
# x=range(10,20,6)
# print(list(x))
#
# #82
# x=range(5,145,50)
# print(list(x))
#
# #83
# x=range(-45,-46,-48)
# print(list(x))
#
# #84
# x=range(45,-58,-85)
# print(list(x))
#
# #85
# x=range(-10,-9)
# print(list(x))

#DICTIONARY-:
#86
# name={1:"rohit",2:"ritu",3:"bittu",4:"rahul",5:"lucky"}
# value=name[4]
# print(value)
#
# #87
# name={1:"rohit",2:"ritu",3:"bittu",4:"rahul",5:"lucky"}
# value=name.get(4)
# print(value)
#
# #88
# name={1:"rohit",2:"ritu",3:"bittu",4:"rahul",5:"lucky"}
# name[4]="seru"
# print(name[4])
#
# #89
# name={1:"rohit",2:"ritu",3:"bittu",4:"rahul",5:"lucky"}
# name[6]="seru"
# print(name[6])
#
# #90
# name={1:"rohit",2:"ritu",3:"bittu",4:"rahul",5:"lucky"}
# x=len(name)
# print(x)
#
# #91
# name={1:"rohit",2:"ritu",3:"bittu",4:"rahul",5:"lucky"}
# del name[4]
# print(name)
#
# #92
# name={1:"rohit",2:"ritu",3:"bittu",4:"rahul",5:"lucky"}
# name.pop(5)
# print(name)
#
# #93
# name={1:"rohit",2:"ritu",3:"bittu",4:"rahul",5:"lucky"}
# check=5 not in name
# print(check)
#
# #94
# name={1:"rohit",2:"ritu",3:"bittu",4:"rahul",5:"lucky"}
# name.clear()
# print(name)
#
# #95
# name={1:"rohit",2:"ritu",3:"bittu",4:"rahul",5:"lucky"}
# x  = name.items()
# print(list(name))
#
# #96
# name={1:"rohit",2:"ritu",3:"bittu",4:"rahul",5:"lucky"}
# add =sum(name)
# print(add)
#
# #97
# name={1:"rohit",2:"ritu",3:"bittu",4:"rahul",5:"lucky"}
# val = name.values()
# print(list(val))
#
# #98
# name={1:"rohit",2:"ritu",3:"bittu",4:"rahul",5:"lucky"}
# x=min(name)
# print(x)
#
# #99
# name={1:"rohit",2:"ritu",3:"bittu",4:"rahul",5:"lucky"}
# keys=name.keys()
# print(list(keys))
#
# #100
# name={1:"rohit",2:"ritu",3:"bittu",4:"rahul",5:"lucky"}
# name.popitem()
# print(len(name))

# DATA TYPE CONVERSIONS:-
#101
# value=10
# conv=str(value)
# print(type(conv))
#
# #102
# value="10"
# conv=int(value)
# print(type(conv))

#103
# value=10
# conv=float(value)
# print(type(conv))
#
# #104
# value=10
# conv=str(value)
# print(type(conv))
#
# #105
# value="hello!"
# conv=list(value)
# print(type(conv))
#
# #106
# value=[2,8,6,7,9,5]
# conv=tuple(value)
# print(type(conv))
#
# #107
# value=[2,8,6,7,9,5]
# conv=frozenset(value)
# print(type(conv))
#
# #108
# value=10
# conv=bin(value)
# print(type(conv))
#
# #109
# value=10
# conv=hex(10)
# print(conv)
#
# #110
# value='0b1010'
# conv=int(value,2)
# print(conv)
#
# #111
# value='0xa'
# conv=int(value,16)
# print(conv)

#conditionals:-
#112
# x="how are you where are you from"
# if len(x)<=50:
#     print("True!")
# #113
# x="hoW are You where are You from"
# if type(x) is str and x.startswith("W"):
#     print("True!")
# #114
# x="how are you where are you from"
# if "z" in x or x.count("Y")<=2:
#     print("True!")
#
# #115
# x="how are you where are you from"
# if x.index("y")>10:
#     print("True!")
# else:
#     print("False!")
#
# #116
# x = "how are you where are you from"
# if x[-3:].isdigit():
#     print("True!")
# else:
#     print("False!")
#
# #117
# x=[111,111.3,112.03,["length","width","heigth"],109,293,480.4,["length","width","heigth"]]
# if len(x)>=8 and type(x[6]) is float:
#     print("True!")
# else:
#     print("False!")
#
# #118
# x=[111,111.3,112.03,["length","width","heigth"],109,293,480.4,["length","width","heigth"]]
# if x[3][1].endswith("h") and x[7][0].endswith("h"):
#     print("True!")
# else:
#     print("False!")
#
# #119
# x=[111,111.3,112.03,["length","width","heigth"],109,293,480.4,["length","width","heigth"]]
# if x[3][2].endswith("h") and x[7][1].endswith("h"):
#     print("True!")
# else:
#     print("False!")
#
# #120
# x=[111,111.3,112.03,109,296,467,["length","width","heigth"]]
# if max(x[:3])<=min(x[3:6]):
#     print("True!")
# else:
#     print("False!")
# #121
# x=[111,111.3,112.03,109,296,467,["length","width","heigth"]]
# if x.count(112)>=1or x.index(111)==0:
#     print("True!")
# else:
#     print("False!")
# #121
# x={1:"python",2:"java",3:"javascript",4:"ruby",5:"perl"}
# if x[5]=="perl"or len(x) % 5<2:
#     print("True!")
# else:
#     print("False!")

#122
# x = {1: "python", 2: "java", 3: "javascript", 4: "ruby", 5: "perl"}
# if 3  in x and sorted(x.values())[0]=="c#":
#     print("True!")
# else:
#     print("False!")
# #123
# x = {1: "python", 2: "java", 3: "javascript", 4: "ruby", 5: "perl"}
# if sorted(x.values())[-1][-1]=="n":
#     print("True!")
# else:
#     print("False!")
# #124
# x = {1: "python", 2: "java", 3: "javascript", 4: "ruby", 5: "perl"}
# if sorted(x.keys())[-1]%sorted(x.keys())[-2]==sorted(x.keys())[0]:
#     print("True!")
# else:
#     print("False!")
# #125
# x = {1: "python", 2: "java", 3: "javascript", 4: "ruby", 5: "perl"}
# if sum(x)<len(x[1]+x[2]+x[3]+x[4]+x[5]):
#     print("True!")
# else:
#     print("False!")
#
# #126
# x = [list(range(5)),list(range(5,9)),list(range(1,10,3))]
# if x[0][2]<2:
#     print("True!")
# elif x[0][4]==5:
#     print("False!")
# else:
#     print("None!")
#
# #127
# x = [list(range(5)),list(range(5,9)),list(range(1,10,3))]
# if x[2][2]<6:
#     print("True!")
# elif x[1][0]==5:
#     print("False!")
# else:
#     print("None!")
#
# #128
# x = [list(range(5)),list(range(5,9)),list(range(1,10,3))]
# if x[0][-1]>3:
#     print("True!")
# elif x[1][-1]<9:
#     print("False!")
# else:
#     print("None!")
#
# #129
# x = [list(range(5)),list(range(5,9)),list(range(1,10,3))]
# if len (x[0])>= 5:
#     print("True!")
# elif len(x[1])==4:
#     print("False!")
# else:
#     print("None!")
#
# #130
# x = [list(range(5)),list(range(5,9)),list(range(1,10,3))]
# if sum([0])>sum(x[2]):
#     print("True!")
# elif max(x[1])>max(x[2])==5:
#     print("False!")
# else:
#     print("None!")
#
# #131
# x = [list(range(5)),list(range(5,9)),list(range(1,10,3))]
# if max(x[0]) - x[2][1] == x[0][0]:
#     print("True!")
# elif len(x[0])-len(x[1])==x[2][0]:
#     print("False!")
# elif sum(x[2])%2==0:
#     print("maybe!")
# else:
#     print("None!")
#
# #132
# x = [list(range(5)),list(range(5,9)),list(range(1,10,3))]
# if sum(x[0][-3:]) + sum(x[2][-3:]) == sum(x[1][-3:]):
#     print("True!")
# elif len(x[0])*2<sum(x[2]):
#     print("False")
#
#
# #133
# x = {1: "python", 2: "java", 3: "javascript", 4: "ruby", 5: "perl"}
# if x[1][1] in x[4]:
#     print("True!")
# else:
#     print("False!")
#
# x = {1: "python", 2: "java", 3: "javascript", 4: "ruby", 5: "perl"}
# if x[3][-2]==x[5][0]:
#     print("True!")
# else:
#     print("False!")
#
# #134
# x = {1: "python", 2: "java", 3: "javascript", 4: "ruby", 5: "perl"}
# if len(min(x.values()))==x[4].count("a"):
#     print("True!")
# else:
#     print("False!")
#
# #135
# x = {1: "python", 2: "java", 3: "javascript", 4: "ruby", 5: "perl"}
# if sum(x)<len(x[1]+x[2]+x[3]+x[4]+x[5]):
#     print("True!")
# else:
    #print("False!")


#LOOPS-:
#136
# x= [1,2,3,5,7,8,9,0,4,3]
# for i in x:
#     print(i)
#137
# x= [1,2,3,5,7,8,9,0,4,3]
# for i in x:
#     print(i%3)

#138
# x= [1,2,3,5,7,8,9,0,4,3]
# for i in sorted(x,reverse=True):
#     print(i*10)
#
# #139
# x= [1,2,3,5,7,8,9,0,4,3]
# for i in x:
#     print(i/2)
# else:
#     print("Great job")

#140
# x= [1,2,3,5,7,8,9,0,4,3]
# for i in x:
#     print(x.index(i))

#141
# x=0
# while x <= 5:
#     print(x**2)
#     x = x+1

#142
# x=0
# while x <= 4:
#     print(x*10)
#     x = x+1
# else:
#     print("Done!")
#
# #143
#
# x=10
# while x <= 15 and x % 5== 0:
#     print(x+10)
#     x = x+1

#144
# x=-7
# while x < 0:
#     print(abs(x))
#     x = x+1

#145
# x=5
# y=2
# while x>=5 and x<10:
#     print(x*y)
#     x = x+1
# else:print(x/y)

#146
# x= [1,2,3,5,7,8,9,0,4,3]
# for i in x:
#     if i<9:
#      print(i*10)
#
#147
# x=[2,3,4]
# y=[3,5]
# for i in x:
#     for j in y:
#         print(i*j)

# #148
# x=[2,3,4]
# y=[3,5,4,20]
# for i in x:
#     for j in y:
#         if j <12:
#            print(i*j)

#149
# x=[2,3,4]
# y=[3,5,4,20]
# for i in x:
#     for j in y:
#         if i>5 and j>12:
#            print(i*j)
#
# #150
# x=[2,3,4]
# y=[3,5,4,20]
# for i in x:
#     for j in y:
#         if j <=10:
#            print(i*j)
#         else:
#             print(i*j ** 2)




#add key in nested dict
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# }
# def add_key_value(student_data):
#     new_key_value={'adress':2}
#     for i in student_data:
#         student_data[i]['adress']='jaipur'
#     return student_data
# print(add_key_value(student_data))


# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# }
# # #duplicate kite baar aaya h
# def remove_duplicate(student_data):
#     new_dict={}
#     for key,value in student_data.items():
#         if value not in new_dict.values():
#             new_dict[key]=value
#     return new_dict
# print(remove_duplicate(student_data))
#
#
#
#
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# }
# def duplicate_count(student_data):
#     duplicate_count=0
#     for key,value in student_data.items():
#         for duplicate_count in student_data:
#             duplicate_count+=0
#     return duplicate_count
# print(duplicate_count(student_data))
#
# #
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# }
# #def duplicate_name(student_data):
# duplicate={}
# result={}
# for key ,value in student_data.items():
#     if value not in result.values():
#         result[key]=value
#     else:
#         duplicate[key]=value
#     #return result,duplicate
# print(result)
# print(duplicate)

# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# }
# def duplicate_count(input_dict):
#     duplicate_count=0
#     check_dict=[]
#     result={}
#     for key,value in input_dict.items():
#         value_list=list(value.items())
#         if value not in result.values():
#             result[key] = value
#         if value_list in check_dict:
#             duplicate_count += 1
#         else:
#             check_dict.append(value_list)
#             result[key]=value
#
#     return duplicate_count,result
# duplicates=duplicate_count(input_dict=student_data)
# print(duplicates)

# duplicate={}
# result={}
# for key ,value in student_data.items():
#     if value not in result.values():
#         result[key]=value
#     else:
#         duplicate[key]=value
#     #return result,duplicate
# print(result,'\n',duplicate)