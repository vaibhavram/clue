import sys
from player import Player
from vplayer import VPlayer
from main import Main

types = sys.argv[1:5]
N = int(sys.argv[5])
wins = {}

for run in range(N):
    players = []
    for i in range(4):
        if types[i] == "p":
            players.append(Player("Player " + str(i)))
        elif types[i] == "v":
            players.append(VPlayer("Player " + str(i)))
        else:
            raise ValueError(types[i] + " not a valid player type")
    game = Main(players)
    winner = game.game()
    wins[winner] = wins.get(winner, 0) + 1

for player in players:
    print(player.get_name() + ": " + str(wins[player.get_name()] / N))