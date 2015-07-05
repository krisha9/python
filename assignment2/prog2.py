x = int(input("enter a number to check if the number is prime or not"))
for i in range(2, int(x/2)):
    if(x % i == 0):
        print("number is not a prime ")
        break
    else:
        print("number is a prime ")
        break
