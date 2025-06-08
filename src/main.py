import random

def game(a, b, tries):
    random_number = random.randint(a, b)
    count = 1


    print("Hello, World! I'm thinking of a number between {0} and {1}. " \
    "Try to guess it. You have {2} tries.".format(a, b, tries))

    
    while True:
        if count > tries:
            print("Sorry but you lost. You exceeded the limits of tries of {0}.".format(tries))
            return
        

        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        

        if a <= guess <= b:
            count += 1
            if guess == random_number:
                print("Congratulations! You win!")
                return
            elif guess < random_number:
                print("Too small.")
            else:
                print("Too big.")
        else:
            print("Really? The random number is between {0} and {1}. Try again.".format(a, b))


def main():
    game(1, 100, 10)


if __name__ == "__main__":
    main()
