import random
secret_number = random.randint(0,100) #it can select any number btwn 0 - 100

print("Welcome to guess a number!")
print("I am thinking of a number between 0 and 100")

playing = "on" #use no. of attempts

while playing == "on":
    user_guess = input("make a guess: ")
    #user input is always a string
    user_guess = int(user_guess)

    if secret_number > user_guess:  #comp 7 user 6,5,4,3,2,1
        print("Guess higher")
    if secret_number < user_guess:  #comp 7 user 8,9,10
        print("Guess lower")
    if secret_number == user_guess:  #comp 7 user 7
        print("Congratulations, you have guessed correctly")
        playing = "off"
        break
