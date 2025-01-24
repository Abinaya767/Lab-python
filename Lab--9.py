#1
dictionary={'1':10,'2':20,'3':50}
total=sum(dictionary.values())
print(total)

#2
inp=int(input())
for i in range(1,inp+1):
    for j in range(i):
        print(i,end="")
    print()
     
