import random
import json
import datetime

name = input("Let's play a game! What is you name: ")

secret = random.randint(1, 30)
attempts = 0


with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

    for score_dict in score_list:
        print(f'{score_dict["name"]} needed {score_dict["attempts"]} attempts on date: {score_dict.get("date")} for a number {score_dict["secret_number"]}')

while True:

    if attempts == 0:
        guess = int(input("Can you do better? Guess the secret number (between 1 and 30): "))
        attempts += 1
    else:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1
        
    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        score_list.append(
            {"name": name,"attempts": attempts, "date": str(datetime.datetime.now()), "secret_number": secret}
        )

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        break
    elif guess > secret:
        print("Your guess is wrong ... try something smaller")
    elif guess < secret:
        print("Your guess is wrong ... try something bigger")