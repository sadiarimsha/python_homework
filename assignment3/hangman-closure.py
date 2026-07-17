def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        display = ""
        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += "_"
        print(display)
        return all(char in guesses for char in secret_word)
    
    return hangman_closure

secret = input("Enter secret word: ")
game = make_hangman(secret)

finished = False

while not finished:
    guess = input("Enter a letter: ")
    finished = game(guess)

print("Congrats, You are a winner!")