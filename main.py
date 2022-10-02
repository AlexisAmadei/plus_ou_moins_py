import random

play_again = True

while True:
    if play_again == True:
        found = False
        nb_tries = 1
        inp = input("Enter the max number: ")
        random_number = random.randint(1, int(inp))
        print("Random max range is set to: " + inp)
        print("----------")
    while found == False:
        guess = input("What is your guess ? (type 'stop' to give up...): ")
        if guess == "stop":
            print("mystery number was " + str(random_number) + ".")
            print("See ya next time !")
            exit()
        guess = int(guess)
        if guess == random_number:
            print("You guessed it in " + str(nb_tries) + " times !")
            found = True
        if guess > random_number:
            print("Your guess is too high !")
            nb_tries += 1
        if guess < random_number:
            print ("Your guess is too low")
            nb_tries += 1
        print('----------')
    # end while
    inp = input("Play again ? Type 'yes' or 'no'\n")
    if inp == "yes":
        found = False
        play_again = True
        print("\n")
    elif inp == "no":
        break
    else:
        play_again = False
# end while
