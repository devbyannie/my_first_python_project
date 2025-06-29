import random
secret_number = random.randint(1,100)
print("I'm thnking of a number between 1 and 100.")
print("Can you guess what it is")

while True:
    guess_text = input ("Enter your guess:")

    try:
        guess_number = int(guess_text)
    except ValueError:
        print("Thst's not a number! Please enter a valid number.")
        continue

    if guess_number< secret_number:
        print("Tow Low!")
    elif guess_number > secret_number:
        print("Too High!")    
    else:
        print(f"Congratualtions! you guesses it! The number was {secret_number}.")
        break
