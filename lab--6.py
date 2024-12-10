n=int(input())
L=[]
for i in range(n):
    L.append(int(input()))
odd=0
even=0
L1=[]
L2=[]
for j in L:
    if j%2==0:
        even+=1
        L1.append(j)
    else:
        odd+=1
        L2.append(j)
print("Number of even numbers",even)
print("Number of odd Numbers",odd)
