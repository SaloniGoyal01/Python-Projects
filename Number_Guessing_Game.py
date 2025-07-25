import random
Computer_Num = random.randrange(1, 101)
userInput = int(input("Enter your number : "))

if userInput > Computer_Num :
    print("Computer Number", Computer_Num)
    print("Your guess number is too high")
elif Computer_Num > userInput :
    print("Computer Number", Computer_Num)
    print("Your guess number is too low")
else :
    print("Computer Number", Computer_Num)
    print("Your guess number is equal")