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
    if email:
        if not email[0].isalpha():
            print("Enter a valid email")
            continue
        if not email.rfind('.') > 2:
            print("Enter a valid email")
            continue
        if not email.count('@') == 1 or not email.find('@') < email.rfind('.') or not email.rfind('.') - email.find('@') > 1:
            print("Enter a valid email")
            continue
        if email.rfind('.') == len(email) - 1:
            print("Enter a valid email")
            continue
        break
    else:
        print("Enter a right email")
print(f"Your Name: {name}\nYour Email: {email}")
