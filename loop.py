import random

failed_attempts = 0
plays = 0

for attempt in range(6):
    choice = input("\nPress Enter to roll the dice or type Q to quit: ")

    if choice.lower() == "q":
        break

    plays += 1

    dice = random.randint(1, 7)
    print("You rolled:", dice)
    

    if dice == 1:
        failed_attempts += 1
        print("You failed this attempt.")
    else:
        print("You passed this attempt!")

print("\n--- Game Over ---")
print("Failed attempts:", failed_attempts)
print("Times played:", plays)

if failed_attempts == 0:
    print("Excellent performance! \n great win")
elif failed_attempts <= 2:
    print("Good performance! \n you win")
else:
    print("bad performance! \n you lose")    