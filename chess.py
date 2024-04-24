class Chess:
    def __init__(self):
        self.board = [[" " for _ in range(8)] for _ in range(8)]

    @staticmethod
    def inputreader() -> list:
        # input:
        # long space: black king A1 white rook B3 ... or
        # long comma: black king A1, white rook B3, ... or
        # short space: BK A1 WR B3 ... or
        # short comma: BK A1, WR B3, ...
        # return: [bka1, wrb3, ...]
        pos_list = []
        input_str = input("Put in all piece positions: ")
        input_style = "none"
        if input_str:
            input_style = "short" if len(input_str.split()[0]) == 2 else "long"
        if input_style == "none":
            return []
        sep = ", " if "," in input_str else " "
        if sep == ", ":
            if input_style == "short":  # short comma
                input_list = [piece for piece in input_str.split(sep)]
            else:  # input_style == "long"; long comma
                for word in input_str.split():
                    if len(word) > 3:
                        input_str = input_str.replace(word, word[0])
                input_list = [piece for piece in input_str.split(sep)]
        else:  # sep == " "
            if input_style == "short":  # short space
                helper_list = input_str.split(sep)
                input_list = ([helper_list[i] + helper_list[i + 1]
                               for i in range(0, len(helper_list) - 1, 2)])
            else:  # input_style == "long"; long space
                for word in input_str.split():
                    if len(word) > 2:
                        input_str = input_str.replace(word, word[0])
                helper_list = input_str.split()
                for i, word in enumerate(helper_list):
                    if len(word) == 2 and i < len(helper_list) - 1:
                        helper_list[i] = word + ","
                input_str = " ".join(helper_list)
                input_list = [piece for piece in input_str.split(",")]
        for piece in input_list:
            pos_list += [piece.replace(" ", "").lower()]
        return pos_list

    def set_board(self):
        positions = self.inputreader()  # [bka1, wrb3, ...]
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for piece in positions:
            row = piece[3]
            col = [letters.index(letter) + 1
                   for letter in letters if letter == piece[2]][0]
            self.board[8 - int(row)][int(col) - 1] = (piece[1].lower()
                                                      if piece[0] == "b"
                                                      else piece[1].upper())

    def print_board(self):
        string_rep = ("     a   b   c   d   e   f   g   h\n" +
                      "   " + "_" * 35 + "\n")
        for i, row in enumerate(self.board):
            string_rep += (" " + str(8 - i) + " | " + " | ".join(row) + " | " +
            str(8 - i) + "\n")
        string_rep += "   " + "_" * 35 + "\n" + \
                      "     a   b   c   d   e   f   g   h"
        print(string_rep)

    @staticmethod
    def chrtoint(letter: str) -> int:
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        return letters.index(letter)

    def available_moves(self) -> list:
        player_color = " "
        while player_color.lower() not in "wbwhiteblack":
            player_color = input("Put in your color: ")
            if player_color.lower() not in "wbwhiteblack":
                print("Invalid input! Put 'w', 'b', 'white', 'black'")
        pieces = []
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for i, row in enumerate(self.board):
            for square in row:
                if player_color.lower() in "white":
                    if square != " " and square.isupper():
                        pieces += ["w" + square.lower() +
                                   letters[row.index(square)] + str(8 - i)]
                else:  # player_color.lower() in "black"
                    if square != " " and square.islower():
                        pieces += ["b" + square.lower() +
                                   letters[row.index(square)] + str(8 - i)]
        moves = []
        for piece in pieces:
            if piece[1] == "k":  # K I N G
                # single step vertical up
                if piece[3] != "8" and (self.board[8 - int(piece[3]) - 1]
                                      [self.chrtoint(piece[2])] == " "):
                    print(piece)
                    moves += [piece + piece[2] + str(int(piece[3]) + 1)]
                # single step vertical down
                if piece[3] != "1" and (self.board[8 - int(piece[3]) + 1]
                                      [self.chrtoint(piece[2])] == " "):
                    moves += [piece + piece[2] + str(int(piece[3]) - 1)]
                # single step horizontal left
                if piece[2] != "a" and (self.board[8 - int(piece[3])]
                                        [self.chrtoint(piece[2]) - 1] == " "):
                    moves += [piece + letters[self.chrtoint(piece[2]) - 1]
                              + piece[3]]
                # single step horizontal right
                if piece[2] != "h" and (self.board[8 - int(piece[3])]
                                        [self.chrtoint(piece[2]) + 1] == " "):
                    moves += [piece + letters[self.chrtoint(piece[2]) + 1]
                              + piece[3]]
                # single step diagonal up left
                if (piece[2] != "a" and piece[3] != "8" and
                        (self.board[8 - int(piece[3]) - 1]
                         [self.chrtoint(piece[2]) - 1] == " ")):
                    moves += [piece + letters[self.chrtoint(piece[2]) - 1]
                              + str(int(piece[3]) + 1)]
                # single step diagonal up right
                if (piece[2] != "h" and piece[3] != "8" and
                        (self.board[8 - int(piece[3]) - 1]
                         [self.chrtoint(piece[2]) + 1] == " ")):
                    moves += [piece + letters[self.chrtoint(piece[2]) + 1]
                              + str(int(piece[3]) + 1)]
                # single step diagonal down left
                if (piece[2] != "a" and piece[3] != "1" and
                        (self.board[8 - int(piece[3]) + 1]
                         [self.chrtoint(piece[2]) - 1] == " ")):
                    moves += [piece + letters[self.chrtoint(piece[2]) - 1]
                              + str(int(piece[3]) - 1)]
                # single step diagonal down right
                if (piece[2] != "h" and piece[3] != "1" and
                        (self.board[8 - int(piece[3]) + 1]
                         [self.chrtoint(piece[2]) - 1] == " ")):
                    moves += [piece + letters[self.chrtoint(piece[2]) + 1]
                              + str(int(piece[3]) - 1)]
                # take vertical up
                if piece[3] != "8" and (self.board[8 - int(piece[3]) - 1]
                                      [self.chrtoint(piece[2])] != " "):
                    moves += [piece + piece[2] +
                              str(int(piece[3]) + 1) + "take"]
                # take vertical down
                if piece[3] != "1" and (self.board[8 - int(piece[3]) + 1]
                                      [self.chrtoint(piece[2])] != " "):
                    moves += [piece + piece[2] +
                              str(int(piece[3]) - 1) + "take"]
                # take horizontal left
                if piece[2] != "a" and (self.board[8 - int(piece[3])]
                                        [self.chrtoint(piece[2]) - 1] != " "):
                    moves += [piece + letters[self.chrtoint(piece[2]) - 1] +
                              piece[3] + "take"]
                # take horizontal right
                if piece[2] != "h" and (self.board[8 - int(piece[3])]
                                        [self.chrtoint(piece[2]) + 1] != " "):
                    moves += [piece + letters[self.chrtoint(piece[2]) + 1] +
                              piece[3] + "take"]
                # take diagonal up left
                if (piece[2] != "a" and piece[3] != "8" and
                        (self.board[8 - int(piece[3]) - 1]
                         [self.chrtoint(piece[2]) - 1] != " ")):
                    moves += [piece + letters[self.chrtoint(piece[2]) - 1]
                              + str(int(piece[3]) + 1) + "take"]
                # take diagonal up right
                if (piece[2] != "h" and piece[3] != "8" and
                        (self.board[8 - int(piece[3]) - 1]
                         [self.chrtoint(piece[2]) + 1] != " ")):
                    moves += [piece + letters[self.chrtoint(piece[2]) + 1]
                              + str(int(piece[3]) + 1) + "take"]
                # take diagonal down left
                if (piece[2] != "a" and piece[3] != "1" and
                        (self.board[8 - int(piece[3]) + 1]
                         [self.chrtoint(piece[2]) - 1] != " ")):
                    moves += [piece + letters[self.chrtoint(piece[2]) - 1]
                              + str(int(piece[3]) - 1) + "take"]
                # take diagonal down right
                if (piece[2] != "h" and piece[3] != "1" and
                        (self.board[8 - int(piece[3]) + 1]
                         [self.chrtoint(piece[2]) - 1] != " ")):
                    moves += [piece + letters[self.chrtoint(piece[2]) + 1]
                              + str(int(piece[3]) - 1) + "take"]
            if piece[1] == "q":  # Q U E E N
                pass
            if piece[1] == "r":  # R O O K
                # move vertical up
                for square in range(8 - int(piece[3]) - 1, -1, -1):
                    if self.board[square][self.chrtoint(piece[2])] == " ":
                        moves += [piece + piece[2] + str(8 - square)]
                    else:  # self.board[] != " "
                        break
                # move vertical down
                for square in range(8 - int(piece[3]) + 1, 8):
                    if self.board[square][self.chrtoint(piece[2])] == " ":
                        moves += [piece + piece[2] + str(8 - square)]
                    else:  # self.board[] != " "
                        break
                # move horizontal left
                for square in range(self.chrtoint(piece[2]) - 1, -1, -1):
                    if self.board[8 - int(piece[3])][square] == " ":
                        moves += [piece + letters[square] + piece[3]]
                    else:  # self.board[] != " "
                        break
                # move horizontal right
                for square in range(self.chrtoint(piece[2]) + 1, 8):
                    if self.board[8 - int(piece[3])][square] == " ":
                        moves += [piece + letters[square] + piece[3]]
                    else:  # self.board[] != " "
                        break
                # take vertical up
                for square in range(8 - int(piece[3]) - 1, -1, -1):
                    if self.board[square][self.chrtoint(piece[2])] != " ":
                        moves += [piece + piece[2] + str(8 - square) + "take"]
                # take vertical down
                for square in range(8 - int(piece[3]) + 1, 8):
                    if self.board[square][self.chrtoint(piece[2])] != " ":
                        moves += [piece + piece[2] + str(8 - square) + "take"]
                # take horizontal left
                for square in range(self.chrtoint(piece[2]) - 1, -1, -1):
                    if self.board[8 - int(piece[3])][square] != " ":
                        moves += [piece + letters[square] + piece[3] + "take"]
                # take horizontal right
                for square in range(self.chrtoint(piece[2]) + 1, 8):
                    if self.board[8 - int(piece[3])][square] != " ":
                        moves += [piece + letters[square] + piece[3] + "take"]
            if piece[1] == "b":  # B I S H O P
                # move diagonal up left
                for square in range(self.chrtoint(piece[2]) - 1, -1, -1):
                    if 8 - int(piece[3]) + square - 3 < 0:  # upper bound
                        break
                    if self.board[8 - int(piece[3]) + square - 3][square] == " ":
                        moves += [piece + letters[int(piece[3]) + square - 3]
                                  + str(8 - square - 2)]
                    else:  # self.board[] != " "
                        break
                # move diagonal up right
                for square in range(self.chrtoint(piece[2]) + 1, 8):
                    if 8 - int(piece[3]) - square + 3 < 0:  # upper bound
                        break
                    if self.board[8 - int(piece[3]) - square + 3][square] == " ":
                        moves += [piece + letters[square]
                                  + str(square)]
                    else:  # self.board[] != " "
                        break
                # move diagonal down left
                for square in range(self.chrtoint(piece[2]) - 1, -1, -1):
                    if 8 - int(piece[3]) - square + 3 > 7:  # lower bound
                        break
                    if self.board[8 - int(piece[3]) - square + 3][square] == " ":
                        moves += [piece + letters[int(piece[3]) - square + 3]
                                  + str(8 - square - 2)]
                    else:  # self.board[] != " "
                        break
                # move diagonal down right
                for square in range(self.chrtoint(piece[2]) + 1, 8):
                    if 8 - int(piece[3]) + square - 3 > 7:  # lower bound
                        break
                    if self.board[square][8 - int(piece[3]) + square - 3] == " ":
                        moves += [piece + letters[square]
                                  + str(8 - square - 2)]
                    else:  # self.board[] != " "
                        break
                # take diagonal up left
                # take diagonal up right
                # take diagonal down left
                # take diagonal down right
            if piece[1] == "n":  # (K) N I G H T
                pass
            if piece[1] == "p":  # P A W N
                # starting row
                if (piece[3] == "2"
                        and self.board[5][self.chrtoint(piece[2])] == " "
                        and self.board[4][self.chrtoint(piece[2])] == " "):
                    moves += [piece + piece[2] + str(8 - 5)]  # single step
                    moves += [piece + piece[2] + str(8 - 4)]  # double step
                # single step
                if (piece[3] != "7" and piece[3] != "2" and  # exc conv&start
                        self.board[8 - int(piece[3]) - 1][self.chrtoint(piece[2])] == " "):
                    moves += [piece + piece[2] + str(int(piece[3]) + 1)]
                # diagonal left take
                if (piece[3] != "7" and piece[2] != "a"  # exc conv&left bound
                        and self.board[8 - int(piece[3]) - 1][self.chrtoint(piece[2]) - 1] != " "):
                    moves += [piece + letters[self.chrtoint(piece[2]) - 1]
                              + str(int(piece[3]) + 1) + "take"]
                # diagonal right take
                if (piece[3] != "7" and piece[2] != "h"  # exc conv&right bound
                        and self.board[8 - int(piece[3]) - 1][self.chrtoint(piece[2]) + 1] != " "):
                    moves += [piece + letters[self.chrtoint(piece[2]) + 1]
                              + str(int(piece[3]) + 1) + "take"]
                # conversion vertical
                if (piece[3] == "7"
                        and self.board[0][self.chrtoint(piece[2])] == " "):
                    moves += [piece + piece[2] + str(8 - 0) + "q"]
                # conversion diagonal left take
                if (piece[3] == "7" and piece[2] != "a"  # exc left bound
                        and self.board[0][self.chrtoint(piece[2]) - 1] != " "):
                    moves += [piece + str(int(piece[2]) - 1) + str(8 - 0)
                              + "takeq"]
                # conversion diagonal right take
                if (piece[3] == "7" and piece[2] != "h"  # exc right bound
                        and self.board[0][self.chrtoint(piece[2]) + 1] != " "):
                    moves += [piece + str(int(piece[2]) + 1) + str(8 - 0)
                              + "takeq"]
        print(moves)


chess = Chess()
chess.set_board()
chess.print_board()
chess.available_moves()
