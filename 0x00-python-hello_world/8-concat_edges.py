#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str1 = str[str.index("object"):str.index("programming") + 11] + " "
str = str1 + str[str.index("with"):str.index("with")+4] + " " + str[:6]
print(str)
