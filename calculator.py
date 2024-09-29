print("Calculator")

num1= float(input("enter the first number"))
num2= float(input("enter the second number"))

print("press 1 for addition/n press 2 for subtraction/n press 3 for multiplication/n press 4 for division")

choice = int(input("enter your choice from 1-4:"))

if choice ==1:
    print("addition of given to numbers is" , num1+num2)

elif choice ==2:
    print("subtraction of given to numbers is" , num1-num2)

elif choice ==3:
    print("multiplication of given to numbers is" , num1*num2)

elif choice ==4:
    print("Division of given to numbers is" , num1/num2)

else:
    print("invalid input")    
