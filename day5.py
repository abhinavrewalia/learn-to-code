while True:
    name = input("What's your name? ").strip()
    if name:
        print(f"Hello {name}, welcome to the average weekly steps calculator! ")
        break
    else:
        print("Please enter your name.")

total = 0
for i in range(7):
    while True:
        try:
            steps = int(input(f"Enter steps for day {i+1}: "))
            if 0 < steps <= 15000:
                break
            else:
                print("Your steps taken can't be in negative, zero or above 15000 for this calculation. NOTE: If you covered more than 15000 steps a day, write it as 15000.")
        except ValueError:
            print("The value of steps taken must be in digits, example - 6500. ")
    total = total + steps

def get_activity_level(average):
    if average < 3000:
        return "sedentary"
    elif average < 6000:
        return "lightly active"
    elif average < 9000:
        return "moderately active"
    else:
        return "highly active"

average = total / 7
level = get_activity_level(average)
print(f"{name}, Your step count puts you in the {level} category - {average:.0f} steps/day.")