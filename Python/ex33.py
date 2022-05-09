i = 0
numbers = []

def while_function(i,add):
    while i < 6:
        print("At the top i is",i)
        numbers.append(i)
        
        i = i + add
        print("Numbers now: ", numbers)
        print("At the bottom i is",i)


while_function(i,1)
print("The numbers:")

for num in numbers:
    print(num)
    
while_function(3,3)
print("The numbers:")

for num in numbers:
    print(num)

def for_loop(max, step):
    i = 0
    numbers = []
    for i in range(0, max, step):
        print("At the top i is %d" % i)
        numbers.append(i)

        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)
    return numbers 

numbers = for_loop(1000,500)
print("The number: ")

for num in numbers:
    print(num)