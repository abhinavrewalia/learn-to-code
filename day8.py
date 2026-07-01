while True:
    name = input("Hi! Please type in your name. ").strip()
    if name:
        break
    else:
        print("Please enter your name. ")

def get_valid_weight(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            else:
                print(f"The entered value should be between {low} and {high} in unit- kilograms(kg). " )
        except ValueError:
            print("The entered value should be in digits.")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weight = {}

for day in days:
    weight[day] = get_valid_weight(f"Enter weight for {day}: ", 0, 200)

print("Your results: ")
for day, kg in weight.items():
    print(f" {day}: {kg}kg")