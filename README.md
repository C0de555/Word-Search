# Word-Search
For this project, you will be using your knowledge of classes and lists to create
a word search game that runs in the terminal. You will be given a few samples to
work with. Each sample will have 2 files:

WS -> The word search board that you will have to load into your code to start the game.
Key -> A key file that lets you know what words you need to find in order to win the game.

The game will have unlimited moves until the player either gives up (quit), or
finds all key words on the board. On each turn, you should give the player the
option to continue guessing the word on the board or to quit. Once all key words
have been found, print out a congratulatory message to the player that they've won
the game. If the player quits, print out a consolation message. If the player enters
a word that exist in the board but is not a key word, print out a message letting
the player know that it is not a valid key word.

You have the option of printing out the word search game board at the start of
the game if you wish to enhance the playing experience. You may not, however,
print out the keys to the player. Since we are creating a word search game that
automatically checks where the word is found, we need to level the playing field
by having the player guess the key words.

When the player's guess matches up with a key on the board, output the location
of the word on the board with the surrounding letters in underscore.

Example:
If the player enters FLORIDA (States_WS.txt file) and it is a matched key, we
should output:
 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
 F L O R I D A - - - - - - - -
 - - - - - - - - - - - - - - -
 - - - - - - - - - - - - - - -
 - - - - - - - - - - - - - - -
 - - - - - - - - - - - - - - -
 - - - - - - - - - - - - - - -
 - - - - - - - - - - - - - - -
 - - - - - - - - - - - - - - -
 - - - - - - - - - - - - - - -
 - - - - - - - - - - - - - - -
 - - - - - - - - - - - - - - -
 - - - - - - - - - - - - - - -
 - - - - - - - - - - - - - - -
 - - - - - - - - - - - - - - -
 If the player has already guessed the word, print out a message to inform the player

 Take into consideration the spacing and letter casing. If you would like more
 test samples, you can easily make your own word search template online here:
 http://puzzlemaker.discoveryeducation.com/WordSearchSetupForm.asp
