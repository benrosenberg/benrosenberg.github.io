# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:08:12 2021

@author: Ben Rosenberg
"""

def grade(s1, s2, s3, s4):
    total_grade =  15*max(s1/30, s2/80) 
    total_grade += 20*max(s2/80, s3/100) 
    total_grade += 30*max(s3/100, s4/100) 
    total_grade += 40*max(s4/100, ((s1/30)/7 + (s2/80)/5 + (s3/100)/3))
    return total_grade
  
def letter(grade):
    grade_listdict = [
      ( 100, "A+" ),
      ( 90 , "A"  ),
      ( 85 , "A-" ),
      ( 80 , "B+" ),
      ( 66 , "B"  ),
      ( 60 , "B-" ),
      ( 54 , "C+" ),
      ( 40 , "C"  )
    ]
    i = 0
    while grade_listdict[i][0] > grade: i += 1
    return grade_listdict[i][1]
  
grade_list = list(input("Enter the points you got on exams 1 through 3, "
                      + "and your desired percent on exam 4, separated "
                      + "by commas:\n").split(','))

for i in range(len(grade_list)):
    grade_list[i] = int(grade_list[i].strip())

s1, s2, s3, s4 = tuple(grade_list)

print(f"Your grade is: {letter(grade(s1, s2, s3, s4))}")

for i in range(101):
    print(f"Your grade is: {letter(grade(s1, s2, s3, i))} \t {i}")

