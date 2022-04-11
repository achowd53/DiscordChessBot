from draw import ChessDraw
from logic import ChessGame

display = ChessDraw()
game = ChessGame("a","b")
a = game.getCurrentPlayer()
b = game.getOtherPlayer()
code, board = game.move(a, "f7", "f5")
code, board = game.move(b, "e2", "e3")
code, board = game.move(a, "e7", "e6")
code, board = game.move(b, "g1", "f3")
code, board = game.move(a, "d8", "h4")
code, board = game.move(b, "f3", "h4")
display.drawBoard(board)
display.showBoard()
