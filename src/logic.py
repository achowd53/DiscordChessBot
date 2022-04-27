from random import shuffle
from draw import ChessDraw

from chess_assets.piece import ChessPiece
from chess_assets.bishop import Bishop
from chess_assets.king import King
from chess_assets.knight import Knight
from chess_assets.pawn import Pawn
from chess_assets.queen import Queen
from chess_assets.rook import Rook

class ChessGame: # En Passante not implemented
    
    def __init__(self, userA, userB):
        self.users = [str(userA), str(userB)]
        shuffle(self.users)
        self.mentionable_users = [userA if self.users[0] == str(userA) else userB, userB if self.users[1] == str(userB) else userA]
        self.turn = 0
        self.board = {}
        self.king_pos = {}
        self.draw = ChessDraw()
        self.stalemate_timer = 50
        self.pieces_left = 32
        self.initBoard()
    
    def initBoard(self): # Initializes board state
        self.board = {}
        self.king_pos = {"white":"e1","black":"e8"}
        for col in "abcdefgh":
            self.board[col+"7"] = Pawn(loc = col+"7", color = "black")
            self.board[col+"2"] = Pawn(loc = col+"2", color = "white")
        for pos in ["a1", "h1"]:
            self.board[pos] = Rook(loc = pos, color = "white")
        for pos in ["a8", "h8"]:
            self.board[pos] = Rook(loc = pos, color = "black")
        for pos in ["b1", "g1"]:
            self.board[pos] = Knight(loc = pos, color = "white")
        for pos in ["b8", "g8"]:
            self.board[pos] = Knight(loc = pos, color = "black")
        for pos in ["c1", "f1"]:
            self.board[pos] = Bishop(loc = pos, color = "white")
        for pos in ["c8", "f8"]:
            self.board[pos] = Bishop(loc = pos, color = "black")
        self.board["d1"] = Queen(loc = "d1", color = "white")
        self.board["d8"] = Queen(loc = "d8", color = "black")
        self.board["e1"] = King(loc = "e1", color = "white")
        self.board["e8"] = King(loc = "e8", color = "black")
        self.updateAllPieces()
        
    def getCurrentPlayer(self):
        return self.users[self.turn]
    
    def getOtherPlayer(self):
        return self.users[(self.turn+1)%2]
    
    def getCurrentColor(self):
        return ["black","white"][self.turn]
    
    def getOtherColor(self):
        return ["black","white"][(self.turn+1)%2]
    
    def getColor(self, userA): #userA is a string
        return "black" if self.users[0] == userA else "white"

    def getPieceCount(self):
        piece_num = 0
        for pos in self.board:
            if self.board[pos] != None:
                piece_num += 1
        return piece_num

    def move(self, userA, arg1, arg2): # Makes Move, -1: Error, 1: Successful, 2: Promotion, 3: Draw, 4: Check, 5: Mate, 6: Stalemate
        if self.getCurrentPlayer() != str(userA): # Wrong player making move
            print("Wrong player making a move")
            return -1, self.mentionable_users[self.turn]
        new_pos = -1
        piece = self.board.get(arg1, None)
        color = None
        if not piece: # Trying to move a blank square
            print("Moving piece from blank square")
            return -1, self.mentionable_users[self.turn]
        else:
            color = piece.getColor()
            piece = piece.getPiece() 
        if piece == " king" and self.board.get(arg2, None) and self.board[arg2].getPiece() == " rook": # If Castle Input
            if arg2[0] == "a":
                self.board, new_pos = self.board[arg1].moveTo("kc")
            elif arg2[0] == "h":
                self.board, new_pos = self.board[arg1].moveTo("qc")
        else: # Normal Move
            self.board, new_pos = self.board[arg1].moveTo(arg2)
        if new_pos == -1: # Move invalid due to check or space was blocked by a piece
            print("Move invalid")
            print("Valid Moves:",self.board[arg1].valid_moves)
            return -1, self.mentionable_users[self.turn]
        else:
            if piece == " king": # Update king_pos if king was moved
                self.king_pos[color] = new_pos
            if self.pieces_left < self.getPieceCount(): # Update Stalemate timer
                self.stalemate_timer = 50
                self.pieces_left = self.getPieceCount()
            else:
                self.stalemate_timer -= 1
            if self.stalemate_timer == 0: # Stalemate
                return 6, None
            self.updateAllPieces()
            if piece == " pawn" and arg2[1] in ["1","8"]: # Pawn Promotion time
                self.turn = (self.turn+1)%2
                return 2, self.mentionable_users[self.turn]
            elif self.checkDraw(self.getOtherPlayer()): # Draw
                if self.inCheck(self.getOtherPlayer()): # Checkmate
                    self.turn = (self.turn+1)%2
                    return 5, self.mentionable_users[(self.turn+1)%2]
                self.turn = (self.turn+1)%2
                return 3, None
            elif self.inCheck(self.getOtherPlayer()): # Other player in check
                self.turn = (self.turn+1)%2
                return 4, self.mentionable_users[(self.turn+1)%2]
            else: # Normal turn occured
                self.turn = (self.turn+1)%2
                return 1, self.board

    def promotePawn(self, promoteTo):
        for pos in self.board:
            if pos[1] in ['1', '8'] and self.board.get(pos, None):
                if self.board[pos].getPiece() == " pawn":
                    self.board[pos].promotePawn(promoteTo, self.king_pos[self.board[pos].getColor()])
                    break

    def updateAllPieces(self):
        toUpdate = []
        for pos in self.board:
            if self.board.get(pos, None):
                toUpdate.append(pos)
        for pos in toUpdate:
            if self.board.get(pos, None):
                self.board[pos].updateValidMoves(self.board, self.king_pos[self.board[pos].getColor()])
    
    def checkDraw(self, userA):
        color = self.getColor(userA)
        for pos in self.board:
            if self.board.get(pos, None) and self.board[pos].getColor() == color:
                if len(self.board[pos].valid_moves) > 0:
                    return False
        return True

    def inCheck(self, userA):
        return self.board[self.king_pos[self.getColor(userA)]].in_check

    def drawBoard(self):
        return self.draw.drawBoard(self.board)