# Init

import random


# Function
def password_generator(length, choice):
  unscrambled_password = []
  scrambled_password = ""
  if choice[0] == "yes" or choice[0] == "Yes":
    unscrambled_password.append(chr(random.randint(65, 90)))
    unscrambled_password.append(chr(random.randint(65, 90)))
  if choice[1] == "yes" or choice[1] == "Yes":
    unscrambled_password.append(chr(random.randint(97, 122)))
    unscrambled_password.append(chr(random.randint(97, 122)))
  if choice[2] == "yes" or choice[2] == "Yes":
    unscrambled_password.append(str(random.randint(0, 9)))
    unscrambled_password.append(str(random.randint(0, 9)))
  if choice[3] == "yes" or choice[3] == "Yes":
    unscrambled_password.append(chr(random.randint(38, 47)))
    unscrambled_password.append(chr(random.randint(38, 47)))
  if length >= 9:
    unscrambled_password.append(chr(random.randint(33, 122)))
  if length >= 10:
    unscrambled_password.append(chr(random.randint(33, 122)))
  if length >= 11:
    unscrambled_password.append(chr(random.randint(33, 122)))
  if length >= 12:
    unscrambled_password.append(chr(random.randint(33, 122)))

  random.shuffle(unscrambled_password)
  #print(unscrambled_password)
  #print(scrambled_password_list)
  for i in unscrambled_password:
    scrambled_password += i
  return scrambled_password


choices = []
password_length = int(
  input(
    "\nHow long would you like your generated password to be?\n(between 8-12 characters)\n>> "
  ))
choices.append(input("\nWould you like to use uppercase letters?\n>> "))
choices.append(input("\nWould you like to use lowercase letters?\n>> "))
choices.append(input("\nWould you like to use numbers?\n>> "))
choices.append(input("\nWould you like to use special characters?\n>> "))
print("\n\nYour generated pasword is:\n" +
      password_generator(password_length, choices))
