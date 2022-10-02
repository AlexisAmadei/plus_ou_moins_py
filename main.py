import random

inp = input("Enter the max number: ")
random_number = random.randint(1, int(inp))
found = False
nb_tries = 0

print("Random max range is set to: " + inp)
print("----------")
while found == False:
    guess = input("What is your guess ?: ")
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
print("Game over. Play again ?")
# end while
