# assign types_of_people to 10
types_of_people = 10
# format x with types_of_people
x = f"There are {types_of_people} types of people."

# assign binary with binary
binary = "binary"
# assign do_not with don't 
do_not = "don't"
# assign y Those who know {binary}(this is to make it to a variable) and those who {do_not}. with format of binary and do_not
y = f"Those who know {binary} and those who {do_not}."

# print x
print(x)
# print y
print(y)

# print I said: with format of x
print(f"I said: {x}") # 2. here
#print I aso said: '{y}' with format of y 
print(f"I also said: '{y}'") # 2. put a string inside a string

# assing hilarious to false
hilarious = False
# assing joke_evaluation with "Isn't that joke so funny?! {}" also a format at the end. 
joke_evaluation = "Isn't that joke so funny?! {}"

#print joke_evaluation with format of hilarious
print(joke_evaluation.format(hilarious))
#print joke_evaluation
print(joke_evaluation)
# assign w with This is the left side of...
w = "This is the left side of..."
# assign e with a string with a right side.
e = "a string with a right side."

#print out w and e. 
# because + is core developers of Python defined that operator.
print(w + e)