def find_max(list):
    if (list == None or len(list) == 0):
        raise Exception("The list must have elements")
    
    current_max = list[0]

    for current_item in list:

        # Find new max?
        if (current_item > current_max):
            current_max = current_item

    return current_max


list = [1, 2, 4, 3]

max = find_max(list)

print(max)