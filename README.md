# DiscordChessBot
A Discord bot that lets you play Chess with friends

Art for Chess Pieces obtained from:
- https://pixabay.com/vectors/chess-pieces-set-symbols-game-26774/

Things to Do:
- Set up skeleton for bot.py for how different commands should work
- Set up logic.py to set up the board using chess pieces and accept commands and run game (Almost Done)
- Add en passante to move validity for pawn and complete method to do it
- Add to lookForChecks a way to see if en passante will result in a check

Steps in turn:
- Send Image of Board State
- After Recieving Input
- See If It's A Valid Move
  - If yes, continue
  - Otherwise, return error and go back a step
- Update Valid Moves of all Pieces
- Check for draw, check, and checkmate (and maybe stalemante) and announce them after updating the image
  - If draw or checkmate, end game
  - Otherwise, go back to step 1 for next turn