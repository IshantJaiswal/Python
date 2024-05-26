# Strings are immutable
a = "!!! Ishant !! !!!!!!!!!"
print(len(a))
print(a)
print(a.upper())
# all letters will come in upper case 


print(a.lower())
# all letters will come in lower case 


print(a.rstrip("!"))
# "rstrip" r denote from right and trip for removing that character like (!) was removed in above print line. c for center and l for left


print(a.replace("Ishant", "Ishu"))
# The replace() method replaces all occurences of a string with another string.


print(a.split(" "))
# The split() method splits the given string at the specified instance and returns the separated strings as list items.


blogHeading = "introduction tO jS"
print(blogHeading.capitalize())
# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.


str1 = "Welcome to the Console!!! hehe"
print(len(str1))
print((str1.center(20)))
# The center() method aligns the string to the center as per the parameters given by the user.


print(a.count("Harry"))
# The count() method returns the number of times the given value has occurred within the given string.

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))
# We can even also check for a value in-between the string by providing start and end index positions.


str1 = "He's name is ishu. He is an honest man."
print(str1.find("is"))
# The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
# print(str1.index("ishh"))
# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.


str1 = "WelcomeToTheConsole"
print(str1.isalnum())
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
str1 = "Welcome"
print(str1.isalpha())
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.


str1 = "hello world"
print(str1.islower())
# The islower() method returns True if all the characters in the string are lower case, else it returns False.

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False

str1 = "         "       #using Spacebar
print(str1.isspace())
# The isspace() method returns True only and only if the string contains white spaces, else returns False.

str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))
# The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())
# The title() method capitalizes each letter of the word within the string.