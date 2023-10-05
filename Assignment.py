# Sample data
data = [
    ("P1", "VSCode", "P23", "Eclipse", "P93", "Chrome", "P42", "JDK"),
    ("P9", "CMD", "P87", "NotePad"),
    (100, 234, 189, 9),
    (7, 23),
    ("MID", "MID", "High", "High", "High", "Low"),
]

# Function to print the table
def print_table(table):
    for row in table:
        print("\t".join(map(str, row)))

# Function to sort the table based on user's choice
def sort_table(table, sort_parameter):
    if sort_parameter == 1:
        return sorted(table, key=lambda row: row[0])
    elif sort_parameter == 2:
        return sorted(table, key=lambda row: row[2])
    elif sort_parameter == 3:
        return sorted(table, key=lambda row: row[5])
    else:
        print("Invalid sorting parameter")
        return table

# Main program
print("Original Table:")
print_table(data)

while True:
    try:
        sort_option = int(input("Enter sorting parameter [1. P_ID, 2. Start Time, 3. Priority]: "))
        if 1 <= sort_option <= 3:
            sorted_data = sort_table(data, sort_option)
            print("Sorted Table:")
            print_table(sorted_data)
            break
        else:
            print("Invalid input. Please enter a valid sorting parameter.")
    except ValueError:
        print("Invalid input. Please enter a valid sorting parameter.")
