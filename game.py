import tkinter as tk
from tkinter import messagebox
import math
import random

class TicTacToePro:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe AI")
        self.window.configure(bg="#90abc6")  
        
        
        self.current_player = "X" 
        self.ai_player = "O"
        self.board = [""] * 9
        
        
        self.header_frame = tk.Frame(self.window, bg='#2c3e50')
        self.header_frame.pack(pady=10)
        
        self.difficulty = tk.StringVar(value="Hard")
        
        
        tk.Label(self.header_frame, text="Difficulty:", fg="white", 
                 bg='#2c3e50', font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=5)
        
        self.diff_menu = tk.OptionMenu(self.header_frame, self.difficulty, "Easy", "Medium", "Hard")
        self.diff_menu.config(bg='#34495e', fg='white', highlightthickness=0)
        self.diff_menu.pack(side=tk.LEFT)

        
        self.grid_frame = tk.Frame(self.window, bg='#34495e', padx=10, pady=10)
        self.grid_frame.pack()
        
        self.buttons = []
        for i in range(9):
            btn = tk.Button(self.grid_frame, text="", font=('Arial', 24, 'bold'), width=4, height=2,
                            bg='#ecf0f1', relief='flat', activebackground='#bdc3c7',
                            command=lambda i=i: self.human_move(i))
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)
            
        
        self.reset_btn = tk.Button(self.window, text="Restart Game", font=('Arial', 12),
                                   bg='#e74c3c', fg='white', relief='flat', command=self.reset)
        self.reset_btn.pack(pady=15)

    def human_move(self, index):
        if self.board[index] == "" and self.current_player == "X":
            self.make_move(index, "X")
            if not self.is_game_over():
                
                self.window.after(600, self.ai_move) 

    def ai_move(self):
        roll = random.random()
        diff = self.difficulty.get()
        
        
        if (diff == "Easy" and roll < 0.8) or (diff == "Medium" and roll < 0.3):
            move = self.get_random_move()
        else:
            move = self.get_best_move()

        if move is not None:
            self.make_move(move, "O")
            self.is_game_over()

    def get_best_move(self):
        best_score = -math.inf
        move = None
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = ""
                if score > best_score:
                    best_score = score
                    move = i
        return move

    def get_random_move(self):
        empty = [i for i, s in enumerate(self.board) if s == ""]
        return random.choice(empty) if empty else None

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
        color = "#b13a12" if player == "X" else "#3ea7c7" # Blue vs Orange
        self.buttons[index].config(text=player, fg=color, state="disabled", disabledforeground=color)

    def check_win_logic(self, b, p):
        
        wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b_idx, c in wins:
            if b[a] == b[b_idx] == b[c] == p:
                return True
        return False

    def is_game_over(self):
        winner_text = None
        if self.check_win_logic(self.board, "X"): winner_text = "You Win!"
        elif self.check_win_logic(self.board, "O"): winner_text = "AI Wins!"
        elif "" not in self.board: winner_text = "It's a Draw!"

        if winner_text:
            messagebox.showinfo("Game Over", winner_text)
            self.reset()
            return True
        return False

    def reset(self):
        self.board = [""] * 9
        self.current_player = "X"
        for btn in self.buttons:
            btn.config(text="", state="normal", bg="#cdbacc")

if __name__ == "__main__":
    game = TicTacToePro()
    game.window.mainloop()