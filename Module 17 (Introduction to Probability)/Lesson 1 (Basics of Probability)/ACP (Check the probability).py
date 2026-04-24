import random

def dice_roll_experiment():
    numbers = [1, 2, 3, 4, 5, 6]

    result = random.choice(numbers)

    pro = numbers.count(6) / len(numbers)
    print("Probability of getting a 6 is:", pro)

    if result == 6:
        return 'Yeah, you can begin the game'
    else:
        return "Aww snap! You didn't get a 6. Please, Roll Again."

res = dice_roll_experiment()
print(res)