import tkinter as tk


class HaltException(Exception):
    pass


class Cell:
    def __init__(self, master=None, num=0, x=0, y=0):
        self.label = tk.Label(master, text=num, height=4, width=9)
        self.label.grid(row=y, column=x)

    def setLabel(self, num, color, x, y):
        self.label.config(text=num, bg=color)
        self.label.grid(row=y, column=x)

class Window():
    def __init__(self, sudoku, size = "630x630"):
        self.root = tk.Tk(className="SudokuSolver")
        self.root.geometry(size)
        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.tkArray = [[Cell() for i in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                self.tkArray[i][j] = Cell(self.root, sudoku[i][j], j, i)
    
    def updateCell(self, pos, num, color):
        self.tkArray[pos[0]][pos[1]].setLabel(num, color, pos[1], pos[0])

    def windowMainLoop(self):
        self.root.mainloop()

    def update(self):
        self.root.update_idletasks()

    def onClosing(self):
        self.root.destroy()
        raise HaltException