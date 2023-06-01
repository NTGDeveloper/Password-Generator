# Init

import random
import string

# Function
def password_generator(length, choice):
  characters = ""
  scrambled_password = ""
  if choice[0] == "yes" or choice[0] == "Yes":
    characters += string.ascii_uppercase
  if choice[1] == "yes" or choice[1] == "Yes":
    characters += string.ascii_lowercase
  if choice[2] == "yes" or choice[2] == "Yes":
     characters += string.digits
  if choice[3] == "yes" or choice[3] == "Yes":
     characters += string.punctuation
  for i in range(length):
    scrambled_password += random.choice(characters)

#  random.shuffle(unscrambled_password)
#  print(unscrambled_password)
#  print(scrambled_password_list)
#  for i in unscrambled_password:
#    scrambled_password += i
  return scrambled_password


choices = []
password_length = int(
  input(
    "\nHow long would you like your generated password to be?\n>> "
  ))
choices.append(input("\nWould you like to use uppercase letters?\n>> "))
choices.append(input("\nWould you like to use lowercase letters?\n>> "))
choices.append(input("\nWould you like to use numbers?\n>> "))
choices.append(input("\nWould you like to use special characters?\n>> "))
print("\n\nYour generated pasword is:\n" +
      password_generator(password_length, choices))
