
'''
print('"Hello" World')
print("mohammed" , "ali")
print(1+1)
print(5*"ali")
x:int = 10
v:float = 3.14
f:chr(2) = 'i'
s:bool = True
a:str = "hello"
print("x = " , x)
print(x)
x,y,z=10,4.5,'hi'
print(y)
# متغيرات
تعليقات
x = 10
v2 = float(x)
v3 = str(x)+"hi"


v1= bool(x)
print(v2)
print(v1,type(v1))
print(v2,type(v2))
print(v3,type(v3))
x = int(input("Enter a number: "))
z = int(input("Enter another number: "))
print(x+5+z)


حساب كم العمر
import datetime
x = int(input("ادخل تاريخ ميلادك : "))
z = datetime.datetime.now().year
print('عمرك الحالي هو',z-x)




x =int(input("Enter a number1: "))
y = int(input("Enter a number2: "))
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)



الاوليه
()
%
/
*
+
-





x = int(input("Enter a number: "))
if x > 0:
    print(x,"is positive")
elif x == 0:
    print(x,"is zero")
else:
    print(x,"no")
x = "hi"
i = 0
while i < 10 :
    print(x)
    i = i + 1

for i in range(10):
    print("hii")


    i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(i, "*", j, "=", i * j)
        j += 1
    i += 1

    while True:
    x = float(input("Enter a number: "))
    if x >= 90:
        print(x, "is greater than 90")

    elif x >= 85:
        print(x, "is greater than 85")

    else:
        print(x, "is less than 85")



while True:
    try:
        x = int(input("Enter a number: "))
        print(x, "is integer")
        break
    except Exception as e:
        print("no")


x= [[1,2,3],[4,5,6],[7,8,9]]
y = ((1,2,3),(4,5,6),(7,8,9))
print(x[0][1])
print(y[0][1])

x = [1,3,5]

for i in range(3):
    x[i] = input("Enter a number: ")
for i in x:
    print(i)
print(x[0:3])


x = "Ali"
print(x[1])
for i in x:
    print(i)

x = open("test.txt","r")
x.write("\nHello World\n")
x.write("Hello World\n")

x.close()


def sum(a,d):
  return a+d

print(sum(1,2))

'''


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
















