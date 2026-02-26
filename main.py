
print("Options menu:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
m = int(input("Choose an option (1-5): "))

def menu(m):

    if m == 1:
        print("Addition")
        

    elif m == 2:
        print("Subtraction")

    elif m == 3:
        print("Multiplication")

    elif m == 4:
        print("Division")
    
    elif m == 5:
        print("Thank you for your time!!")

    else:
        print("Invalid Option. Please choose a number between 1 and 5.")
    return m

#Ask to the user to input 2 numbers and then print the multiplication and the division of those numbers.
# Get the first number from the user
num1 = float(input("Enter the first number: "))
# Get the second number from the user
num2 = float(input("Enter the second number: "))
# Calculate the multiplication
multiplication = num1 * num2
# Calculate the division, checking for division by zero
if num2 != 0:   
    division = num1 / num2
else:
    division = "Undefined (division by zero)"
# Print the results
print(f"The multiplication of {num1} and {num2} is: {multiplication}")
print(f"The division of {num1} by {num2} is: {division}")  