import random
def guess_Number():
        Computer = random.randint(1,100)
        attempts = 0
        print("Lets play a game")
        print("Think of any number between 1 to 100")
        while True:
                User = int(input("Enter Your guess? :"))
                attempts+=1
                if Computer == User:
                    print("Congratulations you guess the right number", Computer ,"in", attempts ,"attempts")
                    break
                elif User < Computer:
                    print("Sorry Too low! Try again")
                else:
                    print("Sorry Too high! Try again")
guess_Number()