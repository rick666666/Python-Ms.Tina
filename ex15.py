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
txt.close()
#tell user input what file is next
print ("Type the filename again:")
#let user input what file is next
file_again = input("> ")
#open the file and print the file. 
txt_again = open(file_again) 
print (txt_again.read())
txt_again.close()
print ("Type the filename again:")
txt_again = open(file_again) 
print (txt_again.read())
txt_again.close()
# the content in the file will not print twice
# using argument can also be away, and it run faster, but input can tell user what you want them to put in. 