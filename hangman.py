import random

def p():
    input("Press EXE...")

words=["PYTHON","CALCULATOR","GEOMETRY","ALGEBRA",
       "DERIVATIVE","PHYSICS","CHEMISTRY","BIOLOGY",
       "COMPUTER","SCIENCE","MATHEMATICS","FUNCTION"]

def game():
    print("\n" + "="*32)
    print("HANGMAN")
    print("="*32 + "\n")
    
    word=random.choice(words)
    guessed=set()
    wrong=set()
    guesses=6
    
    while guesses>0:
        display=""
        for letter in word:
            if letter in guessed:
                display+=letter+" "
            else:
                display+="_ "
        
        print(display)
        print("Wrong: " + " ".join(wrong))
        print("Guesses left: " + str(guesses) + "\n")
        
        letter=input("Guess letter: ").upper()
        
        if len(letter)!=1 or not letter.isalpha():
            print("Enter one letter\n")
            continue
        
        if letter in guessed or letter in wrong:
            print("Already guessed\n")
            continue
        
        if letter in word:
            guessed.add(letter)
            print("Correct!\n")
        else:
            wrong.add(letter)
            guesses-=1
            print("Wrong!\n")
        
        if all(l in guessed for l in word):
            print("WORD: " + word)
            print("YOU WIN!\n")
            p()
            return
    
    print("WORD: " + word)
    print("YOU LOSE!\n")
    p()

while True:
    print("\n" + "="*32)
    print("HANGMAN")
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
