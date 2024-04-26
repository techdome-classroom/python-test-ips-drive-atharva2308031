def longest_substring(s: str) -> int:
    """"
    Implement the function longest_substring 
    using the provided longest_substring function to find 
    the length of the longest substring without repeating characters.
    """ 
    char_index_map = {}  # Dictionary to store the index of each character
    max_length = 0  # Variable to store the maximum length of the substring without repeating characters
    start_index = 0  # Variable to store the start index of the current substring

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start_index:
            # If the current character is seen before and its index is within the current substring,
            # update the start index of the substring to the index after the previous occurrence of the character
            start_index = char_index_map[char] + 1

        # Update the index of the current character
        char_index_map[char] = i

        # Update the maximum length of the substring without repeating characters
        max_length = max(max_length, i - start_index + 1)

    return max_length
#1234



