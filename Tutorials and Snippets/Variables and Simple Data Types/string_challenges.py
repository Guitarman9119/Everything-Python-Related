def name_swap(name_string):
    """
    Given the string name string of the form "first last", return 
    the string "Last First" where both names are now capitalized
    """
    
    (first, last) = name_string.split(" ")
    return last.capitalize() + " " + first.capitalize()
    
# Tests

print(name_swap("vernon peens"))
#print(name_swap("scott rixner"))
#print(name_swap("john greiner"))


# Output

#Peens Vernon