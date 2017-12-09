def debug_malloc(input_data):
    observed_states = []
    number_cycles = 1
    while True:
        max_block = max(input_data)
        index_max = [i for i, val in enumerate(input_data)
                     if val == max_block]
        # Reset max blocks to 0 taking ties into consideration
        input_data[min(index_max)] = 0
        next_index = min(index_max) + 1
        if next_index >= len(input_data):
            next_index = 0
        while max_block > 0:
            input_data[next_index] += 1
            max_block -= 1
            next_index += 1
            if next_index >= len(input_data):
                next_index = 0
        if input_data in observed_states:
            # PART 2 
            distance_to_first_observed = len(observed_states) -\
                                         observed_states.index(input_data)
            return number_cycles, distance_to_first_observed
        observed_states.append(list(input_data))  # list will do a deep copy
        # PART 1
        number_cycles += 1


if __name__ == '__main__':
    input_data = '14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4'
    blocks = [int(i) for i in input_data.split()]
    # PART 1 & PART 2
    part1, part2 = debug_malloc(blocks)
    print(part1, part2)  # Expected (11137, 1037)
