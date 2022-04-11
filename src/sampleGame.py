from draw import ChessDraw
from logic import ChessGame

display = ChessDraw()
game = ChessGame("a","b")
a = game.getCurrentPlayer()
b = game.getOtherPlayer()
code, board = game.move(a, "f7", "f5")
display.drawBoard(board)
display.showBoard()
code, board = game.move(b, "e2", "e3")
display.drawBoard(board)
display.showBoard()
