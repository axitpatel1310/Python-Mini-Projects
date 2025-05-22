import random
import string

def generate_password(lenght):
    if lenght < 6:
        return "Password Must be atleast 6 character"
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(lenght))
    return password

def password_generator():
    print("Generate")
    try:
        length = int(input("Enter the length of password:"))
        print("Generated Password is: ", generate_password(length))
    except ValueError:
        print("Invalid Input")

password_generator()
