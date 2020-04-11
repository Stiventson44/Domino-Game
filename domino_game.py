import random

class Player:
    points = 0
    
    def __init__(self, dominoes, id):
        self.dominoes = dominoes
        self.id = id

    #setting how the player_class object will be displayed
    def __str__(self):
        return "Player {}".format(self.id + 1)

class Domino:

    def __init__(self, top_value, bottom_value):
        self.top_value = top_value
        self.bottom_value = bottom_value

    #setting how the domino_class object will be displayed
    def __str__(self):
        return "[{}|{}]".format(self.top_value, self.bottom_value)

class Game_data:

    def __init__(self, player_class, domino_class):
        self.player_class = player_class
        self.domino_class = domino_class

    def create_dominoes(self):
        dominoes = []
        for i in range(7):
            for j in range(i,7):        
                dominoes.append(self.domino_class(i, j))
        return dominoes

    def shuffle_dominoes(self, dominoes):
          for i in range(len(dominoes)):
            random_position = random.randrange(len(dominoes))
            dominoes[i], dominoes[random_position] = dominoes[random_position], dominoes[i]

    def create_players(self, dominoes, number_of_players):
        players = []
        for i in range(number_of_players):
            #create a player_class object giving the player 7 dominoes and giving him an unique id
            players.append(self.player_class(dominoes[0:7], i))
            #remove 7 dominoes
            dominoes = dominoes[7:]
        return players, dominoes

#object that contains the functionality of creating the game data
game_data = Game_data(Player, Domino)
#creating dominoes
dominoes = game_data.create_dominoes()
#shuffling dominoes
game_data.shuffle_dominoes(dominoes)
#creating players objects
players, dominoes = game_data.create_players(dominoes, 3)

