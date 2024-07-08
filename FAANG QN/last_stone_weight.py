class Solution:
    stones = [1, 3, 5, 6, 7, 8, 32, 12, 43]

    def remove_lastStone(stones):
        largest_i = stones.index(max(stones))
        return stones.pop(largest_i)
    result = remove_lastStone(stones)
    print(result)