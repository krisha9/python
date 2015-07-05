print(" 1 To 'Add' two numbers ")
print(" 2 To 'Subtract' two numbers ")
print(" 3 To 'Multiplication' two numbers ")
print(" 4 For 'Division' ")
print(" 5 For  exit program")
choice=int(input("Enter your choice.: "))
x=int(input("Enter your first no.: "))
y=int(input("Enter the second no.: "))
if choice == 1:
	print("The 'Addition' of both the no.s is : ",x+y)
elif choice== 2:
	print("The 'subtraction' of  the no.s is : ",x-y)
elif choice == 3:
	print("The multiplication of two no.s is : ",x*y)
elif choice == 4:
	print("'Dividing' 1st no. by 2nd no. : ",x/y)
else:
	print("quit")
		
	
