# DiscordChessBot
A Discord bot that lets you play Chess with friends

Art for Chess Pieces obtained from:
- https://pixabay.com/vectors/chess-pieces-set-symbols-game-26774/

Things to Do:
- Make sure check, checkmate, and draw work
- Make sure you can properly start another game after one ends
- Make sure you can concurrently have the bot running multiple games at once
- Add en passante to move validity for pawn and complete method to do it
- Add to lookForChecks a way to see if en passante will result in a check
- Stalemate 
- Allow for movement by chess notation
- Chess Agent using Min-Max Algorithm with Alpha-Beta Pruning
- Chess Agent using Reinforcement Learning
- Chess Agent using CNN and MonteCarlo Tree Search
- Make these Agents playable against

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