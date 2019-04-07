class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.splitted_string = self.matrix_string.split("\n")

    def row(self, index):
        row = []
        for i in self.splitted_string[index-1].split(" "):
            row.append(int(i))
        return row

    def column(self, index):
        column = []
        for i in self.splitted_string:
            i = i.split(" ")
            column.append(int(i[index-1]))
        return column
