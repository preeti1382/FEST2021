import random
n = random.randint(0 , 100)
guess = 5
while(guess!=0) :
    num = int(input("guess the number: "))
    if(num < n):
        print("\n your guessed number is less than the required number.. ")
    elif(num > n):
        print("\n your guessed number is greater than the required number..")
    else :
        print("\n congrats!! you guessed it right..\n")
        break
    guess -= 1
    print("\n you are left with " , guess , "guesses")
    if(guess == 0):
        print("\n game over!!!")
        print("the required number was " , n)
