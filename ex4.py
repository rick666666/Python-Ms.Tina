#assing cars to 100
cars = 100
#assing space_in_a_car to 4.0
space_in_a_car = 4.0
# if use 4 inseted of 4.0 it will only print out 120 but not 120.0 (let it become decimal)
#assing drivers to 30
drivers = 30
#assing passengers to 90
passengers = 90
# assing cars_not_driven to cars minus drivers
cars_not_driven = cars - drivers
#assing cars_driven = drivers
cars_driven = drivers
#assing carpool_capacity = cars_driven times space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#assing average_passengers_per_car = passengers divide by cars_driven
average_passengers_per_car = passengers / cars_driven



print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
a = 123456
b = 4.56897562
c = -1.231554
d = -a-b+c
print(a+b+c)
print(d)