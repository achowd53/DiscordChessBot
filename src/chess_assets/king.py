from .piece import ChessPiece

class King(ChessPiece):
    def __init__(self):
        self.piece = " king"
        pass
    
    def castle(self, side): #Castles on king or queenside and returns board, new position of king
        if side == "queen":
            self.num_movements += 1
            self.board["a"+self.loc[1]].num_movements += 1
            self.board["c"+self.loc[1]] = self.board["e"+self.loc[1]]
            self.board["d"+self.loc[1]] = self.board["a"+self.loc[1]]
            self.board["e"+self.loc[1]] = None
            self.board["a"+self.loc[1]] = None
            return self.board, "c"+self.getLoc[1]
        else:
            self.num_movements += 1
            self.board["h"+self.loc[1]].num_movements += 1
            self.board["g"+self.loc[1]] = self.board["e"+self.loc[1]]
            self.board["f"+self.loc[1]] = self.board["h"+self.loc[1]]
            self.board["e"+self.loc[1]] = None
            self.board["h"+self.loc[1]] = None
            return self.board, "g"+self.loc[1]

    def updateValidMoves(self, board: dict, king_pos: str):
        self.valid_moves = set()
        for target in [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]:
            loc = self._addToLocWithNums(self.loc, target)
            if self.board.get(loc, None) != None:
                self.valid_moves.add(loc)
        if not self.hasMoved():
            if not any(self.board.get("d"+self.loc[1], None), self.board.get("c"+self.loc[1], None), 
              self.board.get("b"+self.loc[1], None)) and self.board.get("a"+self.loc[1], None) and \
              self.board["a"+self.loc[1]].getPiece() == " rook" and self.board["a"+self.loc[1]].getColor() == self.color \
              and not self.board["a"+self.loc[1]].hasMoved():
                self.valid_moves.add("qc")
            if not any(self.board.get("f"+self.loc[1], None), self.board.get("g"+self.loc[1], None)) \
              and self.board.get("h"+self.loc[1], None) and self.board["h"+self.loc[1]].getPiece() == " rook" \
              and self.board["h"+self.loc[1]].getColor() == self.getColor() and not self.board["h"+self.loc[1]].hasMoved():
                self.valid_moves.add("kc")
        return super().updateValidMoves(board, king_pos)