my_list = [1, 7, 3]
print(sorted(my_list, reverse=True))


student_grade = [('Sarah', 89), ('Rebecca', 82),('Matt', 91)]
print(sorted(student_grade))
print(sorted(student_grade, key=lambda x:x[1], reverse=True))