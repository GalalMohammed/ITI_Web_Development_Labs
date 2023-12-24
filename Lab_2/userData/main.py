import re


while True:
    name = input("Enter Your Name:")
    f = True
    if name:
        for c in name:
            if f and not c.isalpha():
                print("Enter a right name")
                f = False
        if f:
            break
    else:
        print("Enter a right name")
while True:
    email = input("Enter Your email:")
    email = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", email)
    email = email[0] if email else None
    if email:
        break
    else:
        print("Enter a right email")
print(f"Your Name: {name}\nYour Email: {email}")
