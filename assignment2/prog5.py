
ge_N = (input("please describe your gender 'male' or 'female'"))
sAl_ = int(input("enter your current salary"))

if(ge_N == 'male' and sAl_ < 1000):
    bonus = (sAl_ * (5 / 100))
    print("you are getting bonus of 5%")
    print(" bonus ", bonus)

elif(ge_N == 'female' and sAl_ < 1000):
    bonus = (sAl_ * (5.5 / 100))
    print("you are getting bonus of 5.5%")
    print("bonus:", bonus)

elif(sAl_ > 1000):
    bonus = (sAl_ * (5 / 100))
    print("you are  getting bonus of 5%")
    print("bonus:",bonus)
