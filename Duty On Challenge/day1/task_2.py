def longest_substring_length(s):
    if not s:
        return 0

    max_length = 0
    start = 0
    char_index_map = {}

    for i in range(len(s)):
        char = s[i]
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length

# Test
s = "abcabcbb"
result = longest_substring_length(s)
print(result)