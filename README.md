# Vityarthi-Project
Word Guessing Game:Includes Taking inputs(guesses from user) and then gives feedback about the accuracy of their guess. It uses dictionary,loops,control-if statements,libraries and modules to execute precisely.It is an interactive and user-friendly game
# Word Guessing Game

## Overview

This is a Wordle-style word game that runs in the terminal. The game picks a secret word and you try to guess it. After every guess, each letter is colored to tell you how close you were. You can play with a totally random word or pick a category like Movies, Animals or Sports, and there are three difficulty levels if you go with the random mode.

I made this as a Python practice project, and it was a fun way to work with lists, dictionaries, functions and recursion.

## Features

- Two game modes: a completely random word, or a word from a category of your choice
- 10 categories to pick from: Science, Movies, Games, Computer, Environment, Animals, Food/Drink, Colors, Countries and Sports
- Three difficulty levels in random mode (Easy: 4-5 letters, Medium: 6-7 letters, Hard: 8-10 letters)
- Colored feedback for every guess:
  - Green means the right letter in the right spot
  - Yellow means the right letter in the wrong spot
  - Red means the letter isn't in the word
- A short message after each guess ("Keep going", "Good try", etc.) based on how close you are
- You get (word length + 1) chances
- A one-time hint if you're running low on lives (it reveals one letter you haven't found yet)
- Your previous guesses are shown after every turn so you can compare them
- Guesses are checked, so wrong-length words and made-up words don't cost you a life
- A play again option at the end

## Technologies / Tools Used

- Python 3
- [english-words] for the dictionary of valid words
- [colorama] for the colored letters in the terminal
- `random` module (comes with Python)

## Steps to Install & Run

1. Make sure Python 3 is installed. You can check with:

   
   python --version
  

2. Download or clone this project and open a terminal in the project folder.

3. Install the two libraries the game needs:

 
   pip install english-words colorama
  

4. Run the game (replace `WordGuessGame.py` with whatever you named your file):

   
   python WordGuessGame.py
   

5. Follow the prompts on screen. Choose a game mode, pick a difficulty or category, and start guessing!

## Instructions for Testing

There are no automated tests, so the best way to check everything works is to play the game and try a few things on purpose:

- Menus: Type a wrong choice (like `7` at the difficulty menu, or a letter at the category menu) and check that the game asks again instead of crashing.
- Guess length: Enter a word that is shorter or longer than the number of blanks. You should get an error message and keep all your lives.
- Invalid words: Enter random letters like `qwzxv`. The game should say the word isn't valid and not use up a chance.
- Colors: Guess a word that shares some letters with the answer and check that green, yellow and red show up correctly. Words with repeated letters are a good test here.
- Winning: Guess the word correctly and check that you see the win message.
- Losing: Use up all your chances and check that the game shows the lose message and tells you the word.
- Hint: Keep guessing wrong until you have fewer than 3 lives left. The game should offer a hint once, and it should show one correct letter in its position.
- Play again: After a game ends, type `y` to start over and `n` to quit. Anything else should just ask again.
## Screenshots 
-opening game: ![alt text](<Screenshot 2026-09-30 150728.png>)
-first function:![alt text](<Screenshot 2026-09-30 160824.png>)
-Second function: ![alt text](<Screenshot 2026-09-30 161025.png>)
-Winning Case: ![alt text](<Screenshot 2026-09-30 151136.png>)
-Losing Case: ![alt text](<Screenshot 2026-09-30 160724.png>)
