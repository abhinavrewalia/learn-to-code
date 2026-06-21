name = input("What's your name? ")
print(f"Hello {name}!, Nice to meet you.")
try:
    year = int(input("What year were you born? "))
    age = 2026 - year
    if age < 0:
        print("....you can't be born in the future....")
    else:
        print(f"You're {age} years old.")
except ValueError:
    print("That's not a year - type digits like 2000.")