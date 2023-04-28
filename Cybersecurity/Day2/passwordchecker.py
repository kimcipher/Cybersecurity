# Regular expressions also called regex
# These are a patterns (or filters) that describes a set of strings that matches the pattern.
# In other words, a regex accepts a certain set of strings and rejects the rest.
import re 

password = "pass123"
print("password = "+str(password))

if(len(password) == 0 ):
    print("Input password")
    
elif(len(password) < 8):
    print("Password must be atleast 8 characters")

elif(len(password) > 15):
    print("Password must be less than 15 characters")

elif not re.search("[a-z]",password):
    print("Password must have atleast one small letter")

elif not re.search("[A-Z]",password):
    print("Password must have atleast one capital letter")
    
elif not re.search("[0-9]",password):
    print("Password must have atleast one number")

elif not re.search("[!@#$%&*^()]",password):
    print("Password must have atleast one symbol")

else:
    print("This password is strong")
