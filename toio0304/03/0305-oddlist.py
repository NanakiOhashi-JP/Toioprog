num = int(input("Type any number: "))
li = []

for i in range(num):
    i += 1
    if i%2 != 0:
        li.append(i)

print(li)
