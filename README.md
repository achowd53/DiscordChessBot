# DiscordChessBot
A Discord bot that lets you play Chess with friends

Art for Chess Pieces obtained from:
- https://pixabay.com/vectors/chess-pieces-set-symbols-game-26774/

Things to Do:
- Add en passante to move validity for pawn and complete method to do it
- Add to lookForChecks a way to see if en passante will result in a check
- Set up logic.py to set up the board using chess pieces and accept commands and run game
- Set up skeleton for bot.py for how different commands should work

Steps in turn:
- Send Image of Board State
- Update Valid Moves of all Pieces
- After Recieving Input
- See If It's A Valid Move
  - If yes, continue
  - Otherwise, go back a step
- Check for draw, check, and checkmate (and maybe stalemante) and announce them after updating the image
  - If draw or checkmate, end game
  - Otherwise, go back to step 1 for next turn