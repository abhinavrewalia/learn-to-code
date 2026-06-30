def get_valid_number(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            else:
                print(f"Marks must be between {low} and {high}. Please try again. ")
        except ValueError:
            print("Please enter your marks in digits such as - 80.") 

while True:
    name = input("What's your name? ").strip()
    if name:
        print(f"Hello {name}, welcome to average marks calculator! ")
        break
    else:
        print("Please enter your name.")

marks = []
for i in range(5):
    mark = get_valid_number(f"Please enter your marks for Subject {i+1}: ", 0, 100)
    marks.append(mark)

average = sum(marks)/len(marks)
print("Here's a breakdown: ")
for mark in marks:
    print(f" - {mark}")
print(f"Marks entered: {marks}")
print(f"Average: {average: .2f}")
print(f"Highest marks: {max(marks)}")
print(f"Lowest marks: {min(marks)}")