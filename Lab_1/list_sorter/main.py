arr = []
for i in range(5):
    while True:
        user_in = input()
        if user_in.isdigit():
            break
    arr.append(int(user_in))
arr.sort()
print(arr)
arr.reverse()
print(arr)
