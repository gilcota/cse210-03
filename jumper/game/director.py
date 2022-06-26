from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.secret_list import SecretList

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _jumper (Jumper): The game's jumper.
        _secret_list (SecretList): The game's secret list of words.
        _terminal_service (TerminalService): For getting and displaying information on the terminal.
        _is_playing (boolean): Whether or not to keep playing.
        letter_chosen (str): Records the letter that was input as a guess.
        letters_guessed (List[str]): Keeps track of the letters that are part of the secret word.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._secret_list = SecretList()
        self._terminal_service = TerminalService()
        self._is_playing = True
        self.letter_chosen = ""
        self.letters_guessed = [""]
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self.do_outputs()
            self.get_inputs()
            self.do_updates()

    def get_inputs(self):
        """Gets the input of a letter used to try to guess the secret word and defines if the game is won or lost.

        Args:
            self (Director): An instance of Director.
        """
        if self._jumper._lines_cut == 4:
            self._terminal_service.write_text("You broke your parachute and crashed... game over.\nBetter luck next time dude!\n")
        elif self._secret_list.winner == "Yes":
            self._terminal_service.write_text("\"" + self._secret_list._secret_word.upper() + "\" is the word, you had a nice landing!\n")
            self._is_playing = False         
        else:
            self.letter_chosen = self._terminal_service.read_text("Guess a letter [a-z]: ")

        
    def do_updates(self):
        """Keeps status of lines to be cut from parachute and letters guessed from the secret word

        Args:
            self (Director): An instance of Director.
        """
        if self.letter_chosen in self._secret_list._secret_word:
            self.letters_guessed.append(self.letter_chosen) 
            self._secret_list.word_guess_status(self.letters_guessed)
        else:
            self._jumper._lines_cut += 1

                      
    def do_outputs(self):
        """Shows on terminal the status of the game and sets its continuation

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text("\n" + self._secret_list.word_guess_status(self.letters_guessed))
        self._terminal_service.write_text(self._jumper._parachute[self._jumper._lines_cut])

        if self._jumper._lines_cut == 4:
            self._is_playing = False        