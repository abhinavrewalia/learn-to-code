name = input("What's your name? ")
print(f"Hello {name}, let's find out your marks percentage.")

total = 0
for i in range(5):
    while True: 
        try:
          marks = int(input(f"Enter marks for subject {i+1}: "))
          if 0 <= marks <= 100:
            break
          else: 
            print(f"Marks must be between 0 and 100. Please try again. ")
        except ValueError:
            print(f"Please enter your marks in digits such as - 80. ")
    total = total + marks

percentage = total / 5
print(f"Your marks percentage is {percentage}. ")