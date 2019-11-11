#!/usr/bin/env python3

from random import *

player_score = 0
computer_score = 0

def draw_hangman(hangman):
	graphic = [
	"""
			+-------+
			|
			|
			|
			|
			|
		    =================
		"""
			,
		"""
			+-------+
			|       |
			|       O
			|
			|
			|
		    =================
		"""
			,
		"""
			+-------+
			|       |
			|       O
			|       |
			|
			|
		    =================
		"""
			,
		"""
			+-------+
			|       |
			|       O
			|       |
			|      /
			|
		    =================
		"""
			,
		"""
			+-------+
			|       |
			|       O
			|       |
			|      / \\
			|
		    =================
		"""
			,
		"""
			+-------+
			|       |
			|       O
			|      /|
			|      / \\
			|
		    =================
		"""
			,
		"""
			+-------+
			|       |
			|       O
			|      /|\\
			|      / \\
			|
		    =================
		"""]
	
	
	print(graphic[hangman])
	return

def start_game():
	print("Let's play a game of Hangman.")
	while game():
		pass
	scores()

def game():
	dictionary = ["gnu", "kernel", "mageia", "penguin", "ubuntu"]
	word = choice(dictionary)
	word_length = len(word)
	clue = word_length * ["_"]
	tries = 6
	letters_tried = ""
	guesses = 0
	letters_right = 0
	letters_wrong = 0
	global computer_score, player_score
	
	while (letters_wrong != tries) and ("".join(clue) != word):
		letter = guess_letter()
		if len(letter)==1 and letter.isalpha():
			if letters_tried.find(letter) != -1:
				print("You have already guessed ",letter)
			else:
				letters_tried = letters_tried + letter
				first_index = word.find(letter)
				if first_index == -1:
					letters_wrong += 1
					print("Sorry,",letter, "isn't in this word.")
				else:
					print("Good guess,",letter,"is correct.")
					for i in range(word_length):
						if letter == word[i]:
							clue[i] = letter
		else:
			print("Choose another")
			
		draw_hangman(letters_wrong)
		print(" ".join(clue))
		print("Guesses: ", letters_tried)
		
		if letters_wrong == tries:
			print("Game Over")
			print("The word was", word)
			computer_score += 1
			break	
		if "".join(clue) == word:
			print("You win!")
			print("The word was", word)
			player_score += 1
			break
	return play_again()

def guess_letter():
	print()
	letter = input("Guess a letter:")
	letter.strip().lower()
	print()
	return letter

def play_again():
	answer = input("Would you like to play again? y/n: ")
	if answer in ("y", "yes"):
		return answer
	else:
		print("Goodbye")

def scores():
	global computer_score, player_score
	print("HIGH SCORES")
	print("Player: ", player_score)
	print("Computer: ", computer_score)

if __name__ == '__main__':
	start_game()
	