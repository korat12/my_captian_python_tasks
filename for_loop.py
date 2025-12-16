# Function to print positive numbers
def print_positive_numbers(lst):
    positives = []

    for num in lst:
        if num > 0:
            positives.append(num)

    return positives


# Input examples
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

# Output
print("Output:", ", ".join(str(x) for x in print_positive_numbers(list1)))
print("Output:", print_positive_numbers(list2))
