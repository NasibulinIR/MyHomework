def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for element in range(1, len(array)):
        if array[element] < smallest:
            smallest = array[element]
            smallest_index = element
    return smallest_index

def selection_sort(array):
    sorted_array = []
    for element in range(len(array)):
        smallest = find_smallest(array)
        sorted_array.append(array.pop(smallest))
    return sorted_array

def quick_sort(array):
    if len(array) < 2:
        return array

    first, middle, last = array[0], array[len(array) // 2], array[-1]
    if (first < middle < last) or (last < middle < first):
        pivot = middle
    elif (middle < first < last) or (last < first < middle):
        pivot = first
    else:
        pivot = last

    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    result = quick_sort(left) + middle + quick_sort(right)
    return result


my_list = [4, 2, 6, 5, 1, 3]

print(quick_sort(my_list))
print(selection_sort(my_list))