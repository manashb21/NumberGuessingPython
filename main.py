import random   

comp_number  = random.randint(1, 100)
#print(comp_number)

print("I challenge you to guess the number on my mind? ")
print("1st hint its between 1 and 100")


def choose_mode():
    print("Which mode? Type easy or hard")
    global comp_number
    mode = input()

    if mode.casefold() == "easy":
        chances = 10
        print("You have chosen the Easy mode.")
        logic(comp_number, chances)
    elif mode.casefold() == "hard":
        chances = 5
        print("You have chose the Hard mode.")
        logic(comp_number, chances)
    else:
        print("There is no such mode. Type again!!")
        choose_mode()

def logic(cnumb, chances):
    if chances != 0:
        print("You have {} chances left to guess.".format(chances))
        print("Enter your guess: ")
        guess = input()
        if (guess.isnumeric() == False):
            print("You didn't type a number. Type a NUMBER.")
            logic(cnumb, chances)
        else:
            number_comparer(int(guess), cnumb, chances)
    else:
        print("Your chances are over! You failed.")

def number_comparer(a, b, chances):
    if (a > b) and (abs(a-b) >= 15):
        print("Too high!")
        logic(comp_number, chances - 1)
    elif (a > b) and (abs(a-b) < 15 ):
        print("Hmm, I sense something getting closer!")
        logic(comp_number, chances - 1)
    elif (a > b) and (abs(a-b) < 5 ):
        print("Almost guessed it!")
        logic(comp_number, chances - 1)
    elif (a < b) and (abs(a-b) >= 15):
        print("Too Low!")
        logic(comp_number, chances - 1)
    elif (a < b) and (abs(a-b) < 15):
        print("You're close.")
        logic(comp_number, chances - 1)
    elif (a < b) and (abs(a-b) < 5 ):
        print("Close call...")
        logic(comp_number, chances - 1)
    elif a == b:
        print("Darn it! You must be a Psychic.")
        print("My number was ", b)


choose_mode()