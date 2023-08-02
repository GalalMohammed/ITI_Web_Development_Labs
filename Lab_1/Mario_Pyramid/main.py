while True:
    user_in = input()
    if user_in.isdigit():
        break
user_in = int(user_in)
for r in range(user_in):
    print(" " * (user_in - r - 1) + "*" * (r + 1))
