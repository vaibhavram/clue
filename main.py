from player import Player

class Main:
    def __init__(self, players):
        self.players = players
        self.deck = {
            "person": set("Peacock", "Scarlet", "Plum", "Green", "Mustard", "White"),
            "weapon": set("Candlestick", "Rope", "Pistol", "Knife"),
            "room": set("Living Room", "Hall", "Dining Room", "Kitchen", "Spa")
        }
        self.envelope = {
            "person": set(),
            "weapon": set(),
            "room": set()
        }

    def game():
        pass

players = [Player("Vaibhav"), Player("Kaanchana")]
game = Main(players)
winner = game.game()