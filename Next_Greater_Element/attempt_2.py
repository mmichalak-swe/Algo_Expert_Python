# Optimal Solution
# O(n) time | O(n) space, where n is the length of the input array
# time is ~2n (max 4n) , which reduces to n
def nextGreaterElement(array):
    output = [-1 for num in array]
    stack = []

    for i in range(2 * len(array)):
        i %= len(array)

        while len(stack) > 0 and array[i] > array[stack[-1]]:
            top = stack.pop()
            output[top] = array[i]

        stack.append(i)

    return output
