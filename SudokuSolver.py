from Window import Window, HaltException
import threading
from time import sleep


class SudokuSolver():
    def __init__(self, sudoku: list):
        self.window = Window(sudoku)
        self.sudoku = sudoku
        self.sudokuSide = len(sudoku)
        if self.sudokuSide % 3 != 0:
            print("It is not a valid Sudoku")
            exit()
        for i in range(self.sudokuSide):  # Is it an valid Sudoku?
            for j in range(self.sudokuSide):
                if self.sudoku[i][j] != 0 and not self.checkNum((i, j), self.sudoku[i][j]):
                    print("It is not a valid Sudoku")
                    exit()


    def checkNum(self, pos: tuple, num: int):
        for i in range(self.sudokuSide):  # Vertical and Horizontal check
            if self.sudoku[pos[0]][i] == num and pos[1] != i:
                return False
            if self.sudoku[i][pos[1]] == num and pos[0] != i:
                return False

        blockPos = ((pos[0] // 3) * 3, (pos[1] // 3) * 3)  # Calc 3x3 block start index

        for i in range(blockPos[0], blockPos[0] + 3):  # 3x3 Block Check
            for j in range(blockPos[1], blockPos[1] + 3):
                if num == self.sudoku[i][j] and (i, j) != pos:
                    return False

        return True

    def findEmptyBlock(self):  # Search for zero and return indexes
        for i in range(self.sudokuSide):
            for j in range(self.sudokuSide):
                if self.sudoku[i][j] == 0:
                    return i, j
        else:
            return None  # If there is no zero returns None

    def solve(self):
        emptyPos = self.findEmptyBlock()
        if emptyPos is None:  # If there is no zero solving process is completed
            return True
        for num in range(1, 10):  # Try numbers 1 to 10
            self.window.updateCell(emptyPos, 0, "green")
            if self.checkNum(emptyPos, num):  # If current num looks like valid
                self.sudoku[emptyPos[0]][emptyPos[1]] = num  # Change it to num
                self.window.updateCell(emptyPos, num, "white")
                if self.solve():  # Go to next empty block
                    return True
                else:  # Revert changes
                    self.sudoku[emptyPos[0]][emptyPos[1]] = 0
        self.window.updateCell(emptyPos, 0, "white")
        return False

    def printSudoku(self):  # Prints sudoku
        line = ""
        for i in range(self.sudokuSide):
            for j in range(self.sudokuSide):
                line += str(self.sudoku[i][j]) + " | "
            print("| ", end="")
            print(line)
            print("-------------------------------------")
            line = ""

    def solveAndPrint(self): # Solves and prints
        if self.solve():
            self.printSudoku()
        else:
            print("There is no solution to this")


if __name__ == "__main__":
    sudoku = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
              [5, 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 8, 7, 0, 0, 0, 0, 3, 1],
              [0, 0, 3, 0, 1, 0, 0, 8, 0],
              [9, 0, 0, 8, 6, 3, 0, 0, 5],
              [0, 5, 0, 0, 9, 0, 6, 0, 0],
              [1, 3, 0, 0, 0, 0, 2, 5, 0],
              [0, 0, 0, 0, 0, 0, 0, 7, 4],
              [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    sudokuSolver = SudokuSolver(sudoku)
    try:
        threading.Thread(target=sudokuSolver.solve).start()
        sudokuSolver.window.windowMainLoop()
    except HaltException:
        exit()