formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
print(formatter.format(
    "Rick",
    "18 years old",
    "IDK what to type",
    "aa bb cc dd ee"
))
print(formatter.format(
    17+25>100,55<=50, 89*789 == 70221,
    "azesxrdctfvygbuhnijmoniue"
))