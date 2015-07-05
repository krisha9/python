print('''1 To 'Add' two numbers 
2 To 'Subtract' two numbers 
3 To 'Multiplication' two numbers 
4 For 'Division''')

ct = True
while ct == True:
    choice = int(input("Enter your choice.: "))
    if choice > 4:
        print("invalid choice")
    else:
        x = int(input("Enter your first no.: "))
        y = int(input("Enter the second no.: "))
        if choice == 1:
            print("The 'Addition' of both the no.s is : ", x + y)

        elif choice == 2:
            print("The 'subtraction' of  the no.s is : ", x - y)

        elif choice == 3:
            print("The multiplication of two no.s is : ", x * y)

        elif choice == 4:
            print("'Dividing' 1st no. by 2nd no. : ", x / y)

        a = input("do you wish to continue?(yes/no)")
        if a == 'yes':
            ct = True
        else:
            ct = False
