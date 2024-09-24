def remove_duplicates(input_list):
    unique_list = []

    for i in input_list:
        if i not in unique_list:
            unique_list.append(i)

    return unique_list


input_list = [1, 2, 3, 2, 4, 5, 1, 3, 6]
print("Original list:", input_list)
print("after remove duplicates:", remove_duplicates(input_list))
