import random
from player import Player

class Main:
    def __init__(self, players):
        self.players = players
        self.deck = {
            "person": set(["Peacock", "Scarlet", "Plum", "Green", "Mustard", "White"]),
            "weapon": set(["Candlestick", "Rope", "Pistol", "Knife"]),
            "room": set(["Living Room", "Hall", "Dining Room", "Kitchen", "Spa"])
        }
        self.envelope = {
            "person": None,
            "weapon": None,
            "room": None
        }
        for player in players:
            player.assign_game(self)

    def deal(self):
        self.envelope["person"] = self.deck["person"].pop()
        self.envelope["weapon"] = self.deck["weapon"].pop()
        self.envelope["room"] = self.deck["room"].pop()
        # print("Envelope: " + str(self.envelope))
        n_cards = sum([len(v) for v in self.deck.values()])
        player_index = 0
        while n_cards > 0:
            r = random.randint(0, n_cards - 1)
            # deciding which card to deal
            if r < len(self.deck["person"]):
                self.players[player_index].deal("person", self.deck["person"].pop())
            elif r < len(self.deck["person"]) + len(self.deck["weapon"]):
                self.players[player_index].deal("weapon", self.deck["weapon"].pop())
            else:
                self.players[player_index].deal("room", self.deck["room"].pop())
            # incrementing player to deal to
            if player_index == len(self.players) - 1:
                player_index = 0
            else:
                player_index += 1
            n_cards -= 1
        # printing cards for dealer confirmation
        # for player in players:
        #     print(player.name + str(player.cards))

    def check_envelope(self, person, weapon, room):
        return(self.envelope["person"] == person and self.envelope["weapon"] == weapon and self.envelope["room"] == room)

    def game(self):
        self.deal()
        return(None)

players = [Player("Vaibhav"), Player("Kaanchana"), Player("Sruthi"), Player("Rohith")]
game = Main(players)
winner = game.game()
print(winner)