from .piece import ChessPiece
from .queen import Queen
from .rook import Rook
from .knight import Knight
from .bishop import Bishop

class Pawn(ChessPiece):
    def __init__(self, loc, color):
        self.piece = " pawn"
        self.add_ep = None
        super().__init__(loc, color)

    def promotePawn(self, promoteTo, king_pos): # Promotes pawn and returns board with promoted pawn
        newPiece = None
        if promoteTo == "knight":
            newPiece = Knight(self.loc, self.color)
        elif promoteTo == "queen":
            newPiece = Queen(self.loc, self.color)
        elif promoteTo == "bishop":
            newPiece = Bishop(self.loc, self.color)
        elif promoteTo == "rook":
            newPiece = Rook(self.loc, self.color)
        newPiece.num_movements = self.num_movements
        self.board[self.loc] = newPiece
        self.board[self.loc].board = self.board
        self.board[self.loc].updateValidMoves(self.board, king_pos)
        return self.board

    def enPassante(self, pos):
        self.board[pos[2:]] = None
        if self.getColor() == "white":
            pos = pos[2]+str(int(self.loc[1])+1)
        else:
            pos = pos[2]+str(int(self.loc[1])-1)
        self.board[self.loc] = None
        self.loc = pos
        self.board[self.loc] = self 
        self.num_movements += 1
        return self.board, pos

    def updateValidMoves(self, board: dict, king_pos: str):
        self.board = board
        self.valid_moves = set()
        dir = 1 if self.getColor() == "white" else -1
        for target in [[-1,dir],[1,dir]]:
            loc = self._addToLocWithNums(self.loc, target)
            if self.board.get(loc, None) != None:
                if self.board[loc].getColor() == self.getOtherColor():
                   self.valid_moves.add(loc)
        self.valid_moves.add(self._addToLocWithNums(self.loc, [0,dir]))
        if (self.color == "black" and self.loc[1] == "7") or (self.color == "white" and self.loc[1] == "2"):
            self.valid_moves.add(self._addToLocWithNums(self.loc, [0,dir*2]))
        if self.add_ep:
            self.valid_moves.add("ep"+self.add_ep)
            self.add_ep = None
        return super().updateValidMoves(board, king_pos)
