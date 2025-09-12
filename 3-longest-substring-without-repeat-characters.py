import typing

# Problem 3: Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Intuition

# Since we are looking for the longest substring in s, we can walk through each
# character in s and build the longest "current" substring, keeping track of a
# maximum length during the loop through each character of s.

# Approach

# The solution is going to require a loop through s first and foremost, but the
# key to finding the maximum length is to build a substring, and reset the
# substring if a duplicate character is found. If a duplicate is found, then
# reduce the substring to the last non-duplicate character to keep the
# substring non-repetitive.

# Time Complexity:

# Looping through s is linear, although since we are looping through substrings
# of s to find duplicates, the time complexity becomes O(n^2).

# Space Complexity:

# Since we are just keeping track of a substring of s, the space required would
# be at maximum, the length of s. Therefore, the space complexity is O(n).

def lengthOfLongestSubstring(s: str) -> int:
    substring = ""
    longest = 0
    for character in s:
        if character in substring:
            found = substring.index(character) + 1
            substring = substring[found:]
        substring += character
        longest = max(longest, len(substring))
    return longest


def main():
    s = "abcabcbb"
    result = lengthOfLongestSubstring(s)
    print(result)


if __name__ == "__main__":
    main()
