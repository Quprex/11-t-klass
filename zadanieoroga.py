total_length = 1000
final_zeros = 343
tape = [0] * total_length
possible_zero_counts = []
for pos in range(total_length):
    current_tape = tape.copy()
    current_tape[pos] = 1
    zeros_left = pos
    zeros_right = total_length - pos - 1
    remaining_zeros_right = final_zeros - zeros_left
    if 0 <= remaining_zeros_right <= zeros_right:
        total_initial_zeros = zeros_left + zeros_right
        possible_zero_counts.append(total_initial_zeros)
max_initial_zeros = max(possible_zero_counts)
print(max_initial_zeros)

