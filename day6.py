def get_valid_number(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            else:
                print(f"Please enter a value between {low} and {high}. ")
        except ValueError:
            print(f"Please enter the value in digits. ")

def get_marks_evaluated(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

while True:    
    name = input("Please enter your student name. ").strip()
    if name:
         print(f"Let's calculate your grades and percentage, {name}. ")
         break
    else:
        print("Please enter your student name to proceed.")

total = 0
for i in range(5):
    total += get_valid_number(f"Enter your marks for subject {i+1}: ", 0, 100)

average = total / 5
grade = get_marks_evaluated(average)
print(f"Your evaluated grades and percentage are as follows- grade {grade} and {average: .2f}%. Thanks for using our services, {name}. ")