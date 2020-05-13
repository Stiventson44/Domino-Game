class Player:
    points = 0
    dominoes = []

    def __init__(self, id):
        self.id = id

    #setting how the player_class object will be displayed
    def __str__(self):
        return "Player {}".format(self.id + 1)