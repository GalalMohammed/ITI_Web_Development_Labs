def longest_ordered_alpha(msg):
    if not msg:
        return None
    ordered_alpha = [[msg[0]]]
    for c in msg[1:]:
        if c > ordered_alpha[-1][-1]:
            ordered_alpha[-1].append(c)
        else:
            ordered_alpha.append([c])
    max_sub = ordered_alpha[0]
    for l in ordered_alpha[1:]:
        if len(l) > len(max_sub):
            max_sub = l
    return "".join(max_sub)


print(longest_ordered_alpha(input()))
