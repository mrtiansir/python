#!/usr/bin/python3
# _*_ coding=utf-8 _*_


department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

line1 = 'Department1 name:%-10s Manager:%-10s COURSE_FEES:%-15.2f The End!' % (department1, depart1_m, COURSE_FEES_SEC)
line2 = 'Department2 name:%-10s Manager:%-10s COURSE_FEES:%-15.2f The End!' % (department2, depart2_m, COURSE_FEES_Python)

# # line1 = 'Department1 name:{:<10s} Manager:{:<10s} COURSE_FEES:{:<15.2f} The End!'.format(department1, depart1_m, COURSE_FEES_SEC)
# # line2 = 'Department2 name:{:<10s} Manager:{:<10s} COURSE_FEES:{:<15.2f} The End!'.format(department2, depart2_m, COURSE_FEES_Python)
#
# line1 = f'Department1 name:{department1:<10s} Manager:{depart1_m:<10s} COURSE_FEES:{COURSE_FEES_SEC:<15.2f} The End!'
# line2 = f'Department2 name:{department2:<10s} Manager:{depart2_m:<10s} COURSE_FEES:{COURSE_FEES_Python:<15.2f} The End!'

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)

