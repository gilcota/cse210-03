import secrets
from game.terminal_service import TerminalService

class SecretList:
    """The list with the secret words.
    
    The responsibility of SecretList is to to have a bank of words to be guessed.
    
    Attributes:
        _secret_list (List[str]): The word bank from where the secret word will be chosen
        _secret_word (str): Secret word randomly chosen from the secret list
        _terminal_service (TerminalService): Calls the terminal service class to do inputs from the terminal and print to the terminal
        _word_guess_status (str): Keeps track of the words guessed and words missing
        winner (str): Determines if no more words are needed to be guessed, and so if the player wins
    """

    def __init__(self):
        """Constructs a new SecretList.

        Args:
            self (Parachute): An instance of Parachute.
        """
        self._secret_list = [
            "class",
            "python",
            "encapsulation",
            "programming",
            "technology",
            "parachute",
            "winner",
            "loser",
            ]
        self._secret_word = secrets.choice(self._secret_list)
        self._secret_word_list = list(self._secret_word) 
        self._terminal_service = TerminalService()
        self._word_guess_status = ""
        self.winner = ""

    def word_guess_status(self, letters_guessed): 
        
        """Gets amount of lines count.

        Args:
            self (Parachute): An instance of Parachute.
            letters_guessed (List[str]): Brings the letters that have been guessed from the secret word.
        
        Returns:
            string: Visual representation of words guessed and pending to be guessed
        """            
        self._word_guess_status = ""
        
        for letter in self._secret_word:
            if letter in letters_guessed:
                self._word_guess_status = self._word_guess_status + letter + " "
            else:
                self._word_guess_status = self._word_guess_status + "_ "

        if not "_" in self._word_guess_status:
            self.winner = "Yes"

        return self._word_guess_status
            
            
        

        