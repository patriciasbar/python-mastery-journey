picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

fill = "."
empty = " "

for row in picture:
    for pixel in row:
        if pixel == 0:
            print(empty, end="")
        else:
            print(fill, end="")
    print("") #need a new line after every row
