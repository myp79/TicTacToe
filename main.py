class Item():
    def __init__(self, value=' ', click_able=True) -> None:
        self.value = value
        self.click = click_able


class Board():

    def __init__(self) -> None:
        matrix = [
            [],
            [],
            []
        ]
        counter = 0
        for i in range(3):
            for j in range(3):
                counter += 1
                item = Item()
                item.value = str(counter)

                matrix[i].append(item)
        self.matrix = matrix

    def print_board(self) -> None:
        print(self.matrix[0][0].value + '|' +
              self.matrix[0][1].value + '|' + self.matrix[0][2].value)
        print('-+-+-')
        print(self.matrix[1][0].value + '|' +
              self.matrix[1][1].value + '|' + self.matrix[1][2].value)
        print('-+-+-')
        print(self.matrix[2][0].value + '|' +
              self.matrix[2][1].value + '|' + self.matrix[2][2].value)


def game():
    place = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
             '4': (1, 0), '5': (1, 1), '6': (1, 2),
             '7': (2, 0), '8': (2, 1), '9': (2, 2)}
    turn = 'X'
    count = 0

    board = Board()
    matrix = board.matrix
    for i in range(9):
        board.print_board()
        print("turn:" + turn + " Choose a place?")
        move = input()
        x, y = place.get(move, (-1, -1))
        if (x, y) != (-1, -1) and matrix[x][y].click:
            matrix[x][y].value = turn
            matrix[x][y].click = False
            count += 1

        if count >= 5:
            if matrix[0][0].value == matrix[0][1].value == matrix[0][2].value:
                board.print_board()
                return '%s WON! Game over!' % (turn)
            elif matrix[1][0].value == matrix[1][1].value == matrix[1][2].value:
                board.print_board()
                return '%s WON! Game over!' % (turn)
            elif matrix[2][0].value == matrix[2][1].value == matrix[2][2].value:
                board.print_board()
                return '%s WON! Game over!' % (turn)
            elif matrix[0][0].value == matrix[1][0].value == matrix[2][0].value:
                board.print_board()
                return '%s WON! Game over!' % (turn)
            elif matrix[0][1].value == matrix[1][1].value == matrix[2][1].value:
                board.print_board()
                return '%s WON! Game over!' % (turn)
            elif matrix[0][2].value == matrix[1][2].value == matrix[2][2].value:
                board.print_board()
                return '%s WON! Game over!' % (turn)
            elif matrix[0][0].value == matrix[1][1].value == matrix[2][2].value:
                board.print_board()
                return '%s WON! Game over!' % (turn)
            elif matrix[2][0].value == matrix[1][1].value == matrix[0][2].value:
                board.print_board()
                return '%s WON! Game over!' % (turn)

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    board.print_board()
    return 'draw! Game over!'


print(game())
