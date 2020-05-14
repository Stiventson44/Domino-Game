class Domino:

    def __init__(self, top_value, bottom_value):
        self.top_value = top_value
        self.bottom_value = bottom_value

    #setting how the domino object will be displayed
    def __str__(self):
        return "[{}|{}]".format(self.top_value, self.bottom_value)
