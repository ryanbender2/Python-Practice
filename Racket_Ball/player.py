"""player.py -- Player class."""

class Player(object):
    def __init__(self, name, probability):
        """The player class holds all the information on
            each of the players playing racquetball.
        
        Arguments:
            name {str} -- Name of the player.
            probability {float} -- Player's percentage chance of winning a rally
        """
        self.name = name
        self.probability = probability
        self.wins = 0
        self.shutouts = 0
    
    def add_win(self):
        """Adds one to player's win counter."""
        self.wins += 1
    
    def add_shutout(self):
        """Adds win and shutout to player's counts."""
        self.wins += 1
        self.shutouts += 1