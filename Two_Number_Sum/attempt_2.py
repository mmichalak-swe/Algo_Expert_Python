# O(n) time, O(n) space

def two_number_sum(array: list[int], target_sum: int) -> list[int]:

    ans = {}

    for num in array:
        if target_sum - num in ans:
            return [num, target_sum - num]
        ans[num] = True
    return []
