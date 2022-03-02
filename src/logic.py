from random import shuffle
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
        self.in_check = -1
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
        self.board["d1"] = King(loc = "d1", color = "black")
        self.board["d8"] = King(loc = "d8", color = "white")
        self.board["e1"] = Queen(loc = "e1", color = "black")
        self.board["e8"] = Queen(loc = "e8", color = "white")
        
    def getCurrentPlayer(self):
        return self.users[self.turn]
    
    def getOtherPlayer(self):
        return list(set(self.users)-set([self.getCurrentPlayer()]))[0]
    
    def getCurrentColor(self):
        return ["b","w"][self.turn]
    
    def getOtherColor(self):
        return ["b","w"][(self.turn+1)%2]
    
    def move(self, userA, arg1, arg2): # Makes Move, -1: Error, 1: Successful, 2: Promotion Input Required, 3: Checkmate, 4: Draw
        if userA != self.getCurrentPlayer():
            return -1, None
        if self.board.get(arg1, 0) and self.board[arg1] == self.getCurrentColor() and\
        self.validateMove(arg1, arg2):
            pre_move_board = self.board
            if self.inCheck(userA):
                self.in_check = self.turn
            else:
                if self.in_check == self.turn:
                    self.in_check = -1
            self.board[arg2] = self.board[arg1]
            self.board[arg1] = None
            self.turn = (self.turn+1)%2
            if self.board[arg2][1] == "k":
                self.king_pos[self.board[arg2]] = arg2
            if self.inCheck(userA):
                self.board = pre_move_board
                return -1, None
            if self.checkDraw(self.getOtherPlayer()):
                return 4, None
            if self.inCheck(self.getOtherPlayer()) and self.checkDraw(self.getOtherPlayer()):
                if str(self.mentionable_users[1]) == self.getOtherPlayer():
                    return 3, self.mentionable_users[1]
                else:
                    return 3, self.mentionable_users[0]
            return 1, None 
        return -1, None
    
    def checkDraw(self, userA):
        pass

    def inCheck(self, userA):
        pass