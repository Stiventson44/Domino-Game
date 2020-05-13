import random

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

    @staticmethod
    def shuffle_dominoes(dominoes):
        for i in range(len(dominoes)):
            random_position = random.randrange(len(dominoes))
            dominoes[i], dominoes[random_position] = dominoes[random_position], dominoes[i]

    def create_players(self, number_of_players):
        players = []
        for i in range(number_of_players):
            players.append(self.player_class(i))
        return players

    @staticmethod
    def distribute_dominoes(dominoes, players):
        for player in players:
            player.dominoes = dominoes[0:7]
            dominoes = dominoes[7:]
        return dominoes

    def get_game_data(self, number_of_players):
        #creating dominoes
        dominoes = self.create_dominoes()
        #shuffling dominoes
        self.shuffle_dominoes(dominoes)
        #creating players objects
        players = self.create_players(number_of_players)
        #distribute dominoes
        dominoes = self.distribute_dominoes(dominoes, players)
        return players, dominoes