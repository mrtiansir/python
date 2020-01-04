"""
print("QYTANG' day 2014-9-28")

word = "scallywag"
sub_word = word[2:6]
print(sub_word)

word1 = input("Please Input Your Word: ")
first_c = word1[0]
else_c = word1[1:]
print(else_c + "-" + first_c + "y")
"""

department1 = "Security"
department2 = "Python"
depart1_m = "cq_bomb"
depart2_m = "qinke"
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

#line1 = "%s:%-15s %s:%-10s %s:%-15.2f The End!" % ("Department1 name",department1,"Manager",depart1_m,"COURSE_FEES",COURSE_FEES_SEC)
#line2 = "%s:%-15s %s:%-10s %s:%-15.2F The End!" % ("Department2 name",department2,"Manager",depart2_m,"COURSE_FEES",COURSE_FEES_Python)

line1 = "{0:s}{1:<15s}{2:s}{3:<10s}{4:s}{5:<15.2f} The End!".format("Department1 name:",department1,"Manager:",depart1_m,"COURSE_FEES:",COURSE_FEES_SEC)
line2 = "{0:s}{1:<15s}{2:s}{3:<10s}{4:s}{5:<15.2f} The End!".format("Department2 name:",department2,"Manager:",depart2_m,"COURSE_FEES:",COURSE_FEES_Python)

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)

