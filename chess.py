


import tkinter as tk
import chess
import random

class ChessGUI:
    piece_letters_white = {
        chess.PAWN: 'P',
        chess.ROOK: 'R',
        chess.KNIGHT: 'N',
        chess.BISHOP: 'B',
        chess.QUEEN: 'Q',
        chess.KING: 'K'
    }

    piece_letters_black = {
        chess.PAWN: 'p',
        chess.ROOK: 'r',
        chess.KNIGHT: 'n',
        chess.BISHOP: 'b',
        chess.QUEEN: 'q',
        chess.KING: 'k'
    }

    def __init__(self, root):
        self.root = root
        self.root.title("لعبة الشطرنج - بدون صور")

        self.board = chess.Board()
        self.square_size = 60

        self.canvas = tk.Canvas(root, width=8*self.square_size, height=8*self.square_size)
        self.canvas.pack()

        self.selected_square = None

        self.draw_board()
        self.draw_pieces()

        self.canvas.bind("<Button-1>", self.click)

    def draw_board(self):
        self.canvas.delete("square")
        colors = ["#F0D9B5", "#B58863"]  # بيج وبني
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                x1 = col * self.square_size
                y1 = row * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="square")

    def draw_pieces(self):
        self.canvas.delete("piece")
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                row = 7 - chess.square_rank(square)
                col = chess.square_file(square)
                x = col * self.square_size + self.square_size // 2
                y = row * self.square_size + self.square_size // 2

                if piece.color == chess.WHITE:
                    text = self.piece_letters_white[piece.piece_type]
                else:
                    text = self.piece_letters_black[piece.piece_type]

                self.canvas.create_text(x, y, text=text, font=("Arial", 32), tags="piece")

    def click(self, event):
        col = event.x // self.square_size
        row = event.y // self.square_size
        square = chess.square(col, 7 - row)

        if self.selected_square is None:
            piece = self.board.piece_at(square)
            if piece and piece.color == chess.WHITE:
                self.selected_square = square
                self.highlight_square(square)
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.selected_square = None
                self.draw_board()
                self.draw_pieces()
                self.root.after(500, self.make_computer_move)
            else:
                self.selected_square = None
                self.draw_board()
                self.draw_pieces()

    def highlight_square(self, square):
        self.draw_board()
        self.draw_pieces()
        row = 7 - chess.square_rank(square)
        col = chess.square_file(square)
        x1 = col * self.square_size
        y1 = row * self.square_size
        x2 = x1 + self.square_size
        y2 = y1 + self.square_size
        self.canvas.create_rectangle(x1, y1, x2, y2, outline="red", width=3, tags="highlight")

    def make_computer_move(self):
        if self.board.is_game_over():
            print("انتهت اللعبة! النتيجة:", self.board.result())
            return
        move = random.choice(list(self.board.legal_moves))
        self.board.push(move)
        self.draw_board()
        self.draw_pieces()

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChessGUI(root)
    root.mainloop()
















