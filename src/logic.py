from random import shuffle

class ChessGame: # Promotion, En Passante not implemented
    
    def __init__(self, userA, userB):
        self.users = [str(userA), str(userB)]
        shuffle([str(userA), str(userB)])
        self.mentionable_users = [userA, userB]
        self.turn = 1
        self.in_check = -1
        self.board = {}
        self.king_pos = {}
        self.initBoard()
    
    def initBoard(self): # Initializes board state
        self.board = {}
        self.king_pos = {"b":"e1","w":"e8"}
        for col in "abcdefgh":
            self.board[col+"7"] = "wp"
            self.board[col+"2"] = "bp"
        for col, piece in list(zip("abcdefgh","rhbqkbhr")):
            self.board[col+"8"] = "w"+piece
            self.board[col+"1"] = "b"+piece
        
    def getCurrentPlayer(self):
        return self.users[self.turn]
    
    def getOtherPlayer(self):
        return list(set(self.users)-set([self.getCurrentPlayer()]))[0]
    
    def getCurrentColor(self):
        return ["b","w"][self.turn]
    
    def getOtherColor(self):
        return ["b","w"][(self.turn+1)%2]
    
    def move(self, userA, arg1, arg2): # Makes Move, -1: Error, 1: Successful, 2: Promotion Input Required, 3: Checkmate, 4: Draw
        if userA != self.getCurrentPlayer():
            return -1, None
        if self.board.get(arg1, 0) and self.board[arg1] == self.getCurrentColor() and\
        self.validateMove(arg1, arg2):
            pre_move_board = self.board
            if self.inCheck(userA):
                self.in_check = self.turn
            else:
                if self.in_check == self.turn:
                    self.in_check = -1
            self.board[arg2] = self.board[arg1]
            self.board[arg1] = None
            self.turn = (self.turn+1)%2
            if self.board[arg2][1] == "k":
                self.king_pos[self.board[arg2]] = arg2
            if self.inCheck(userA):
                self.board = pre_move_board
                return -1, None
            if self.checkDraw(self.getOtherPlayer()):
                return 4, None
            if self.inCheck(self.getOtherPlayer()) and self.checkDraw(self.getOtherPlayer()):
                if str(self.mentionable_users[1]) == self.getOtherPlayer():
                    return 3, self.mentionable_users[1]
                else:
                    return 3, self.mentionable_users[0]
            return 1, None 
        return -1, None
    
    def checkDraw(self, userA):
        for space in self.board:
            if self.board[space] != None and self.board[space][0] == self.getCurrentColor():
                if self.board[space][1] == "r":
                    if any(self.validateMove(space, chr(ord(space[0])-1)+space[1]),
                           self.validateMove(space, chr(ord(space[0])+1)+space[1]),
                           self.validateMove(space, space[0]+chr(ord(space[1])-1)),
                           self.validateMove(space, space[0]+chr(ord(space[1])-1))):
                        return False
                elif self.board[space][1] == "p":
                    if any(self.validateMove(space, chr(ord(space[0])-1)+chr(ord(space[1])-1)),
                           self.validateMove(space, chr(ord(space[0])+1)+chr(ord(space[1])-1)),
                           self.validateMove(space, space[0]+chr(ord(space[1])-1)),
                           self.validateMove(space, chr(ord(space[0])-1)+chr(ord(space[1])+1)),
                           self.validateMove(space, chr(ord(space[0])+1)+chr(ord(space[1])+1)),
                           self.validateMove(space, space[0]+chr(ord(space[1])+1))):
                        return False
                elif self.board[space][1] == "h":
                    if any(self.validateMove(space, chr(ord(space[0])-1)+chr(ord(space[1])-2)),
                           self.validateMove(space, chr(ord(space[0])-2)+chr(ord(space[1])-1)),
                           self.validateMove(space, chr(ord(space[0])+1)+chr(ord(space[1])-2)),
                           self.validateMove(space, chr(ord(space[0])+2)+chr(ord(space[1])-1)),
                           self.validateMove(space, chr(ord(space[0])-1)+chr(ord(space[1])+2)),
                           self.validateMove(space, chr(ord(space[0])-2)+chr(ord(space[1])+1)),
                           self.validateMove(space, chr(ord(space[0])+1)+chr(ord(space[1])+2)),
                           self.validateMove(space, chr(ord(space[0])+2)+chr(ord(space[1])+1))):
                        return False
                elif self.board[space][1] == "b":
                    if any(self.validateMove(space, chr(ord(space[0])-1)+chr(ord(space[1])-1)),
                           self.validateMove(space, chr(ord(space[0])-1)+chr(ord(space[1])+1)),
                           self.validateMove(space, chr(ord(space[0])+1)+chr(ord(space[1])+1)),
                           self.validateMove(space, chr(ord(space[0])+1)+chr(ord(space[1])-1))):
                        return False
                else:
                    if any(self.validateMove(space, chr(ord(space[0])-1)+chr(ord(space[1])-1)),
                           self.validateMove(space, chr(ord(space[0])-1)+chr(ord(space[1]))),
                           self.validateMove(space, chr(ord(space[0])-1)+chr(ord(space[1])+1)),
                           self.validateMove(space, chr(ord(space[0]))+chr(ord(space[1])+1)),
                           self.validateMove(space, chr(ord(space[0]))+chr(ord(space[1])-1)),
                           self.validateMove(space, chr(ord(space[0])+1)+chr(ord(space[1])-1)),
                           self.validateMove(space, chr(ord(space[0])+1)+chr(ord(space[1]))),
                           self.validateMove(space, chr(ord(space[0])+1)+chr(ord(space[1])+1))):
                        return False
        return True

    def inCheck(self, userA):
        king_loc = self.king_pos[self.getCurrentColor()]
        if self.getOtherColor()+"p" in [self.board.get(chr(ord(king_loc[0])+1)+chr(ord(king_loc[0])+(1 if self.getCurrentColor() == "b" else -1), None)),
                                        self.board.get(chr(ord(king_loc[0])-1)+chr(ord(king_loc[0])+(1 if self.getCurrentColor() == "b" else -1), None))]:
            return True
        if any(self.getOtherColor()+"k" == self.board.get(x,None) for x in [chr(ord(king_loc[0])-1)+chr(ord(king_loc[1])-1),
            chr(ord(king_loc[0])-1)+chr(ord(king_loc[1])), chr(ord(king_loc[0])-1)+chr(ord(king_loc[1])+1),
            chr(ord(king_loc[0]))+chr(ord(king_loc[1])+1), chr(ord(king_loc[0]))+chr(ord(king_loc[1])-1),
            chr(ord(king_loc[0])+1)+chr(ord(king_loc[1])-1), chr(ord(king_loc[0])+1)+chr(ord(king_loc[1])),
            chr(ord(king_loc[0])+1)+chr(ord(king_loc[1])+1)]):
            return True
        if any(self.getOtherColor()+"h" == self.board.get(x, None) for x in [chr(ord(king_loc[0])-1)+chr(ord(king_loc[1])-2),
            chr(ord(king_loc[0])-2)+chr(ord(king_loc[1])-1), chr(ord(king_loc[0])+1)+chr(ord(king_loc[1])-2),
            chr(ord(king_loc[0])+2)+chr(ord(king_loc[1])-1), chr(ord(king_loc[0])-1)+chr(ord(king_loc[1])+2),
            chr(ord(king_loc[0])-2)+chr(ord(king_loc[1])+1), chr(ord(king_loc[0])+1)+chr(ord(king_loc[1])+2),
            chr(ord(king_loc[0])+2)+chr(ord(king_loc[1])+1)]):
            return True
        for i in range(1,8):
            if self.board.get(king_loc[0] + chr(ord(king_loc[1])+i), None) in [self.getOtherColor()+"r",self.getOtherColor()+"q"] or\
               self.board.get(king_loc[0] + chr(ord(king_loc[1])-i), None) in [self.getOtherColor()+"r",self.getOtherColor()+"q"] or\
               self.board.get(chr(ord(king_loc[0])+i) + king_loc[1], None) in [self.getOtherColor()+"r",self.getOtherColor()+"q"] or\
               self.board.get(chr(ord(king_loc[0])-i) + king_loc[1], None) in [self.getOtherColor()+"r",self.getOtherColor()+"q"] or\
               self.board.get(chr(ord(king_loc[0])+i) + chr(ord(king_loc[1])+i), None) in [self.getOtherColor()+"b",self.getOtherColor()+"q"] or\
               self.board.get(chr(ord(king_loc[0])+i) + chr(ord(king_loc[1])-i), None) in [self.getOtherColor()+"b",self.getOtherColor()+"q"] or\
               self.board.get(chr(ord(king_loc[0])-i) + chr(ord(king_loc[1])+i), None) in [self.getOtherColor()+"b",self.getOtherColor()+"q"] or\
               self.board.get(chr(ord(king_loc[0])-i) + chr(ord(king_loc[1])-i), None) in [self.getOtherColor()+"b",self.getOtherColor()+"q"]:
                   return True
        return False
    
    def validateMove(self, arg1, arg2): # See if movement of piece is valid for piece
        if len(arg1) != 2 or len(arg2) != 2 or not('a' <= arg1[0].lower() <= 'h') or not('a' <= arg2[0].lower() <= 'h') or\
        not('1' <= arg1[1] <= '8') or not('1' <= arg2[1] <= '8'):
            return False
        piece = self.board[arg1][1]
        if piece == "p":
            if self.board[arg1][0] == "b":
                if chr(ord(arg1[0])-1)+chr(ord(arg1[1])+1) == arg2 or chr(ord(arg1[0])+1)+chr(ord(arg1[1])+1) == arg2:
                    return self.board.get(arg2, None) != None
                elif arg1[1] == "2" and arg1[0]+chr(ord(arg1[1])+2) == arg2:
                    return self.board.get(arg2, None) == None
                elif arg1[0]+chr(ord(arg1[1])+1) == arg2:
                    return self.board.get(arg2, None) == None
                return False
            if self.board[arg1][0] == "w":
                if chr(ord(arg1[0])-1)+chr(ord(arg1[1])-1) == arg2 or chr(ord(arg1[0])+1)+chr(ord(arg1[1])-1) == arg2:
                    return self.board.get(arg2, None) != None
                elif arg1[1] == "7" and arg1[0]+chr(ord(arg1[1])-2) == arg2:
                    return self.board.get(arg2, None) == None
                elif arg1[0]+chr(ord(arg1[1])-1) == arg2:
                    return self.board.get(arg2, None) == None
                return False
        elif piece == "r":
            if abs(ord(arg1[0])-ord(arg2[0])) ^ abs(ord(arg1[1])-ord(arg2[1])):
                if abs(ord(arg1[0])-ord(arg2[0])):
                    for c in range(min(ord(arg1[0]),ord(arg2[0]))+1, max(ord(arg1[0]),ord(arg2[0]))):
                        if self.board.get(chr(c)+arg1[1], None) != None:
                            break
                    else:
                        return True
                else:
                    for c in range(min(ord(arg1[1]),ord(arg2[1]))+1, max(ord(arg1[1]),ord(arg2[1]))):
                        if self.board.get(arg1[0]+chr(c), None) != None:
                            break
                    else:
                        return True
                return False
            return False
        elif piece == "h":
            if sorted([abs(ord(arg1[0])-ord(arg2[0]), abs(ord(arg1[1])-ord(arg2[1])))]) == [1,2]:
                return self.board.get(arg2, None) != None
            return False
        elif piece == "b":
            if abs(ord(arg1[0])-ord(arg2[0])) == abs(ord(arg1[1])-ord(arg2[1])):
                hor_dir = -1 if ord(arg1[0])>ord(arg2[0]) else 1
                ver_dir = -1 if ord(arg1[1])>ord(arg2[1]) else 1
                for i in range(1,abs(ord(arg1[0])-ord(arg2[0]))):
                    if self.board.get(chr(ord(arg1[0])+hor_dir*i)+chr(ord(arg1[0])+ver_dir*i), None) != None:
                        return False
                else:
                    return True
            return False
        elif piece == "q":
            if abs(ord(arg1[0])-ord(arg2[0])) ^ abs(ord(arg1[1])-ord(arg2[1])):
                if abs(ord(arg1[0])-ord(arg2[0])):
                    for c in range(min(ord(arg1[0]),ord(arg2[0]))+1, max(ord(arg1[0]),ord(arg2[0]))):
                        if self.board.get(chr(c)+arg1[1], None) != None:
                            return False
                    return True
                else:
                    for c in range(min(ord(arg1[1]),ord(arg2[1]))+1, max(ord(arg1[1]),ord(arg2[1]))):
                        if self.board.get(arg1[0]+chr(c), None) != None:
                            return False
                    return True
            elif abs(ord(arg1[0])-ord(arg2[0])) == abs(ord(arg1[1])-ord(arg2[1])):
                hor_dir = -1 if ord(arg1[0])>ord(arg2[0]) else 1
                ver_dir = -1 if ord(arg1[1])>ord(arg2[1]) else 1
                for i in range(1,abs(ord(arg1[0])-ord(arg2[0]))):
                    if self.board.get(chr(ord(arg1[0])+hor_dir*i)+chr(ord(arg1[0])+ver_dir*i), None) != None:
                        return False
                return True
            return False
        elif piece == "k":
            if abs(ord(arg1[0])-ord(arg2[0])) + abs(ord(arg1[1])-ord(arg2[1])) == 1:
                return True
            elif self.in_check != self.turn:
                if (self.board[arg1][0] == "b" and arg1 == "e1") or (self.board[arg1][0] == "w" and arg1 == "e8"):
                    if (arg2 == "b"+arg1[1] and "r" in self.board.get("a"+arg1[1])):
                        for c in range(ord('a')+1, ord('e')):
                            if self.board.get(chr(c)+arg1[1], None) != None:
                                return False
                        self.board["c"+arg1[1]] = self.board["a"+arg1[1]]
                        self.board["a"+arg1[1]] = None
                        return True 
                    elif(arg2 == "g"+arg1[1] and "r" in self.board.get("h"+arg1[1])):
                        for c in range(ord('e')+1, ord('h')):
                            if self.board.get(chr(c)+arg1[1], None) != None:
                                return False
                        self.board["f"+arg1[1]] = self.board["h"+arg1[1]]
                        self.board["h"+arg1[1]] = None
                        return True
                return False    
        return False                    