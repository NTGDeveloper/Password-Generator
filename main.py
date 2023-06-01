# Password Generator by Chaney Goldstein
# Tip: Run the program and select v2 to run the "version2.py"
# If you run v1, that will use the function within this "main.py" file.

# Init

import random


# Function
def password_generator(length):
  uppercase_letter_1 = chr(random.randint(65, 90))
  uppercase_letter_2 = chr(random.randint(65, 90))
  lowercase_letter_1 = chr(random.randint(97, 122))
  lowercase_letter_2 = chr(random.randint(97, 122))
  digit_1 = random.randint(0, 9)
  digit_2 = random.randint(0, 9)
  punctuation_sign_1 = chr(random.randint(38, 47))
  punctuation_sign_2 = chr(random.randint(38, 47))
  random_digit_1 = ""
  random_digit_2 = ""
  random_digit_3 = ""
  random_digit_4 = ""
  scrambled_password = ""
  if length >= 9:
    random_digit_1 = chr(random.randint(33, 122))
  if length >= 10:
    random_digit_2 = chr(random.randint(33, 122))
  if length >= 11:
    random_digit_3 = chr(random.randint(33, 122))
  if length >= 12:
    random_digit_4 = chr(random.randint(33, 122))

  unscrambled_password = (uppercase_letter_1 + uppercase_letter_2 +
                          lowercase_letter_2 + lowercase_letter_1 +
                          str(digit_1) + str(digit_2) + punctuation_sign_1 +
                          punctuation_sign_2 + str(random_digit_1) +
                          str(random_digit_2) + str(random_digit_3) +
                          str(random_digit_4))
  scrambled_password_list = random.sample(unscrambled_password,
                                          len(unscrambled_password))
  for i in scrambled_password_list:
    scrambled_password += i
  return scrambled_password


print("Welcome to Chaney's Password Generator!\n\n")
genmode = input("Would you like to use v1 or v2?\n>> ")
if genmode == "v2":
  import version2
else:
  password_length = int(input(
    "\nHow long would you like your generated password to be?\n(between 8-12 characters)\n>> "
    ))
  print("\n\nYour generated pasword is:\n" +  password_generator(password_length))