x=int(input("Enter Number 1 : "))
y=int(input("Enter Number 2 : "))
print("If you want to Add - enter 1")
print ("If you want to Subtract - enter 2")
print("If you want to Multiply - enter 3")
print("If you want to Divide - enter 4")
a=int(input("Enter your choice : "))
if a==1:
    print(x+y)
elif a==2:
    print(x-y)
elif a==3:
    print(x*y)
elif a==4:
    print(x/y)
else :
    print("invalid choice")