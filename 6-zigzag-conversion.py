import typing

# Problem 6: Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion


# Intuition

# The zigzag pattern we see in the resulting string is simply alternating back
# and forth between number of the rows stated (0 -> 1 -> 2 -> 1 -> 0). This
# means that we can just create multiple lists housing our rows, loop through
# the characters of s, and combine them at the end to get the resulting string.

# Approach

# Since one row means the original string, we can just check against that and
# return it. Otherwise, we are going to alternate between the number of rows and
# add each character in s while we alternate back and forth. We must combine our
# ordered lists into one string at the end to get the final result.

# Time Complexity:

# Since the algorithm mainly just needs to loop through the characters of s to
# add them to lists, the worst case runtime would be O(n).

# Space Complexity:

# As we create lists to house the correct characters, we are at most storing n
# characters which match the number of characters in s. Therefore the space
# complexity is also O(n).


def convert(s: str, numRows: int) -> str:
    rows = {index: [] for index in range(numRows)}
    row, forward = 0, True

    # one row would mean the entire string as is.
    if numRows == 1:
        return s

    # add the characters in s to their appropriate lists.
    for index in range(len(s)):
        rows[row].append(s[index])
        forward = False if row == numRows - 1 else forward
        forward = True if row == 0 else forward
        row = row + 1 if forward else row - 1

    # combine the list parts into one conjoined string.
    result = ""
    for part in rows:
        result += "".join(rows[part])
    return result


def main():
    s = "PAYPALISHIRING"
    result = convert(s, 3)
    print(result)


if __name__ == "__main__":
    main()
