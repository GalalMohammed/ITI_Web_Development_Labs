instr = input()
count = 0
for c in instr:
    if c in "aeiou":
        count += 1
print(count)
