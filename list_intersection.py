def list_intersection1(list1, list2):

    # Find intercept between the two lists
    intersection_set = set(list1) & set(list2)
    
    # Convert the intercept (set) to list
    intersection_list = list(intersection_set)
    
    return intersection_list

def list_intersection2(list1, list2):

    list = []
    for item in list1:
        if item in list2:
            list.append(item)

    return list

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

result1 = list_intersection1(list_a, list_b)
result2 = list_intersection2(list_a, list_b)

print(result1)
print(result2)