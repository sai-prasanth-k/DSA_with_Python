def majority_element(num: list[int]) -> None:
    candidate = None
    count = 0

    for i in num:
        if count == 0:
            candidate = i

        count += 1 if candidate == i else -1
    return candidate


class Solution:
    n = input().split(" ")
    n_list = [int(i) for i in n]
    print(majority_element(n_list))





