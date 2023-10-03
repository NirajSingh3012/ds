class TwoDArray:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def insert(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            print("Invalid row or column index")

    def transpose(self):
        transposed = [[0] * self.rows for _ in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                transposed[j][i] = self.data[i][j]
        self.data = transposed
        self.rows, self.cols = self.cols, self.rows

    def add(self, other_array):
        if self.rows != other_array.rows or self.cols != other_array.cols:
            print("Arrays must have the same dimensions for addition")
            return

        result = TwoDArray(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other_array.data[i][j]

        return result

    def display(self):
        for row in self.data:
            print(row)


# Example usage:
array1 = TwoDArray(3, 3)
array1.insert(0, 0, 1)
array1.insert(0, 1, 2)
array1.insert(0, 2, 3)
array1.insert(1, 0, 4)
array1.insert(1, 1, 5)
array1.insert(1, 2, 6)
array1.insert(2, 0, 7)
array1.insert(2, 1, 8)
array1.insert(2, 2, 9)

print("Array 1:")
array1.display()

array2 = TwoDArray(3, 3)
array2.insert(0, 0, 9)
array2.insert(0, 1, 8)
array2.insert(0, 2, 7)
array2.insert(1, 0, 6)
array2.insert(1, 1, 5)
array2.insert(1, 2, 4)
array2.insert(2, 0, 3)
array2.insert(2, 1, 2)
array2.insert(2, 2, 1)

print("\nArray 2:")
array2.display()

print("\nTransposing Array 1:")
array1.transpose()
array1.display()

print("\nAdding Array 1 and Array 2:")
result_array = array1.add(array2)
result_array.display()
