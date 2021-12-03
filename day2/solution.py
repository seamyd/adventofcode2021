forward = 0
down = 0

with open('input', 'r') as file_object:
    for line in file_object:
        direction, amount = line.split(' ')

        if direction == 'forward':
            forward += int(amount)
        elif direction == 'down':
            down += int(amount)
        else:
            down -= int(amount)

print(f'Forward: {forward} // Down: {down} // Multiplied: {forward * down}')
