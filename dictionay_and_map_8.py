# Enter your code here. Read input from STDIN. Print output to STDOUT
phoneBook = {}
newNum = int(input())
for _ in range(newNum):
    name,contact=input().split()
    phoneBook[name]=contact

try:
    while(True):
        check=str(input())
        if check in phoneBook:
            print(check+"="+phoneBook[check])
        else:
            print('Not found')

except(EOFError):
    pass