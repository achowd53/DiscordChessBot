# DiscordChessBot
A Discord bot that lets you play Chess with friends

Art for Chess Pieces obtained from:
- https://pixabay.com/vectors/chess-pieces-set-symbols-game-26774/

Things to Do:
- Make sure Draw, Stalemate work
- Make sure you can concurrently have the bot running multiple games at once
- Add en passante to move validity for pawn and complete method to do it
- Add to lookForChecks a way to see if en passante will result in a check 
- Allow for movement by chess notation (Maybe depending on how long it seems to implement)
- Chess Agent using Min-Max Algorithm with Alpha-Beta Pruning
- Chess Agent using Reinforcement Learning
- Chess Agent using CNN and MonteCarlo Tree Search
- Make these Agents playable against

En Passante: How To Implement (Temp):
- En Passante implementation suggestions:
  - Add an private attribute to pawns of add_ep 
  - After a 2-move, set the add-ep of any adjacent enemy pawns to loc of the pawn that moved
  - After updating valid_moves, reset add_ep to None for a pawn
- To test en passante for valid moves, do the following:
  - Move 2-move piece back 1
  - Do a normal pawn take on it 
