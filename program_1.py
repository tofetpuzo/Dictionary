def mean(my_list):
    """
    calculating the mean of a list
    """
    the_mean = sum(my_list) / len(my_list)
    return the_mean

print(mean([1, 4, 5]))   


# student_grades = [9.1, 8.4, 5.3]
# mysum = sum(student_grades)
# length = len(student_grades)

# mean2 = mysum / length

# print(mean2)

# import datetime
# datetime.datetime.now()

# student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
# item1 = student_grades.count(10.0)

# # to check the index from a list you can use this style 
# student_grades[1]  
# # indexing: how to get the last index of a number 
# student_grades[-1] 