import random

print("Welcome!")
target_num = random.randint(0, 5)
max_tries = 5
user_tries = 0
score = 5

while True:
    print("\nRemaining attempts: %s" % (max_tries - user_tries))
    user_input = input("Guess the number (Enter 'stop' to quit): ")

    if user_input == 'stop':
        print("Maximum number of attempts reached. The secret number was %s" % target_num)
        break

    try:
        user_input = int(user_input)
    except ValueError as ex:
        print("The secret number must be a whole number and contain only digits," +
              "'%s' Not correct! Please try again." % user_input)
        continue

    user_tries += 1

    if user_tries >= max_tries:
        print("The secret number was %s" % target_num)
        break

    if target_num == user_input:
        print("Congratulations! You guessed the number.")
        print("Your score: %s" % (score * (max_tries - user_tries + 1) / (max_tries)))
        break