import random
numbers = []
for i in range(1, 101):
    numbers += [i]
#print(f"List of All({len(numbers)}):\n {numbers}")
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
random_number = random.choice(numbers)
#print(random_number)
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty_level == "easy":
    print("You have 10 Choice left!")

    for times in range(10,0,-1):
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it right! The random number was {random_number}.")
            break
        elif times-1 == 0:
            print("Sorry. You failed!")
        elif guess > random_number:
            print("Too High!")
            print(f"You have {times - 1} Choice left!")
        elif guess < random_number:
            print("Too low!")
            print(f"You have {times - 1} Choice left!")
elif difficulty_level == "hard":
    print("You have 5 Choice left!")

    for times in range(5,0,-1):
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it right! The random number was {random_number}.")
            break
        elif times-1 == 0:
            print("Sorry. You failed!")
        elif guess > random_number:
            print("Too High!")
            print(f"You have {times - 1} Choice left!")
        elif guess < random_number:
            print("Too low!")
            print(f"You have {times - 1} Choice left!")









