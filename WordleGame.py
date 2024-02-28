import requests
import os

# ---------- CONSTANTS ---------- #
WORDS_API_KEY = os.environ.get("WORDS_API_KEY")
URL = "https://wordsapiv1.p.rapidapi.com/words/"

# ---------- WORDSAPI VARIABLES ---------- # 
querystring = {"random":"true","letters":"5"}

headers = {
	"X-RapidAPI-Key": WORDS_API_KEY,
	"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}

response = requests.get(URL, headers=headers, params=querystring)

# ---------- GLOBAL VARIABLES ---------- #
playing = True
word = str(response.json().get("word")).upper()
wordList = list(word)
guess = ""
attempt = 0
attempts = {
  0 : ["   ", "   ", "   ", "   ", "   "],
  1 : ["   ", "   ", "   ", "   ", "   "],
  2 : ["   ", "   ", "   ", "   ", "   "],
  3 : ["   ", "   ", "   ", "   ", "   "],
  4 : ["   ", "   ", "   ", "   ", "   "],
  5 : ["   ", "   ", "   ", "   ", "   "],
}
triedLetters = []

def showBoard():
  board = f"""
_______________________________
| {attempts[0][0]} | {attempts[0][1]} | {attempts[0][2]} | {attempts[0][3]} | {attempts[0][4]} |
-------------------------------
| {attempts[1][0]} | {attempts[1][1]} | {attempts[1][2]} | {attempts[1][3]} | {attempts[1][4]} |
-------------------------------
| {attempts[2][0]} | {attempts[2][1]} | {attempts[2][2]} | {attempts[2][3]} | {attempts[2][4]} |
-------------------------------
| {attempts[3][0]} | {attempts[3][1]} | {attempts[3][2]} | {attempts[3][3]} | {attempts[3][4]} |
-------------------------------
| {attempts[4][0]} | {attempts[4][1]} | {attempts[4][2]} | {attempts[4][3]} | {attempts[4][4]} |
-------------------------------
| {attempts[5][0]} | {attempts[5][1]} | {attempts[5][2]} | {attempts[5][3]} | {attempts[5][4]} |
_______________________________
"""
  return board




def playGame():
  global attempts
  global attempt
  global guess
  guessing = True
  guess = str(input("\nWhat is your guess? : ").strip().upper())
  while guessing:
    if len(guess) != 5:
      guess = str(input("\nPlease ensure your guess is exactly 5 characters : ").strip().upper())
    else:
      guessing = False

  guessList = list(guess)
  print(attempt)
  for letter in range(len(guessList)):
    if guessList[letter] == wordList[letter]:
      attempts[attempt][letter] = f"{guessList[letter]}✅"
    
    elif guessList[letter] in wordList:
      attempts[attempt][letter] = f"{guessList[letter]}🟨"
    
    else:
      attempts[attempt][letter] = f"{guessList[letter]}🟥"
      if guessList[letter] not in triedLetters:
        triedLetters.append(guessList[letter])
  attempt += 1
  print(showBoard())
  triedLetters.sort()
  print(f"Incorrect Letters: {triedLetters}")
  winCondition()


def winCondition():
  global guess
  global word
  global playing
  global attempt
  if guess == word:
    print(f"You win! The word was: {word}\n")
    playing = False
  
  elif attempt == 6:
    print(f"You lost! The word was: {word}\n")
    playing = False


def gameReset():
  global playing
  global attempt
  global triedLetters
  global attempts
  global word
  global wordList
  response = requests.get(URL, headers=headers, params=querystring)
  word = str(response.json().get("word")).upper()
  wordList = list(word)
  playing = True
  attempt = 0
  triedLetters = []
  attempts = {
    0 : ["   ", "   ", "   ", "   ", "   "],
    1 : ["   ", "   ", "   ", "   ", "   "],
    2 : ["   ", "   ", "   ", "   ", "   "],
    3 : ["   ", "   ", "   ", "   ", "   "],
    4 : ["   ", "   ", "   ", "   ", "   "],
    5 : ["   ", "   ", "   ", "   ", "   "],
  }


def start():
  global playing
  while True:
    askToPlay = input("Would you like to play a game similar to Wordle? 'Y' or 'N' : ").strip().upper()
    while askToPlay != "Y" and askToPlay != "N":
      askToPlay = input("Please type 'Y' or 'N' : ").strip().upper()
    if askToPlay == "N":
      exit()

    while playing:
      playGame()
    gameReset()


start()