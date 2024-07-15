# You are playing a game where you get to collect different antique
# items through your gameplay which are then used in the trade shop
# to upgrade your character.
# In order to make the game balance, the creator has set a cooldown
# time for each antique item. That means, once you collect an antique
# item, you can use it in trade shop only after the cooldown time.
# You have collected N antique items in order. Each upgrade costs K
# 'consecutive' antique items from your collection and each antique
# item can only be used once. You want to know how long you have to
# wait to make M upgrades to your character.
# Given N integers, where the ith integer represents the cooldown time
# of ith antique item you have collected, and two integers M and K,
# where M represents the number of upgrades you want to make and K
# represents the number of consecutive antique items you have to
# trade for each upgrade.
# Write a program to print the minimum time you have to wait to make
# M upgrades. Print -1, if M upgrades are not possible.
# Note: When you pick K consecutive antique items to trade from the
# middle of your collection, after trading, the space used to store them
# remains empty and is not merged by remaining items in the left part
# and right part.
# Input
# First line contains a single integer N.
# Second line contains N space-separated integers representing the
# cooldown time of N antique items in order.
# Third line contains two space-separated integers M and K.
# Output
# Print a single integer based on the above context.
# Explanation
# In Sample Input 1, you have to pick only one antique item for each
# upgrade. The minimum time you have to wait is when you pick the
# items whose cooldown time is 1, 2, 3. So, the output is 3.
# In Sample Input 2, you have to pick three consecutive items for each
# upgrade. So, it takes a minimum of nine antique items for M upgrades.
# As N is exactly nine, there is only one possible way of trading, and the
# minimum time it takes for M upgrades is the maximum of given
# cooldown times. So, the output is 15.
# Constraints
# 1 <= N <= 10^5
# 1 <= cooldownTime <= 10^8
# 1 <= M <= 10^6
# 1 <= K <= N.
# Sample Input 1
# 5
# 1 5 3 4 2
# 3 1
# Sample Output 1
# 3
# Sample Input 2
# 9
# 5 5 2 5 10 4 8 15 1
# 3 3
# Sample Output 2
# 15
# This question is asked in following companies
# Google.

INT_MAX = 2 ** 31 -1


def possible_upgradation(cooldown_arr, n, mid, m, k):
    antique = 0
    upgrade = 0
    flag = 0
    for i in range(n):
        if cooldown_arr[i] <= mid:
            antique += 1
        else:
            antique = 0

        if antique == k:
            upgrade += 1
            antique = 0
    if upgrade >= m:
        flag = 1
    return flag

def min_cooldown(cooldown_arr, n, m, k):
    if m * k > n:
        return -1

    start = 0
    end = INT_MAX

    while(start < end):
        mid = start + (end - start)
        if possible_upgradation(cooldown_arr, n, mid, m, k):
            end = mid
        else:
            start = mid + 1
    return end


if __name__ == "__main__":
    n = int(input())
    cooldown_arr = [int(i) for i in input().split()][:n]
    m, k = map(int, input().strip().split())
    min_cooldown_time = min_cooldown(cooldown_arr, n, m, k)
    print(min_cooldown_time)