_PlaneT = ['mercury', 'venus', 'earth', 'mars',
           'jupiter', 'saturn', 'uranus', 'neptune']
pLa_ = input(
    "Enter  name of planet to find if it is inner plannet or outer planet ")

if pLa_ in _PlaneT[0:2]:

    print("It is Inner planet!!")

elif pLa_ in _PlaneT[2]:

    print("you are on earth!!")

elif pLa_ in _PlaneT[3:8]:

    print("It is outer planet")

else:
    print("you have entered wrong input.....enter name of planet!!!! ")
