line = input()
state = 0
for char in line:
    if state == 0:
        if char == 'a':
            state == 1
    elif state == 1:
        if char == 'b':
            state = 2
        elif char == 'a':
            state = 1
        else:
            state = 0
    elif state == 2:
        if char == 'c':
            state = 3
        elif char == 'a':
            state = 1
        else:
            state = 0
    elif state == 3:
        if char == 'd':
            state = 4
        elif char == 'a':
            state = 1
        else:
            state = 0
    print('Substring found!' if state == 4 else 'Substring not found.')
