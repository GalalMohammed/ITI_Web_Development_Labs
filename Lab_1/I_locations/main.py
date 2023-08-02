user_in = input()
idx = -1
while True:
    idx = user_in.find('i', idx + 1)
    if idx < 0:
        break
    print(idx)
