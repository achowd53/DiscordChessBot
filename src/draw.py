import PIL
from PIL import Image

from chess_assets.piece import ChessPiece
from chess_assets.bishop import Bishop
from chess_assets.king import King
from chess_assets.knight import Knight
from chess_assets.pawn import Pawn
from chess_assets.queen import Queen
from chess_assets.rook import Rook

class ChessDraw:
    def __init__(self):
        self.image = None
        self.base = Image.open("models/board.jpg")
        self.pieces = {"black pawn": "bp", "black knight": "bh", "black king": "bk", "black bishop": "bb", "black queen": "bq", "black rook": "br",
                  "white pawn": "wp", "white knight": "wh", "white king": "wk", "white bishop": "wb", "white queen": "wq", "white rook": "wr",}
        for piece in self.pieces:
            self.pieces[piece] = Image.open("models/"+self.pieces[piece]+".png")

    def drawBoard(self, board):
        self.image = self.base.copy()
        for pos in board:
            if board.get(pos, None):
                x,y = ord(pos[0])-ord('a'), ord('8')-ord(pos[1])
                self.image.paste(self.pieces[board[pos].getName()],(55+x*123,55+y*123),self.pieces[board[pos].getName()].convert('RGBA'))
        return self.image

    def showBoard(self):
        self.image.show()



