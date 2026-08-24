import random

def p():
    input("Press EXE...")

def game():
    print("\n" + "="*32)
    print("NUMBER GUESSING GAME")
    print("="*32 + "\n")
    
    low=1
    high=100
    secret=random.randint(low,high)
    guesses=0
    
    print("I picked a number 1-100")
    print("You have about 7 guesses")
    print("(7 = log2(100))\n")
    
    while guesses<10:
        guesses+=1
        print("Hint: " + str(low) + "-" + str(high))
        
        try:
            guess=int(input("Guess " + str(guesses) + ": "))
        except:
            print("Enter a number")
            continue
        
        if guess==secret:
            print("\nCORRECT!")
            print("Guesses: " + str(guesses))
            if guesses<=7:
                print("Great job!")
            elif guesses<=10:
                print("Good try!")
            else:
                print("Lucky!\n")
            p()
            return
        elif guess<secret:
            print("Too low")
            low=max(low,guess+1)
        else:
            print("Too high")
            high=min(high,guess-1)
    
    print("\nGAME OVER")
    print("Number was: " + str(secret) + "\n")
    p()

while True:
    print("\n" + "="*32)
    print("GUESSING GAME")
    print("="*32 + "\n")
    print("1 = Play")
    print("2 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        game()
    elif ch=="2":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
