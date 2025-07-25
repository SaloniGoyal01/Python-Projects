import string    # For getting character sets like letters, digits, and symbols
import random    # For shuffling and generating random choices

# All character groups
s1 = string.ascii_lowercase   # a...z
# print(s1)
s2 = string.ascii_uppercase   # A...Z
# print(s2)
s3 = string.digits    # 0...9
# print(s3)
s4 = string.punctuation  # !@#$...
# print(s4)

#  Ask the user to enter desired password length
#  plen stands for password length.
plen = int(input("Enter your password length :"))

s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
# print(s)
# This is done to add all characters (lowercase, uppercase, digits, symbols) into one single list (s).


random.shuffle(s)
# print(s)
print("Your Password is: ")

print("".join(s[0:plen]))