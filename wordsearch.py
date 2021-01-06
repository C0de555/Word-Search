class WordSearch:
    def __init__(self, board, keys):
        self.board = board
        self.keys = keys
        self.word = None
        self.found_keys = []

    # Check if the index is within bounds of the word board
    def within_range(self, row, col):
        return False if (row < 0 or row > len(self.board) - 1) or (col < 0 or col > len(self.board[0]) - 1) else True

    # Check if the submitted word can be found on the board given a direction
    def check_direction(self, start, direction):
        char_indexes = []

        # make sure that the rest of the word is found with the given direction
        # and that it will not go out of bound
        row = start[0] + direction[0]
        col = start[1] + direction[1]
        for i in range(2, len(self.word)):
            if self.within_range(row, col) and self.word[i] == self.board[row][col]:
                char_indexes.append((row, col))
            else:
                return []

            row += direction[0]
            col += direction[1]
        return char_indexes

    # Check if the word can be found in a valid direction on the board.
    def find_word(self, indexes):
        # possible directions to find each character in the word (row, col)
        # start from upper left and end at lower right position
        directions = [(-1, -2), (-1, 0), (-1, 2), (0, -2), (0, 2), (1, -2), (1, 0), (1, 2)]
        print("indexes:", indexes)
        # go through all index candidates to find where the word is
        for index in indexes:
            for direction in directions:
                row = index[0] + direction[0]
                col = index[1] + direction[1]
                # check if the direction is out of bounds and if the rest of the word
                # exist in the direction where the 2nd character matches
                if self.within_range(row, col) and self.word[1] == self.board[row][col]:
                    char_indexes = self.check_direction((row, col), (direction[0], direction[1]))
                    # if all characters in word is found, record the word and print the board
                    # showing where the word is found
                    if len(char_indexes) > 0:
                        self.found_keys.append(self.word)
                        self.keys.remove(self.word)
                        self.print_board([index] + [(row, col)] + char_indexes)
                        return True

        return False

    # Print the word board with all characters or only the word found.
    # Also prints out the total key words left to search for and what
    # words have been found so far.
    def print_board(self, focus=[]):
        if len(focus) != 0:
            underscore = "_ " * len(self.board)
            focus_board = [[char for char in underscore[:-1]] for row in range(len(self.board))]

            # only show the characters in list
            for i in range(len(focus)):
                row = focus[i][0]
                col = focus[i][1]
                focus_board[row][col] = self.word[i].upper()

            for row in focus_board:
                print(''.join(row))
        else:
            for row in self.board:
                print(row.upper())

        print("\nWords found:", len(self.found_keys))
        if len(self.found_keys) > 0:
            print("\n", "  ".join(self.found_keys), "\n")

        print("Total key words left to search for:", len(self.keys), "\n")

    # Initializes the word search game and tries to find the word on the board
    def play(self):
        # record where the first character of the word is found
        indexes = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == self.word[0]:
                    indexes.append((row, col))
        # print(indexes)

        # find the word based on the index positions
        if self.find_word(indexes) and len(self.keys) == 0:
            return False
        return True


if __name__ == "__main__":
    game_file = input("Word search board name filename: ")

    # read in board & keys from file
    word_board = open(game_file + "_WS.txt").read().lower().splitlines()
    word_keys = open(game_file + "_Key.txt").read().lower().splitlines()

    # instantiate word search class
    ws = WordSearch(word_board, word_keys)
    # print board and start game
    ws.print_board()
    while True:
        ws.word = input("Enter found word on board (q to quit): ").lower().replace(" ", "")

        if ws.word == "q":
            print("Goodbye. Try again next time!")
            break
        elif ws.word in ws.found_keys:
            print("Word has already been found. Find another one.")
        elif ws.word not in ws.keys:
            print("Not a valid key word to win.")
        elif not ws.play():
            print("You've found all the key words, congratulations!")
            break
