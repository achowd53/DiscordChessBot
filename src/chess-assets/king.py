from .piece import ChessPiece

class King(ChessPiece):
    def __init__(self):
        self.piece = " king"
        pass
    
    def castle(self, loc): 
        pass

    def updateValidMoves(self, board: dict, king_pos: str):
        self.valid_moves = set()
        for target in [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]:
            loc = self._addToLocWithNums(self.loc, target)
            if self.board.get(loc, None) != None:
                self.valid_moves.add(loc)
        return super().updateValidMoves(board, king_pos)