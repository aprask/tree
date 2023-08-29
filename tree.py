rows = int(input("Enter number of rows: "))
i = 0
spaces = rows - 1
hashes = rows - spaces
stump = rows - 1
while i < rows:
    for rows in range(0, rows):
        for space in range(0, spaces):
            print(" ", end="")
        for hash in range(0, hashes):
            print("#", end="")
        print()
        i += 1
        spaces -= 1
        hashes += 2
    for spaces in range(0, stump):
        print(" ", end="")
    print("#", end="")
