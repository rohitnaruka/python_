#given the code below,insert the correct methood on line 3 in order to replace all the occurrences of letter i with the substring btc
text_str = "In 2010, someone paid 10k Bitcoin for two pizzas."
s1 = "i"
s2 = "abcd"
s=text_str.split(s1)
new_str = ""
for i in s:
    if (i == ""):
        new_str += s2
    else:
        new_str += i
print(new_str)