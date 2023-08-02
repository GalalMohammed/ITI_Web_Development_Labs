def strReverser(msg):
    msg = list(msg)
    msg.reverse()
    return "".join(msg)


print(strReverser(input()))
