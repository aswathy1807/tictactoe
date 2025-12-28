import tkinter as tk
from tkinter import messagebox
import math

class TicTacToeAI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Human vs AI Tic Tac Toe")
        self.current_player = "X" 
        self.ai_player = "O"      
        self.board = [""] * 9
        
        self.buttons = []
        for i in range(9):
            btn = tk.Button(self.window, text="", font=('normal', 20), width=5, height=2,
                            command=lambda i=i: self.human_move(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def human_move(self, index):
        if self.board[index] == "" and self.current_player == "X":
            self.make_move(index, "X")
            if not self.is_game_over():
                self.window.after(500, self.ai_move) 

    def ai_move(self):
        best_score = -math.inf
        move = None
        
        
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = self.ai_player
                score = self.minimax(self.board, 0, False)
                self.board[i] = "" 
                if score > best_score:
                    best_score = score
                    move = i
        
        if move is not None:
            self.make_move(move, "O")
            self.is_game_over()

    def minimax(self, board, depth, is_maximizing):
        
        if self.check_win_logic(board, "O"): return 1
        if self.check_win_logic(board, "X"): return -1
        if "" not in board: return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if board[i] == "":
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ""
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if board[i] == "":
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ""
                    best_score = min(score, best_score)
            return best_score

    def make_move(self, index, player):
        self.board[index] = player
        color = "blue" if player == "X" else "red"
        self.buttons[index].config(text=player, fg=color)

    def check_win_logic(self, board_state, player):
        
        wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in wins:
            
            if board_state[a] == board_state[b] == board_state[c] == player:
                return True
        return False

    def is_game_over(self):
        
        if self.check_win_logic(self.board, "X"):
            messagebox.showinfo("Result", "You won!")
            self.reset()
            return True
        if self.check_win_logic(self.board, "O"):
            messagebox.showinfo("Result", "AI wins!")
            self.reset()
            return True
        if "" not in self.board:
            messagebox.showinfo("Result", "Draw!")
            self.reset()
            return True
        return False

    def reset(self):
        self.board = [""] * 9
        for btn in self.buttons:
            btn.config(text="")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    TicTacToeAI().run()