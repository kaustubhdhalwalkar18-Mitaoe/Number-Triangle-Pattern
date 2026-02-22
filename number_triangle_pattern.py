# number_triangle_pattern.py

def print_number_triangle(rows):
    """
    Function to print a right-angled triangle pattern of numbers
    """
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  # Move to next line


if __name__ == "__main__":
    try:
        n = int(input("Enter the number of rows: "))
        
        if n <= 0:
            print("Number of rows must be greater than 0.")
        else:
            print("\nNumber Right-Angled Triangle Pattern:\n")
            print_number_triangle(n)

    except ValueError:
        print("Invalid input! Please enter a valid integer.")