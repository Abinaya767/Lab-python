#7 upper lower count
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
