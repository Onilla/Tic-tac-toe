enter = " " * 9
print(f"""
---------
| {enter[0]} {enter[1]} {enter[2]} |
| {enter[3]} {enter[4]} {enter[5]} |
| {enter[6]} {enter[7]} {enter[8]} |
---------
""")
data = [[char for char in enter[i * 3: (i + 1) * 3]] for i in range(3)]
print("Enter the coordinates:")
coordinates = input()
turn = 2
def owins(x):
    if data[0][2] == data[1][1] == data[2][0] == "O" or data[0][0] == data[1][1] == data[2][2] == "O" or \
        data[0][0] == data[0][1] == data[0][2] == "O" or data[1][0] == data[1][1] == data[1][2] == "O" or \
        data[2][0] == data[2][1] == data[2][2] == "O" or data[0][0] == data[1][0] == data[2][0] == "O" or \
        data[0][1] == data[1][1] == data[2][1] == "O" or data[0][2] == data[1][2] == data[2][2] == "O":
        return True
def xwins(y):
    if data[0][2] == data[1][1] == data[2][0] == "X" or data[0][0] == data[1][1] == data[2][2] == "X" or \
        data[0][0] == data[0][1] == data[0][2] == "X" or data[1][0] == data[1][1] == data[1][2] == "X" or \
        data[2][0] == data[2][1] == data[2][2] == "X" or data[0][0] == data[1][0] == data[2][0] == "X" or \
        data[0][1] == data[1][1] == data[2][1] == "X" or data[0][2] == data[1][2] == data[2][2] == "X":
        return True
def coord_to_matrix(x, y):
    global row
    row = x - 1
    global col
    col = y - 1
for i in range(1, 10):
    try:
        coord_to_matrix(int(coordinates[0]), int(coordinates[2]))
        if data[row][col] == "X" or data[row][col] == "O":
            print("This cell is occupied! Choose another one!")
            coordinates = input()
        elif data[row][col] == " ":
            if turn % 2 == 0:
                mark = 'X'
            else:
                mark = 'O'
            data[row][col] = mark
            turn += 1
            print(f"""
---------
| {data[0][0]} {data[0][1]} {data[0][2]} |
| {data[1][0]} {data[1][1]} {data[1][2]} |
| {data[2][0]} {data[2][1]} {data[2][2]} |
---------
""")
            if xwins(data) is True:
                print("X wins")
            elif owins(data) is True:
                print("O wins")
            i += 1
            coordinates = input()
            if i >= 9:
                print("Draw")
    except ValueError:
        print("You should enter numbers!")
        coordinates = input()
    except IndexError:
        print("Coordinates should be from 1 to 3!")
        coordinates = input()


