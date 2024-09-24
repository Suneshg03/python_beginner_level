# Function to remove duplicates from a list
def remove_duplicates(input_list):
    # Create an empty list to store unique elements
    unique_list = []

    # Iterate through the input list
    for item in input_list:
        # Check if item is not already in unique_list
        if item not in unique_list:
            # If not present, add it to unique_list
            unique_list.append(item)

    return unique_list

# Test the function
input_list = [1, 2, 3, 2, 4, 5, 1, 3, 6]
print("Original list:", input_list)
print("List with duplicates removed:", remove_duplicates(input_list))
