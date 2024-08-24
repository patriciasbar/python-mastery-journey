from random import randint

secret = randint(0,10)
tries = 0

while True:
    try: 
        guess = int(input('Guess a number from 0 to 10: '))
        print(secret)
        if guess == secret:
            print(f"Correct! Secret number is {secret}! You've tried {tries} times!")
            break
        elif 0 > guess > 11:
            print(f"Please inform a number from 0 to 10!!")
            tries += 1
            continue
        else:
            tries += 1
            continue
    except ValueError:
        print(f"Please raise a valid number!")
        

