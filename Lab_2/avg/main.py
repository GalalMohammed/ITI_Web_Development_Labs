total = 0
count = 0
while True:
    user_in = input()
    if user_in == 'done':
        break
    if not user_in.isnumeric():
        print("Enter a valid number")
    else:
        total += int(user_in)
        count += 1
print(total / count if count > 0 else 0)
