from random import randint

def generate_secret(f=1, t=10):
    try:
        return randint(f,t)
    except (ValueError) as e:
        raise ValueError (f"Please inform a positive integer number. {e}")
    except Exception as e:
        raise Exception (f"Something else has happened. {e}")


def is_valid_number(g):
    try:
        guess = int(g)
        if guess < 0 or guess > 10:
            raise ValueError (f"Please inform a number from 0 to 10!!")
    except ValueError as e:
        raise ValueError (f"Please inform a positive integer number. {e}")


def guess_game():
    secret = generate_secret()
    while True:
        guess = input('Guess a number from 0 to 10: ')
        is_valid_number(guess)
        if int(guess) == secret:
            print(f"You are a genius! Secret number is {secret}!")
            break
        else:
            print(f"That was close! let's try it again...")
     
if __name__ == "__main__":
     guess_game()