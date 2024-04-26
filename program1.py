from typing import List

def smallest_missing_positive_integer(nums: List[int]) -> int:

    # Remove non-positive integers and duplicates
    nums = set(filter(lambda x: x > 0, nums))

    # If the list is empty, the smallest missing positive integer is 1
    if not nums:
        return 1

    # Find the maximum element in the list
    max_num = max(nums)

    # Check for the smallest missing positive integer
    for i in range(1, max_num + 2):
        if i not in nums:
            return i





    



  

