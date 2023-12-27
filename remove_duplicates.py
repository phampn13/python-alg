def remove_duplicates(input_list):
    added_set = set()

    # New list to store non-duplicates
    result_list = []

    for item in input_list:
        # if the current item is not added
        if item not in added_set:
            # Add the new item into the result_list
            result_list.append(item)

            # Mark the item is already added
            added_set.add(item)

    return result_list


list = [1, 2, 3, 1, 2, 4]

no_duplicates = remove_duplicates(list)

print(no_duplicates)