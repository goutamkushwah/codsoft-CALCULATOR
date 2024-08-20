def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def mult(a,b):
    return a*b
def divide(a,b):
    return a/b
a=int(input("Enter first number : "))
b=int(input("Enter scound number : "))
print("Enter your choice \n 1. addition\n .2 subtraction\n 3. multiplication\n 4. division ")
choice = int(input())
if(choice==1):
    print("addition :",add(a,b))
if(choice==2):
    print("subtract:",subtract(a,b))    
if(choice==3):
    print("multiplication : ",mult(a,b))
if(choice==4):
    print("Divison :",divide(a,b))