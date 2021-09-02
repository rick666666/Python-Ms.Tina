tabby_cat = "\tI'm tabbed in." 
persian_cat = "I'm split\non a line." 
backslash_cat = "I'm \\ a \\ cat." 
fat_cat = """ 
I'll do a list: 
\t* Cat food 
\t* Fishies 
\t* Catnip\n\t* Grass
\bfdsafds
"""
print (tabby_cat) 
print (persian_cat) 
print (backslash_cat) 
print (fat_cat)

i="fds'a"

print ("%s\r" % i)
# while True:
# for i in ["/","-","|","\\", "|"]:
#     print("%s\r"%i ),
#2. when I need to print out charecter that need to be escape. 
# %s uses the str function and %r uses the repr function 
# %r  all / " are escape