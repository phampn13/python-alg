def reverse_list(input_list):
    length = len(input_list)

    ## Observed:

    # Swap list[index]  with list[length-1 - index]
    # For all indexes: 0 to length/2

    for index in range(length // 2):
        temp = input_list[index]
        input_list[index] = input_list[length - 1 - index]
        input_list[length - 1 - index] = temp

    return input_list


list = [1,2,3]

reversed_list = reverse_list(list)

print(reversed_list)