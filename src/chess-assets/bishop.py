from .piece import ChessPiece

class Bishop(ChessPiece):
    def __init__(self):
        pass

    def updateValidMoves(self, board: dict, king_pos: str):
        self.valid_moves = set()
        for piece_name, shift in [[1,1],[1,-1],[-1,1],[-1,-1]]:
            temp_loc = self._addToLocWithNums(self.loc, shift)
            while temp_loc != "NA":
                switch = self.board.get(temp_loc, None)
                if switch == None:
                    self.valid_moves.add(temp_loc)
                    temp_loc = self._addToLocWithNums(temp_loc, shift)
                elif switch.getName() == self.getOtherColor() + piece_name:
                    self.valid_moves.add(temp_loc)
                    break
                else:
                    break
        return super().updateValidMoves(board, king_pos)
# Overload updateValidMoves