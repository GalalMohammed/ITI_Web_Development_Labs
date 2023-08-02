while True:
    user_in = input()
    if user_in.isdigit():
        break
print([[i * j for j in range(1, i + 1)] for i in range(1, int(user_in) + 1)])
