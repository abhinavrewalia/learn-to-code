name = input("What's your name? ")
print(f"Hello {name}, let's find out your marks percentage.")

try:
    marks = int(input("What's the sum total of marks of your five subjects? "))
    percentage = marks / 5
    if 0 <= marks <= 500:
        print(f"Your percentage calculates to {percentage}, thanks for using our service. ")
    else:
        print("The sum of marks provided is incorrect.")
except ValueError:
    print("Provide the total sum in digits. For example- 380. ")