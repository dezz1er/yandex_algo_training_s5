def divide_ceil(dividend, divisor):
    return (dividend + divisor - 1) // divisor

def calculate_line_length(words, total_words, line_width):
    line_count = 1
    remaining_space = line_width
    idx = 0
    while idx < total_words:
        if words[idx] > line_width:
            return -1
        if words[idx] <= remaining_space:
            remaining_space -= (words[idx] + 1)
        else:
            idx -= 1
            remaining_space = line_width
            line_count += 1
        idx += 1
    return line_count

def max_papyrus_length(col1, col2, col1_words, col2_words, col1_width, col2_width):
    return max(calculate_line_length(col1, col1_words, col1_width), calculate_line_length(col2, col2_words, col2_width))

def binary_search_optimization(col1, col2, col1_words, col2_words, total_width, left, right):
    while left < right:
        midpoint = (left + right) // 2
        if calculate_line_length(col1, col1_words, midpoint) < calculate_line_length(col2, col2_words, total_width - midpoint):
            right = midpoint
        else:
            left = midpoint + 1
    return right - 1

def main():
    papyrus_width, col1_word_count, col2_word_count = map(int, input().split())
    col1_lengths = list(map(int, input().split()))
    col2_lengths = list(map(int, input().split()))

    longest_col1 = max(col1_lengths)
    longest_col2 = max(col2_lengths)

    if longest_col1 + longest_col2 == papyrus_width:
        print(max_papyrus_length(col1_lengths, col2_lengths, col1_word_count, col2_word_count, longest_col1, longest_col2))
        return

    left_bound = longest_col2
    right_bound = papyrus_width - longest_col1
    result = binary_search_optimization(col2_lengths, col1_lengths, col2_word_count, col1_word_count, papyrus_width, left_bound, right_bound)
    if result == 0:
        result += 1
    combined_length_1 = max_papyrus_length(col1_lengths, col2_lengths, col1_word_count, col2_word_count, papyrus_width - result, result)

    left_bound = longest_col1
    right_bound = papyrus_width - longest_col2
    result = binary_search_optimization(col1_lengths, col2_lengths, col1_word_count, col2_word_count, papyrus_width, left_bound, right_bound)
    if result == 0:
        result += 1
    combined_length_2 = max_papyrus_length(col1_lengths, col2_lengths, col1_word_count, col2_word_count, result, papyrus_width - result)

    print(min(combined_length_1, combined_length_2))

if __name__ == "__main__":
    main()
