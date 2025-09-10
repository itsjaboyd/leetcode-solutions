import typing

# Intuition

# Since the sum of two integers equals the target, we can utilize the target
# subtracting one of the integers to get the other integer, which was key in
# finding the other additive in linear time.

# Approach
# Looping through the nums list, we can immediately figure out what the other
# integer should be, so we need to continue saving the index in nums and its
# value for lookup. Once we have the current value and its calculated other
# additive found in lookup, return the two indeces since there can only be one
# solution within the nums list.

# Time Complexity
# Since we use a dictionary (hash table) lookup, the algorithm runs in linear
# (O(n)) time to loop through the nums list to find the indece.

# Space complexity:
# Saving the lookup table just requires a hash table of the nums list, saving
# its value and its index, which requires O(n) space complexity as well.


def twoSum(nums: list[int], target: int) -> list[int]:
    lookup = {}
    for i in range(len(nums)):
        found = lookup.get(target - nums[i])
        if found is not None:
            return [i, found]
        lookup[nums[i]] = i


def main():
    nums = [3, 2, 4]
    target = 6
    result = twoSum(nums, target)
    print(result)


if __name__ == "__main__":
    main()
