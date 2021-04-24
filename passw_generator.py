import string
from random import choice


password = ""
total_chars = int(input("how long should the password be: "))

chars = "string.ascii_letters" + "string.digits" + "string.punctuation" + " "

members = []
for _ in range(total_chars):
    members.append(choice(chars))

for s in members:
    password += s

print(password)
