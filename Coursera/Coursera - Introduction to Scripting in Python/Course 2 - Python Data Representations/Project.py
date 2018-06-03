"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between 
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    #get the length of the lines to compare if it is equal
    length_of_sentence = min(len(line2), len(line1))

    
    for index in range(length_of_sentence):
        if line1[index] != line2[index]:
            return index

    if length_of_sentence == len(line1) and length_of_sentence == len(line2) and line1 == line2: 
        return -1      # they're identical

    else:
        return length_of_sentence
        
    

print(singleline_diff("Hello World", "Hello World "))


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if "\n" in line1 or "\n" in line2:
        return ""
    if idx < 0:
        return ""
    if len(line1) < len(line2):
        if idx > len(line1):
            return ""
    if len(line2) < len(line1):
        if idx >= len(line2):
            return ""

    return line1 + "\n" + "="*idx + "^" + "\n" + line2 + "\n"

   

#lineone = "Heelo"
#linetwo = "Heero"
#print(singleline_diff_format(lineone, linetwo, singleline_diff(lineone, linetwo)))


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    line_one = lines1
    line_two = lines2
 
    if singleline_diff(line_one, line_two) >=0:
        if len(lines1) != len(lines2):
            ln_num = singleline_diff(line_one, line_two)
 
            line_one = lines1[singleline_diff(line_one, line_two)]
            line_two = lines2[singleline_diff(line_one, line_two)]
            idx_num = singleline_diff(line_one, line_two)
            return (ln_num, idx_num)
 
 
        elif len(lines1) == len(lines2):
            ln_num = singleline_diff(line_one, line_two)
 
            line_one = lines1[singleline_diff(line_one, line_two)]
 
            line_two = lines2[ln_num]
 
            idx_num = singleline_diff(line_one, line_two)
            return (ln_num, idx_num)
 
 
 
    return (IDENTICAL, IDENTICAL)

#line1 = "Ek hou van Wors"
#line2 = "Ek hou van Wors"
#line3 = "Ek hou van Wors"

#print(multiline_diff(['line1', 'line2'], ['line1', 'line2', 'line3']))
#print(multiline_diff((line1, line2) , (line1, line2 )))


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    #my_file = open(filename, 'rt')
    #my_file_text = my_file.read()
    
    lines_list = open(filename).read().splitlines()
    
    print(lines_list)
    #my_file.close()  
 
    return lines_list

#get_file_lines("test.txt")

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
   
    file_one = get_file_lines(filename1)
    file_two = get_file_lines(filename2)

    line_difference = multiline_diff(file_one, file_two)

    if line_difference == (-1,-1):

        return "No differences" "\n" 


 
    