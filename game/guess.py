import random

from game.terminal_service import TerminalService

class Guess:
    """The secret word that the lattes have to be guessed. 
    
    The responsibility of Guess is to monitor the word and guessed latters. 
    
    Attributes:
        _guess: The guessed latters (A-Z).
        letters_left: Keep track of how many letters are left blank.
        wrong_guess : Number of letter wrongly guessed.
    """

    def __init__(self):
        """Constructs a new Guess.

        Args:
            self (Guess): An instance of Guess.
        """
        terminal_service = TerminalService()
        self._words_list = ["Winter", "Today", "Spring"]
        self._word_chosen = ""

        self._word_guess = ["_"]*len(self._word_chosen)
    
    def _selected_word(self):
        """select and return rundom word from the list.

        Args:
            self (Guess): An instance of Guess.
        
        Returns:
            string: the selected word.
        """
        self.picked = random.choice(self._words_list)
        return self.picked


    def draw_word_guess(self):

        self.terminalservice.write_text(self._words_list)

        
    def process_guess(self, guess_letter):
        """Watches the guess by keeping track of the letters guessed.

        Args:
            self (Guess): An instance of Guess.
        """
        for i in range(len(self.picked)):
            if guess_letter == self.picked[i]:
                self.picked = guess_letter
        
    def can_keep_guessing(self):

        pass