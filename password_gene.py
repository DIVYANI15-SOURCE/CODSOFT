# ----------------------------------------
# CODSOFT Python Programming Internship
# Task 3: Password Generator
#
# Description:
# This application generates strong and secure random
# passwords using letters, numbers, and special characters.
# The user can specify the desired password length.
#
# Developed by: Devyani Verma
# ----------------------------------------
import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)