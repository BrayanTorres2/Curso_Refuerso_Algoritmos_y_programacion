from array_clase import Array
import random


class Grid():
    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value=fill_value)

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "

            result += "\n"

        return str(result)

    def random_fill(self, min, max):
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                self[i][j] = random.randint(min, max)
