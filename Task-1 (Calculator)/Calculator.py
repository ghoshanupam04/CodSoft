    #Create a Simple Calculator:
print("Enter your 1st Number:",end="")
a=int(input())
print("Enter Your 2nd Number:",end="")
b=int(input())
print("Enter Operator:",end="")
c=input()
print("Total:",end="")
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
else:
    print("Return")