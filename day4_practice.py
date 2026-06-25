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

average = total / 7
if 3000 > average:
    print(f"{name}, Your step count puts you in the sedentary category - {average:.0f} steps/day.")
elif 6000 > average:
    print(f"{name}, Your step count puts you in the lightly active category - {average:.0f} steps/day.")
elif 9000 > average:
    print(f"{name}, Your step count puts you in the moderately category - {average:.0f} steps/day.")
else:
    print(f"{name}, Your step count puts you in the highly category - {average:.0f} steps/day.")
