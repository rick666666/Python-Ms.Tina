formatter = "{} {} {} {}" # use the format to print 4 string

print(formatter.format(1, 2, 3, 4)) # print 1234 with the format of formatter
print(formatter.format("one", "two", "three", "four")) # print 4 string with the format of formatter
print(formatter.format(True, False, False, True)) # print 4 boolean with the format of formatter
print(formatter.format(formatter, formatter, formatter, formatter)) # print 4 formatter with the format of formatter
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))# print 4 string with the format of formatter
print(formatter.format(
    "Rick",
    "18 years old",
    "IDK what to type",
    "aa bb cc dd ee"
))#print 4 string with the format of formatter


