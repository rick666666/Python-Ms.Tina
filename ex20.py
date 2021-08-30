# import argv
from sys import argv
# assing script and filename to argv
script, input_file = argv
# define function print_all vith variable f
def print_all(f):
    #print file f
    print (f.read())
# define function rewind with variable f
def rewind(f):
    #Change the current file position to 0, and return the rest of the line:
    f.seek(0)
# define print_a_line with variable line_count and f
def print_a_line(line_count, f):
    # print line of line_count of file f. 
    print (line_count, f.readline())
#open the file that is name input_file = to current file. 
current_file = open(input_file)
# print First let's print the whole file: and then next line
print ("First let's print the whole file:\n")
# use the print_all function with variable current_file
print_all(current_file)
#print Now let's rewind, kind of like a tape.
print ("Now let's rewind, kind of like a tape.")
# use rewind function with variable current_file
rewind(current_file)
# print Let's print three lines:
print ("Let's print three lines:")
# set variable current_line to 1
current_line = 1
#use funciton print_a_line with variable current_line, current_file
print_a_line(current_line, current_file)
#add one to variable current_line
current_line += 1
#use funciton print_a_line with variable current_line, current_file
print_a_line(current_line, current_file)
#add one to variable current_line
current_line += + 1
#use funciton print_a_line with variable current_line, current_file
print_a_line(current_line, current_file)
def plus(a,b):
    print(a+b)

plus(1,2)
plus(2,2)
plus(3,2345)
plus(4,29786)
plus(5,2867)
plus(6,23432)
plus(7,24321)
plus(8,24321)
plus(9,4321)
plus(10,4321)