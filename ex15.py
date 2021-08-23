# import argv
from sys import argv 
# assing script and filename to argv
script, filename = argv 
#open the file of what user input
txt = open(filename) 
# print the file name that user input
print ("Here's your file %r:" % filename)
# print out the txt file
print (txt.read()) 
#tell user input what file is next
print ("Type the filename again:")
#let user input what file is next
file_again = input("> ")
#open the file and print the file. 
txt_again = open(file_again) 
print (txt_again.read())

print ("Type the filename again:")
txt_again = open(file_again) 
print (txt_again.read())

# if no raw input it will open the same file as before. 