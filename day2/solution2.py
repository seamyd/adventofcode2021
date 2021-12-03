forward = 0
depth = 0
aim = 0

with open('input', 'r') as file_object:
    for line in file_object:
        direction, amount = line.split(' ')

        if direction == 'forward':
            forward += int(amount)
            depth += (int(aim) * int(amount))
        elif direction == 'down':
            aim += int(amount)
        else:
            aim -= int(amount)

print(f'Forward: {forward} // Down: {depth} // Multiplied: {forward * depth}')
