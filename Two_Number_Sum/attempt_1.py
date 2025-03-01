# O(n^2) time, O(1) space

def two_number_sum(array: list[int], target_sum: int) -> list[int]:
    for i in range(len(array)):
            for j in range((i+1), len(array)):
                if array[i] + array[j] == target_sum:
                    return[array[i], array[j]]
    return[]
