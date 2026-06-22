name = input("What's your name? ")
print(f"Hello {name}, nice to meet you! ")

while True:
    try:
        year = int(input(f"What year were you born in {name}? "))
        age = 2026 - year
        if year > 2026:
            print("...you can't be born in the future... ")
        else:
            print(f"You're {age} years old, {name}. ")
            break
    except ValueError:
        print("Please enter proper credentials in digits such as- 1990.")
        