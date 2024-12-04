li = []

def increase_alph(str, int):
    return chr(ord(str) + int)

for i in range(26):
    li.append(increase_alph("A", i))

print(li)