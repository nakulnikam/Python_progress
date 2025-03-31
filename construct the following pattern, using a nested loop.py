rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print('*', end='')
    print()  # Move this outside the inner loop

for i in range(rows - 1, 0, -1):
    for j in range(i):
        print('*', end='')
    print()  # Move this outside the inner loop