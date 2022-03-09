from random import shuffle

from sympy import E

from chess_assets.piece import ChessPiece
from .chess_assets.bishop import Bishop
from .chess_assets.king import King
from .chess_assets.knight import Knight
from .chess_assets.pawn import Pawn
from .chess_assets.queen import Queen
from .chess_assets.rook import Rook

class ChessGame: # En Passante not implemented
    
    def __init__(self, userA, userB):
        self.users = [str(userA), str(userB)]
        shuffle([str(userA), str(userB)])
        self.mentionable_users = [userA, userB]
        self.turn = 1
        self.board = {}
        self.king_pos = {}
        self.initBoard()
    
    def initBoard(self): # Initializes board state
        self.board = {}
        self.king_pos = {"black":"e1","white":"e8"}
        for col in "abcdefgh":
            self.board[col+"7"] = Pawn(loc = col+"7", color = "white")
            self.board[col+"2"] = Pawn(loc = col+"2", color = "black")
        for pos in ["a1", "h1"]:
            self.board[pos] = Rook(loc = pos, color = "black")
        for pos in ["a8", "h8"]:
            self.board[pos] = Rook(loc = pos, color = "white")
        for pos in ["b1", "g1"]:
            self.board[pos] = Knight(loc = pos, color = "black")
        for pos in ["b8", "g8"]:
            self.board[pos] = Knight(loc = pos, color = "white")
        for pos in ["c1", "f1"]:
            self.board[pos] = Bishop(loc = pos, color = "black")
        for pos in ["c8", "f8"]:
            self.board[pos] = Bishop(loc = pos, color = "white")
        self.board["d1"] = Queen(loc = "d1", color = "black")
        self.board["d8"] = Queen(loc = "d8", color = "white")
        self.board["e1"] = King(loc = "e1", color = "black")
        self.board["e8"] = King(loc = "e8", color = "white")
        
    def getCurrentPlayer(self):
        return self.users[self.turn]
    
    def getOtherPlayer(self):
        return list(set(self.users)-set([self.getCurrentPlayer()]))[0]
    
    def getCurrentColor(self):
        return ["black","white"][self.turn]
    
    def getOtherColor(self):
        return ["black","white"][(self.turn+1)%2]
    
    def move(self, userA, arg1, arg2): # Makes Move, -1: Error, 1: Successful, 2: Promotion Input Required, 3: Check, 4: Draw, 5: Mate
        if self.getCurrentPlayer() != str(userA): # Wrong player making move
            return -1
        new_pos = -1
        piece = self.board.get(arg1, None)
        color = None
        if not piece: # Trying to move a blank square
            return -1
        else:
            color = piece.getColor()
            piece = piece.getPiece() 
        if piece == " king" and self.board[arg2].getPiece() == " rook":
            if arg2[0] == "a":
                self.board, new_pos = self.board[arg1].moveTo("kc")
            elif arg2[0] == "h":
                self.board, new_pos = self.board[arg1].moveTo("qc")
        else:
            self.board, new_pos = self.board[arg1].moveTo(arg2)
        if new_pos == -1: # Move invalid due to check or space was blocked by a piece
            return -1
        else:
            if piece == "king":
                self.king_pos[color] = new_pos
            if piece == " pawn" and arg2[1] in ["1","8"]: # Pawn Promotion time
                self.turn = (self.turn+1)%2
                return 2
            elif self.inCheck(self.getOtherPlayer()): # Other player in check
                if self.checkDraw(self.getOtherPlayer()):
                    self.turn = (self.turn+1)%2
                    return 5
                return 3
            elif self.checkDraw(self.getOtherPlayer()):
                return 4
    
    def updateAllPieces(self):
        for pos in self.board:
            if self.board.get(pos, None):
                self.board[pos].updateValidMoves(self.board, self.king_pos[self.board[pos].getColor()])
    
    def checkDraw(self, userA):
        pass

    def inCheck(self, userA):
        pass