# define the function of cheese_and_crackers vith variable of cheese_count, boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print "You have %d cheeses!" with variable of cheese_count
    print ("You have %d cheeses!" % cheese_count)
    #print You have %d boxes of crackers!" with variable of boxes_of_crackers
    print ("You have %d boxes of crackers!" % boxes_of_crackers)
    #print Man that's enough for a party!
    print ("Man that's enough for a party!")
    #print Get a blanket. and next line
    print ("Get a blanket.\n")

#print We can just give the function numbers directly:
print ("We can just give the function numbers directly:")
# use the function cheese_and_crackers with 20 and 30 directly
cheese_and_crackers(20, 30)

#print OR, we can use variables from our script:
print ("OR, we can use variables from our script:")
# set amount_of_cheese to 10
amount_of_cheese = 10
# set amount_of_crackers to 50
amount_of_crackers = 50

#use the funciton cheese_and_crackers with variable amount_of_cheese, amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print We can even do math inside too:
print ("We can even do math inside too:")
#use the funciton cheese_and_crackers with variable 10+20, 5+6
cheese_and_crackers(10 + 20, 5 + 6)

#print And we can combine the two, variables and math:
print ("And we can combine the two, variables and math:")
# use function cheese_and_crackers with variable amount_of_cheese plus 100 and variable amount_of_crackers plus 1000
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)