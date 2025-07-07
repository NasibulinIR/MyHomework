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

my_list = [4, 2, 6, 5, 1, 3]
print(selection_sort(my_list))