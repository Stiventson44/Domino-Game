import player, domino_tile, game_data as gd, game_logic as gl

def number_of_players_validation():
  while(True):
    number_of_players = input()
    if len(number_of_players) == 1 and number_of_players.isdigit() and (int(number_of_players) > 1 and int(number_of_players) < 5):
      return int(number_of_players)
    else:
      print("wrong input")

def points_to_win_validation():
  while(True):
    points_to_win = input()
    if len(points_to_win) > 0 and points_to_win.isdigit() and int(points_to_win) > 0:
      return int(points_to_win)
    else:
      print("Wrong input")

def game_setup():
    print('how many players are going to play?')
    number_of_players = number_of_players_validation()
    print("what's limit of points to win that you want to set?")
    points_to_win = points_to_win_validation()
    #create game data object
    game_data = gd.Game_data(player.Player, domino_tile.Domino)
    #create game logic object 
    game_logic = gl.Game_logic(game_data, points_to_win, number_of_players)
    #start the game
    game_logic.game_start()

game_setup()