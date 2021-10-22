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


board = Board()
board.print_board()
