import re


def re_ls(arr, target):
    arr_str = ','.join(str(i) for i in arr)
    print(arr_str)
    match = re.search(r'\b{}\b'.format(target), arr_str)
    print(match)
    print(match.start())
    if match:
        result = arr_str[:match.start()].count(',')
        print(result)


arr: list[int] = [12, 112, 423, 54, 65, 474, 75, 86, 978, 52, 312]
arr.sort()
print(arr)
target = 474
re_ls(arr, target)
