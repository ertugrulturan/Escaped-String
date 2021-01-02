content = "PACKET TEXT"
for i in list(content):
    s = "\\x" + format(ord(i), 'X')
    print(s)
