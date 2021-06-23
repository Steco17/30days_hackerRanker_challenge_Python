
phoneBook = {}
newNum = int(input())
for i in range(0,newNum):
    entry = str(input()).split(" ")
    name = entry[0]
    number = int(entry[1])
    phoneBook[name] = number
    
for i in range(0, newNum):
    name = input()
    if name in phoneBook:
        print(name + "=" + str(phoneBook[name]))
    else:
        print("Not found")