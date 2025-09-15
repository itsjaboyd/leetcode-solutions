import typing

# Problem 5: Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/


# Intuition

# Since we are looking for the longest palindrome substring within a string,
# one way we could find that is analyze each character in s as the center of
# the palindrome, extending outwards from each character, and saving the
# longest palindrome as each character is analyzed.

# Approach

# For each character present in the string s, use that character as the center
# of the palindrome, and figure out what its palindrome is (one character as a
# "palindrome" in that its the same letter forwards and backwards). This only
# covers the cases where one letter is the center, so we also need to analyze
# the odd cases where two letters are the center (i.e. 'abba'). Once each
# character is analyzed, we have saved the largest palindrome found.

# Time Complexity:

# Since we are stepping through each character of s, and then stepping through
# worst case each character again in s, the time complexity of this algorithm
# is O(n^2).

# Space Complexity

# The worst case is that we have saved the entire string s if it happens to be
# a palindrome itself, so the space complexity of this algorithm is O(n).


def longestPalindrome(s: str) -> str:
    # helper function to find the palindrome around an index
    def palindrome_surround(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    substring = ""
    for index in range(len(s)):
        result_even = palindrome_surround(s, index, index)
        if len(result_even) > len(substring):
            substring = result_even
        result_odd = palindrome_surround(s, index, index + 1)
        if len(result_odd) > len(substring):
            substring = result_odd
    return substring


def main():
    s = "babad"
    result = longestPalindrome(s)
    print(result)


if __name__ == "__main__":
    main()
