"""
Solution - Create a function make_grade_table(names, grades_list) 
whose keys are the names in names and whose values are the
lists of grades in grades
"""


# Add code here

def make_grade_table(name_list, grades_list):
    """
    Given a list of name_list (as strings) and a list of grades
    for each name, return a dictionary whose keys are
    the names and whose associated values are the lists of grades
    """
    
    grade_table = {}
    for name, grades in zip(name_list, grades_list):
        grade_table[name] = grades
    return grade_table
        

# Tests
print(make_grade_table([], []))

name_list = ["Joe", "Scott", "John"]
grades_list = [100, 98, 100, 13], [75, 59, 89, 77],[86, 84, 91, 78] 
print(make_grade_table(name_list, grades_list))


# Output
#{}
#{'Scott': [75, 59, 89, 77], 'John': [86, 84, 91, 78], 'Joe': [100, 98, 100, 13]}

