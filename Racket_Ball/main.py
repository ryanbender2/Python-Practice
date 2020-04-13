"""Main class for game."""

from player import Player
from game import Game

class RacquetBall(object):
    def __init__(self, player1_name, player2_name, player1_prob, player2_prob, num_games):
        """Simulate racquetball games!
        
        Arguments:
            player1_name {str} -- Name of player 1.
            player2_name {str} -- Name of player 2.
            player1_prob {float} -- Player 1's probability of winning rally.
            player2_prob {float} -- Player 2's probability of winning rally.
            num_games {int} --  Number of games to simulate.
        """
        self.player1 = Player(player1_name, player1_prob)
        self.player2 = Player(player2_name, player2_prob)
        self.num_games = num_games

    def simulate_games(self, watch_game=False):
        for _ in range(self.num_games):
            # simulate game
            game = Game(self.player1.probability, self.player2.probability)
            game.play(watch_game, self.player1.name, self.player2.name)
            
            # add win to players count
            if game.winner == 0 and game.shutout == False:
                self.player1.add_win()
            if game.winner == 0 and game.shutout == True:
                self.player1.add_shutout()
            if game.winner == 1 and game.shutout == False:
                self.player2.add_win()
            if game.winner == 1 and game.shutout == True:
                self.player2.add_shutout()

    def print_stats(self):
        stats = "\nNumber of Games Simulated: {}\n  Player 1 Stats:\n    Name: {}\n    Wins: {}\
                \n    Winning Percentage: {}\n    Shutouts: {}\n\n  Player 2 Stats:\n    Name: {}\
                \n    Wins: {}\n    Winning Percentage: {}\n    Shutouts: {}"\
            .format(self.num_games, self.player1.name, self.player1.wins, round(self.player1.wins / self.num_games, 4), self.player1.shutouts,
                    self.player2.name, self.player2.wins, round(self.player2.wins / self.num_games, 4), self.player2.shutouts)
        print(stats)


def main():
    # take_inputs
    P1_n = input("Player 1's Name: ").split()
    P2_n = input("Player 2's Name: ").split()
    P1_p = input("Player 1's Probablility: ")
    P2_p = input("Player 2's Probablility: ")
    games = input("Number of games to be simulated: ")
    
    # error checks
    try:
        P1_p = round(float(P1_p), 2)
        P2_p = round(float(P2_p), 2)
    except ValueError as err:
        raise Exception('Probability values were not valid: ' + str(err))
    
    try:
        games = int(games)
    except ValueError as err:
        raise Exception('Number of games needs to be readable as int: ' + str(err))
    
    if P1_p > 1 or P2_p > 1:
        raise Exception('Probability values need to be less than 1')  
    
    # format names
    name_format = lambda name: ''.join([name[0].upper()] + [i.lower() for i in name[1:]])
    P1_n = ' '.join(list(map(name_format, P1_n)))
    P2_n = ' '.join(list(map(name_format, P2_n)))

    # run game
    racquetball = RacquetBall(P1_n, P2_n, P1_p, P2_p, games)
    racquetball.simulate_games(watch_game=False)
    racquetball.print_stats()
    

if __name__ == "__main__":
    main()
