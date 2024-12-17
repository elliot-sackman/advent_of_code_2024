with open('day_9.txt', 'r') as input_file:
    input_data = input_file.read()
    
    files = []
    free_space = []
    for index, char in enumerate(input_data):
        # If it's odd, it's free space
        if index % 2:
            free_space.append(int(char))
        # If it's even, it's a file block
        else:
            file_id = index // 2
            files.append([file_id, int(char)])

    left_file_pointer, right_file_pointer, block_index, free_space_index, checksum = 0, len(files) - 1, 0, 0, 0

    while left_file_pointer <= right_file_pointer:
        left_file = files[left_file_pointer]
        left_file_id, left_count = left_file[0], left_file[1]

        if left_count > 0:
            checksum += left_file_id * block_index # Add value to checksum
            files[left_file_pointer] = [left_file_id, left_count-1] # Decrement the count
            block_index += 1 # Increment the block index
        else:
            # We've run out of the left file, so check free space
            num_free = free_space[free_space_index]

            # If we have free space, fill it with the right most file
            if num_free > 0:
                right_file = files[right_file_pointer]
                right_file_id, right_count = right_file[0], right_file[1]

                # If we've run out of the right most file_id, we continue
                if right_count == 0:
                    right_file_pointer -= 1 # decrement the right pointer to look at the next file block to the left
                    continue

                checksum += block_index * right_file_id # Add value to checksum
                block_index += 1 # increment the block index
                free_space[free_space_index] -= 1 # decrement free space
                files[right_file_pointer] = [right_file_id, right_count-1] # decrement the counter for the right file
            else:
                # We've run out of free space, so increment the left pointer and the free space pointer
                left_file_pointer += 1
                free_space_index += 1
    
    print('Question 1 Answer: ', checksum)

    files = []
    raw_disk = []
    for index, char in enumerate(input_data):
        if len(raw_disk) == 0:
            start = 0
        else:
            start = raw_disk[-1][2] + 1

        # If it's odd, it's free space
        if index % 2:
            end = start + int(char) - 1
            raw_disk.append(('free', start, end, -1))
        # If it's even, it's a file block
        else:
            file_id = index // 2
            end = start + int(char) - 1
            files.append([file_id, int(char)])
            raw_disk.append(('file', start, end, file_id))

    def find_and_move_file_block_to_free_space(disk, remove_file_id, insert_index):
        move_index, move_block = -1, None

        for index, block in enumerate(disk):
            file_id = block[3]
            if remove_file_id == file_id:
                move_index = index
                move_block = block
                break
        
        if move_index > -1 and move_index > insert_index and move_block:
            disk[move_index] = ('free', move_block[1], move_block[2], -1)
            return move_block
        
    for right_file_pointer in range(len(files) - 1, -1, -1):
        right_file = files[right_file_pointer]
        right_file_id, right_count = right_file[0], right_file[1]

        insert_index = -1
        for index, block in enumerate(raw_disk):
            block_type, start, end, file_id = block

            if block_type == 'free':
                length = end - start + 1
                if length >= right_count:
                    insert_index = index
                    break
        
        if insert_index > 0:
            removed_block  = find_and_move_file_block_to_free_space(raw_disk, right_file_id, insert_index)
            if removed_block:
                block_type, start, end, file_id = removed_block
                free_block_type, free_start, free_end, free_file_id = raw_disk[insert_index]
                raw_disk[insert_index] = ('free', free_start + right_count, free_end, -1)
                raw_disk.insert(insert_index, (block_type, free_start, free_start + right_count - 1, file_id))
    
    checksum = 0
    for block in raw_disk:
        block_type, start, end, file_id = block

        if block_type == 'file':
            for i in range(start, end+1):
                checksum += file_id * i
    
    print('Question 2 Answer: ', checksum)

