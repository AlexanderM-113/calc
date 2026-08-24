import random

def p():
    input("Press EXE...")

def game():
    print("\n" + "="*32)
    print("ROCK PAPER SCISSORS")
    print("="*32 + "\n")
    
    wins=0
    losses=0
    
    while True:
        print("Score: " + str(wins) + "-" + str(losses))
        print("1=Rock 2=Paper 3=Scissors 4=Quit\n")
        
        choice=input("Your move: ")
        
        if choice=="4":
            print("\nFinal: " + str(wins) + "-" + str(losses) + "\n")
            break
        
        if choice not in ["1","2","3"]:
            print("Invalid\n")
            continue
        
        choices=["Rock","Paper","Scissors"]
        player_choice=choices[int(choice)-1]
        cpu_choice=random.choice(choices)
        
        print("You: " + player_choice)
        print("CPU: " + cpu_choice)
        
        if player_choice==cpu_choice:
            print("TIE\n")
        elif (player_choice=="Rock" and cpu_choice=="Scissors" or
              player_choice=="Paper" and cpu_choice=="Rock" or
              player_choice=="Scissors" and cpu_choice=="Paper"):
            print("YOU WIN\n")
            wins+=1
        else:
            print("YOU LOSE\n")
            losses+=1
    
    p()

while True:
    print("\n" + "="*32)
    print("ROCK PAPER SCISSORS")
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
