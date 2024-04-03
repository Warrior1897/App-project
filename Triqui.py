import tkinter as tk
from tkinter import messagebox

class Triqui:
    def __init__(self, master):
        self.master = master
        self.master.title("Triqui")
        self.board = [[' ']*3 for _ in range(3)]
        self.current_player = 'X'
        
        self.buttons = [[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text=' ', font=('Helvetica', 20), width=4, height=2,
                                               command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)
        
    def on_button_click(self, i, j):
        if self.board[i][j] == ' ':
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Triqui", f"¡{self.current_player} ha ganado!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Triqui", "¡Empate!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False
    
    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True
    
    def reset_board(self):
        self.board = [[' ']*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ')
        self.current_player = 'X'
        

def main():
    root = tk.Tk()
    triqui_game = Triqui(root)
    root.mainloop()

if __name__ == "__main__":
    main()