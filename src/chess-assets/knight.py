from .piece import ChessPiece

class Knight(ChessPiece):
    def __init__(self):
        pass
    
    def updateValidMoves(self, board: dict, king_pos: str):
        self.valid_moves = set()
        knight_moves = [(1,2),(2,1),(-1,2),(2,-1),(1,-2),(-2,1),(-1,-2),(-2,-1)]
        for shift in knight_moves:
            x = self._addToLocWithNums(self.loc, shift)
            if x != "NA":
                self.valid_moves.add(x)
        return super().updateValidMoves(board, king_pos)