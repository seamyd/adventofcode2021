counts = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
]

with open('input', 'r') as file_object:
    for line in file_object:
        for i in range(len(line.strip())):
            if line[i] == '0':
                counts[i][0] += 1
            else:
                counts[i][1] += 1


def binary_string(counts, getMax=True):
    binary_string = ''

    for digit in counts:
        min_or_max_value = max(digit) if getMax else min(digit)
        min_or_max_index = digit.index(min_or_max_value)
        binary_string += str(min_or_max_index)

    return binary_string


gamma = int(binary_string(counts), 2)
epsilon = int(binary_string(counts, False), 2)
print(f'Gamma rate: {gamma}')
print(f'Epsilon rate: {epsilon}')

print(f'Gamma X Epsilon = {gamma * epsilon}')
