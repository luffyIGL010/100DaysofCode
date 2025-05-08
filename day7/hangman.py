# hangman 
import random
choosen_word = random.choice(["python", "java", "kotlin", "javascript"])
word_length = len(choosen_word) 
display = []
for _ in range(word_length):
    display += "_"

print(choosen_word)
print(display)
lives = 6
end_of_game = False

while not end_of_game:
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter in display:
        print(f"You've already guessed {guess_letter}")
    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess_letter:
            display[position] = letter
    if guess_letter not in choosen_word:
        lives -= 1
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win.")