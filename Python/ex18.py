# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print ("arg1: %r, arg2: %r" % (arg1, arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print ("arg1: %r" % arg1)

# this one takes no arguments
def print_none():
    print ("I got nothin'.")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# 1. Did you start your function defi nition with def? yes
# 2. Does your function name have only characters and _ (underscore) characters? yes
# 3. Did you put an open parenthesis ( right after the function name? yes
# 4. Did you put your arguments after the parenthesis ( separated by commas? yes
# 5. Did you make each argument unique (meaning no duplicated names)? yes
# 6. Did you put a close parenthesis and a colon ): after the arguments? yes
# 7. Did you indent all lines of code you want in the function four spaces? No more, no less. yes
# 8. Did you “end” your function by going back to writing with no indent (dedenting we call it)? yes
# And when you run (“use” or “call”) a function, check these things:
# 1. Did you call/use/run this function by typing its name? yes
# 2. Did you put the ( character after the name to run it? yes
# 3. Did you put the values you want into the parenthesis separated by commas? yes
# 4. Did you end the function call with a ) character? yes