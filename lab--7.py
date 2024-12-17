"""n=input()
c=0
s=0
cap=[]
small=[]
L=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
l=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
for i in n:
    if i in L:
        cap.append(i)
        c+=1
for j in n:
    if j in l:
        small.append(j)
        s+=1
print(c)
print(s)
"""#2
def count(inp):
    up_co=0
    low_co=0
    for i in inp:
        if i.isupper():
            up_co+=1
        elif i.islower():
            low_co+=1
    return up_co, low_co

inp=input("Enter input=")
up,low=count(inp)
print("No of Upper case letters=",up)
print("No of lower case letters=",low)
