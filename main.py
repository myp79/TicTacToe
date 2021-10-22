class Item():
    def __init__(self, value=' ', click_able=True) -> None:
        self.value = value
        self.click = click_able


class Board():
    def __init__(self) -> None:
        item = Item()
        matrix = []
        for i in range(3):
            matrix.append([item]*3)
        self.matrix = matrix
