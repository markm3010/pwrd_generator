import string
import random


password = ""
total_chars = int(input("how long should the password be: "))

chars = "string.ascii_letters" + "string.digits" + "string.punctuation" + " "

members = []
random.seed()

for _ in range(total_chars):
    members.append(random.choice(chars))

[print(s, end='') for s in members]
# print(password)
