
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