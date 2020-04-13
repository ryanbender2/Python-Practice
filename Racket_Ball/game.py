"""game.py -- Game class."""

from random import choice
from random import shuffle
from time import sleep

class Game(object):
    def __init__(self, p1_prob, p2_prob):
        """Ready to simulate a Racquetball game? Game simulates one game of
            racquetball based on both player's probability of winning each
            rally within the match.
            To begin, call the play method.
    
            Arguments:
                p1_prob {float} -- Player 1's percentage chance of winning a rally
                p2_prob {float} -- Player 2's percentage chance of winning a rally
        """
        self.p1_prob = p1_prob
        self.p2_prob = p2_prob
        self.p1_score = 0
        self.p2_score = 0
        self.shutout = False
        self.winner = None
    
    def _play_game(self, watch_game, n1, n2):
        """Main game function."""
        p1 = [0 for _ in range(int(self.p1_prob * 100))]
        p2 = [1 for _ in range(int(self.p2_prob * 100))]
        player_probabilities = p1 + p2
        shuffle(player_probabilities)
        first_to_serve = choice([0, 1])  # p1 - 0 | p2 - 1
        serving = first_to_serve
        game_finished = False
        rally_counter = 0
        
        # Game loop
        while not game_finished:
            rally_counter += 1
            rally_loser = None
            rally_winner = choice(player_probabilities)
            
            if rally_winner == 0:
                rally_loser = 1
            else:
                rally_loser = 0
    
            if watch_game:
                if serving == 0:
                    _serving = n1
                else:
                    _serving = n2
                
                if rally_winner == 0:
                    _r_w = n1
                else:
                    _r_w = n2
                
                game_stats = "Rally {} | {}'s Score {} | {}'s Score {} | Serving {} | Rally Winner {}"\
                    .format(rally_counter, n1, self.p1_score, n2, self.p2_score, _serving, _r_w)
                print(game_stats)
                sleep(2)
    
            if rally_winner == serving:
                if rally_winner == 0:
                    self.p1_score += 1
                else:
                    self.p2_score += 1
            
            if rally_loser == serving:
                serving = rally_winner
            
            if self.p1_score == 15:
                game_finished = True
                self.winner = 0
            if self.p2_score == 15:
                game_finished = True
                self.winner = 1
            if self.p1_score == 7 and self.p2_score == 0:
                game_finished = True
                self.shutout = True
                self.winner = 0
            if self.p2_score == 7 and self.p1_score == 0:
                game_finished = True
                self.shutout = True
                self.winner = 1

    def play(self, watch_game, n1, n2):
        """Start game."""
        self._play_game(watch_game, n1, n2)
