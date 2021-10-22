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
    for i in range(10):
        board.print_board()
        print("turn:" + turn + " Choose a place?")
        move = input()
        x, y = place.get(move, (-1, -1))
        if x == y != -1 and board.matrix[x][y].click:
            board.matrix[x][y].value = turn
            board.matrix[x][y].click = False
            count += 1
        else:
            print('Wrong Place choose again!')
            i -= 1
            continue
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
