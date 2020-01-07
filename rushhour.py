################################
#   rushhour.py
#   Prints boardgame rush hour
################################


class Rushhour():
    
    def __init__(self, game):
        data = self.load_games(game)

        return 

    def load_games(self, filename):

        # list for returning
        games_data = []

        # load from datafile
        with open(filename, "r") as f:
            game_data = []
            
            for line in f:
                line = line.split()
                game_data.append(line)
            game_data.remove(game_data[0])                                
        return game_data
    
     
if __name__ == "__main__":
    rushhour = Rushhour("games/Rushhour6x6_1.csv")
  