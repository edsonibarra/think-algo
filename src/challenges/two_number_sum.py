def twoNumberSum(array, targetSum):
    results = dict()
    for i, n in enumerate(array):
        result = targetSum - n
        if result in results:
            return [n, result]
        results[n] = True
    return []


# Solution 2 sorting the array first
def twoNumberSum(array, target_sum):
    # pointers
    left = 0
    right = len(array) - 1

    # This solution only works for sorted arrays:
    array.sort()  # Sorting in place

    while left < right:

        result_sum = array[left] + array[right]

        if result_sum == target_sum:
            return [array[left], array[right]]
        elif result_sum > target_sum:
            right -= 1
        else:
            # result_sum < target_sum
            left += 1
    return []
