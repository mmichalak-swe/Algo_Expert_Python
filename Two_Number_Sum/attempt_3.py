# O(n*log(n)) time, O(1) space

def two_number_sum(array: list[int], target_sum: int) -> list[int]:
    array.sort()

    left = 0
    right = len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target_sum:
            return [array[left], array[right]]
        if current_sum < target_sum:
            left += 1
        elif current_sum > target_sum:
            right -= 1

    return []
