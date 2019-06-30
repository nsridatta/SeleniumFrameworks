from string import capwords
course = "Python for Programmers"
# capitalize method will capitalize only first letter in the sentence
print(course.capitalize())

for word in course.split():
    print(word.capitalize(), sep=" ")


# capwords method of string library will capitalize first letter of the words in the sentence
print("\n" + capwords(course))

print(course.__len__())

print(course.replace("Programmers", "Coders"))
print(len(course))

# Upper case method
print("Upper case of this string is "+course.upper())
# Lower case method
print("Lower case of this string is "+course.lower())
# find the location of string python in the given variable
print(course.find("Python"))
# return a boolean if the given expression is present in the given string
print("for" in course)
# RFind method returns the last index of the string occurrence
print(course.rfind("for"))


