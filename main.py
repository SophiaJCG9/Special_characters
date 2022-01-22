
#A program that omits special characters from userInput.
special_characters = (".")

def remove_spec_char():
  userInput = input()
  for c in userInput:
    if c == ".":
      print( userInput.replace('.',' ' ))
    

remove_spec_char()

"""
exampleStr = "Python is a general-purpose programming language."

# Look for substring in source string
if 'gene' in exampleStr:
    print("Found! The string contains the phrase 'gene'.")
else:
    print("Didn't find the substring.")
"""
