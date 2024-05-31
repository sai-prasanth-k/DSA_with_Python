import re


def iterative_linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i


def recursive_approach_linear_search(arr, current_index, target):
    if current_index < 0:
        return -1
    if arr[current_index] == target:
        return current_index
    return recursive_approach_linear_search(arr, current_index-1, target)


def re_linear_search(arr,target):
    arr_str = ','.join(str(i) for i in arr)
    match = re.search(r'\b{}\b'.format(target), arr_str)

    if match:
        result = arr_str[:match.start()].count(',')
        return result


class BasicLinearSearch:
    arr = [1, 32, 53, 65, 24, 46, 67232, 3455, 65, 4232, 313, 647, 32, 1232]
    target = 647
    arr.sort()
    current_index = len(arr)-1
    linear_search_method = iterative_linear_search(arr, target)
    recursive_linear_search_method = recursive_approach_linear_search(arr, current_index, target)
    re_linear_search_method = re_linear_search(arr,target)
    print(re_linear_search_method)
    print(recursive_linear_search_method)
    print(linear_search_method)
