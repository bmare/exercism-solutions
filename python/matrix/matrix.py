class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix_string = [item.split() for item in self.matrix_string.splitlines()]
        self.matrix_string = [[int(item) for item in self.matrix_string[nestedList]] for nestedList in range(len(self.matrix_string))]
    def row(self, index):
        return self.matrix_string[index-1]
    def column(self, index):
        column=[self.matrix_string[item][index-1] for item in range(len(self.matrix_string))]
        return column
