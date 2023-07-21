import random
for i in range(999):
    A= input("You want to play a game?")
    B= ("yes")
    C= ("no")
    if A==B:
        print("That's Great. Now let's play a game")
        Fruits = ["apple", "banana", "orange", "grape", "pineapple", "watermelon"]
        print(Fruits)
        D= random.choice(Fruits)
        print("Now guess any fruit from the above list :")
        E=input("Sooo What is your guess 🤨? ")
        if D==E:
            print("Congratulations! You got the right guess")
        else:
            print("Sorry You guess wrong. Better luck next time. The right answer was", D)
        
        
    elif A==C:
        print("No problem. Have a nice day!")
        break
    
    

    
        
        
