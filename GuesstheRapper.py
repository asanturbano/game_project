#Pseudo code for the Guess the Rapper terminal-based game

"""
- Greet user
- Prompt user for name

- Welcome message to user (include name)

- Instructions for user about the game
    - 15 rap lyrics will be given out
    - User has to guess who the rapper is
    - The game will count right guesses and let you know how close 
you are to becoming a rapper

Prompt user if they're ready
    If ready, we'll start the game
    Else, if not ready, message letting them know they can try later (break)

Game starts
- ~100 rap lyrics saved in the database, different random rap lyric
pulled up each time

- Print random rap lyric
- Prompt for user inpur
    If correct, print message, count as 1
    If incorrect, print other message, count as 0
    Add to total score
    Return
- Repeat 14 more times

After 15 guesses,
- If 0-5 out of 15 guesses right, print message
- If 6-10 out of 15 guesses right, print message
- If 11-15 out of 15 guesses right, print message

Prompt user if they want to play again

"""