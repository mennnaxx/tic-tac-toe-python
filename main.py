def board(b):
    for i, row in enumerate(b):
        print(" | ".join(str(x) for x in row))
        if i < 2:
            print("---------")


def check(b, player):
    for r in range(3):
        if all(b[r][c] == player for c in range(3)):
            return True
    for c in range(3):
        if all(b[r][c] == player for r in range(3)):
            return True
    if b[0][0] == player and b[1][1] == player and b[2][2] == player:
        return True
    if b[0][2] == player and b[1][1] == player and b[2][0] == player:
        return True
    return False


def play(b, player):
    try:
        choice = int(input(f"Player {player}, enter a number (1-9): ").strip())
    except ValueError:
        print("Invalid input. Enter a number from 1 to 9.")
        return False

    if not 1 <= choice <= 9:
        print("Number must be between 1 and 9.")
        return False

    row, col = (choice - 1) // 3, (choice - 1) % 3

    if b[row][col] in ("X", "O"):
        print("Cell already taken, choose another.")
        return False

    b[row][col] = player
    return True


def main():
    b = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    current = "X"
    moves = 0

    print("Tic Tac Toe — choose a number from 1 to 9")
    board(b)

    while moves < 9:
        if play(b, current):
            moves += 1
            board(b)

            if check(b, current):
                print(f"Player {current} wins!")
                return

            current = "O" if current == "X" else "X"

    print("It's a draw!")


if __name__ == "__main__":
    main()
