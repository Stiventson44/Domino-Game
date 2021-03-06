class Game_logic:
    turn = 0
    game_table = []
    in_game = True
    dominoes = []

    def __init__(self, game_data, points_to_win, number_of_players):
        self.game_data = game_data
        self.points_to_win = points_to_win
        self.number_of_players = number_of_players
    
    def game_loop(self):
        while(self.in_game):
            current_player = self.players[self.turn]
            print("{} turn".format(current_player))
            self.show_current_player_dominoes()
            #if game is locked
            if self.is_game_locked():
                print("game is locked, restarting the game")
                self.reset_round()
                self.first_move()

            #if is a capicua
            elif len(current_player.dominoes) == 1 and self.can_play_left([current_player.dominoes[0]]) and self.can_play_right([current_player.dominoes[0]]):
                self.play_validation()
                self.show_game_table()
                print("{} Capicua! + 25 points".format(current_player))
                current_player.points += 25
                self.if_anyone_wins_logic()
    
            #if the current player is able to play with his dominoes
            elif self.can_play(current_player.dominoes):
                self.play_validation()
                self.show_game_table()
                if len(current_player.dominoes) == 0:
                    self.if_anyone_wins_logic()
                else:
                    self.change_turn()

            #if player is not able to play then refill
            else:
                print("you can't play with any domino")
                if len(self.dominoes) > 0:
                    self.refill()
                else:
                    print("there is no dominoes left to refill")
                    self.change_turn()

    def is_game_locked(self):
        if len(self.dominoes) == 0:
            for player in self.players:
                if self.can_play(player.dominoes):
                    return False
            return True 
        else:
            return False

    def if_anyone_wins_logic(self):
        current_player = self.players[self.turn]
        self.add_points(self.turn)
        if current_player.points >= self.points_to_win:
            print("{} won the game with {} points".format(current_player, current_player.points))
            self.in_game = False
        else:
            print("{} won this round, now have {} points".format(current_player, current_player.points))
            self.reset_round()

    def reset_round(self):
        self.game_table = []
        self.dominoes = self.game_data.create_dominoes()
        self.game_data.shuffle_dominoes(self.dominoes)
        self.dominoes = self.game_data.distribute_dominoes(self.dominoes, self.players)
    
    #refill current player dominoes
    def refill(self):
        self.players[self.turn].dominoes.append(self.dominoes[0])
        del self.dominoes[0]
        print("+1 domino")

    #add all the points of the opposing players to the current player points
    def add_points(self, player_id):
        winner_points = 0
        for player in self.players:
            if not player == self.players[player_id]:
                for domino in player.dominoes:
                    winner_points += domino.top_value
                    winner_points += domino.bottom_value
        self.players[player_id].points += winner_points

    def can_play_right(self, dominoes):
        if len(self.game_table) == 0:
            return True
        else:
            for domino in dominoes:
                if domino.top_value == self.game_table[-1].bottom_value or domino.bottom_value == self.game_table[-1].bottom_value:
                    return True
        return False

    def can_play_left(self, dominoes):
        if len(self.game_table) == 0:
            return True
        else:   
            for domino in dominoes:
                if domino.bottom_value == self.game_table[0].top_value or domino.top_value == self.game_table[0].top_value:
                    return True
        return False        
    
    def can_play(self, dominoes):
        if self.can_play_left(dominoes) or self.can_play_right(dominoes):
            return True
        else:
            return False

    @staticmethod
    def split_input():
        while(True):
            string = input()
            if len(string) == 2:
                domino_num = string[0]
                side = string[1]
                return domino_num, side
            elif len(string) == 3:
                domino_num = string[0:2]
                side = string[2]
                return domino_num, side
            else:
                print('wrong input, try again')
    
    @staticmethod
    def side_validation(side):
        if len(side) == 1 and (side == 'A' or side == 'D' or side == 'a' or side == 'd'):
            return True
        print("wrong input, try again")
        return False

    def domino_num_validation(self, domino_num):
        player_dominoes = self.players[self.turn].dominoes
        if len(domino_num) == 1 and domino_num.isdigit() and int(domino_num) <= len(player_dominoes):
            return True
        elif len(domino_num) == 2 and domino_num.isdigit() and int(domino_num) <= len(player_dominoes):
            return True
        print("wrong input, try again")      
        return False   

    def play_validation(self):
        while(True):
            if len(self.game_table) == 0:
                domino_num = input()
                side = ''
                if self.domino_num_validation(domino_num):
                    domino_index = int(domino_num) - 1
                    if self.move_validation(domino_index, side):
                        break
            else:
                domino_num, side = self.split_input()
                if self.domino_num_validation(domino_num) and self.side_validation(side):
                    domino_index = int(domino_num) - 1
                    if self.move_validation(domino_index, side):
                        break
                
    def move_validation(self, domino_index, side):
        selected_domino = self.players[self.turn].dominoes[domino_index]
        if len(self.game_table) == 0:
            self.play(domino_index)
            return True
        if (side == 'a' or side == 'A') and self.can_play_left([selected_domino]):
            self.play_left(domino_index)
            return True
        elif (side == 'd' or side == 'D') and self.can_play_right([selected_domino]):
            self.play_right(domino_index)
            return True
        else:
            print("invalid move")
            return False        
 
    @staticmethod
    def flip_domino(domino):
        domino.top_value, domino.bottom_value = \
        domino.bottom_value, domino.top_value

    def play_left(self, domino_index):
        selected_domino = self.players[self.turn].dominoes[domino_index]
        #if the domino is backwards then flip it and make the move
        if self.game_table[0].top_value == selected_domino.top_value:
            self.flip_domino(selected_domino)
            self.game_table.insert(0, selected_domino)
            del self.players[self.turn].dominoes[domino_index]
        else:
            self.game_table.insert(0, selected_domino)
            del self.players[self.turn].dominoes[domino_index]

    def play_right(self, domino_index):
        selected_domino = self.players[self.turn].dominoes[domino_index]
        #if the domino is backwards then flip it and make the move
        if self.game_table[-1].bottom_value == selected_domino.bottom_value:
            self.flip_domino(selected_domino)
            self.game_table.append(selected_domino)
            del self.players[self.turn].dominoes[domino_index]
        else:
            self.game_table.append(selected_domino)
            del self.players[self.turn].dominoes[domino_index]

    def play(self, domino_index):
        self.game_table.append(self.players[self.turn].dominoes[domino_index])
        del self.players[self.turn].dominoes[domino_index]         
           
    def show_game_table(self):
        print("Game table: ", end="")
        for domino in self.game_table:
            print("{}".format(domino), end="")
        print("")

    def show_current_player_dominoes(self):
        current_player = self.players[self.turn]
        print("{} dominoes: ".format(current_player), end="")
        for i in range(len(current_player.dominoes)):
            print("{}){} ".format(i + 1, current_player.dominoes[i]), end="")
        print("")

    def change_turn(self):
        if self.turn + 1 < len(self.players):
            self.turn += 1
        else:
            self.turn = 0

    #get the player's index and domino index of the player that have the biggest double domino
    def get_biggest_double(self):
        biggest = 0
        for player in self.players:
            for domino in player.dominoes:
                if domino.top_value == domino.bottom_value and domino.top_value > biggest:
                    biggest = domino.top_value
                    domino_index = player.dominoes.index(domino)
                    player_index = self.players.index(player)
        return  player_index, domino_index

    def first_move(self):
        player_index, domino_index = self.get_biggest_double()
        self.turn = player_index
        print("{} Has the highest double and plays first".format(self.players[player_index]))
        self.play(domino_index)
        self.show_game_table()
        self.change_turn()
            
    def game_start(self):
        self.players, self.dominoes = self.game_data.get_game_data(self.number_of_players)
        self.first_move()
        self.game_loop()
