class Jumper:
    """The jumper. 
    
    The responsibility of Jumper is to show the jumper's parachute condition throughout the game.
    
    Attributes:
        _parachute (List[str]): Representation of all states of the parachute.
        _lines_cut (int): Keeps track of amount of lines cut from the parachute.
    """

    def __init__(self):
        """Constructs a new Parachute.

        Args:
            self (Parachute): An instance of Parachute.
        """
        self._parachute = [
            "       \n"
            "  ___  \n"
            " /___\ \n"
            " \   / \n"
            "  \ /  \n"
            "   O   \n"
            "  /|\  \n"
            "  / \  \n"
            "       \n"
            "^^^^^^^\n",

            "       \n"
            " /___\ \n"
            " \   / \n"
            "  \ /  \n"
            "   O   \n"
            "  /|\  \n"
            "  / \  \n"
            "       \n"
            "^^^^^^^\n",

            "       \n"
            " \   / \n"
            "  \ /  \n"
            "   O   \n"
            "  /|\  \n"
            "  / \  \n"
            "       \n"
            "^^^^^^^\n",

            "       \n"
            "  \ /  \n"
            "   O   \n"
            "  /|\  \n"
            "  / \  \n"
            "       \n"
            "^^^^^^^\n",

            "       \n"
            "   X   \n"
            "  /|\  \n"
            "  / \  \n"
            "       \n"
            "^^^^^^^\n"
            ]
        self._lines_cut = 0