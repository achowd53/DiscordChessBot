from .piece import ChessPiece

class Rook(ChessPiece):
    def __init__(self, loc, color):
        self.piece = " rook"
        super().__init__(loc, color)

    def updateValidMoves(self, board: dict, king_pos: str):
        self.board = board
        self.valid_moves = set()
        for shift in [[1,0],[-1,0],[0,1],[0,-1]]:
            temp_loc = self._addToLocWithNums(self.loc, shift)
            while temp_loc != "NA":
                switch = self.board.get(temp_loc, None)
                if switch == None:
                    self.valid_moves.add(temp_loc)
                    temp_loc = self._addToLocWithNums(temp_loc, shift)
                elif switch.getColor() == self.getOtherColor():
                    self.valid_moves.add(temp_loc)
                    break
                else:
                    break
        return super().updateValidMoves(board, king_pos)
