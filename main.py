
#A program that omits special characters from userInput.
special_characters = (".")

def remove_spec_char():
  userInput = input()
  for c in userInput:
    if c == ".":
      print( userInput.replace('.',' ' ))
    

remove_spec_char()


