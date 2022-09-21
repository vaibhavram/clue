class Player:
    def __init__(self, name):
        self.name = name
        self.candidates = {
            "person": set(["Peacock", "Scarlet", "Plum", "Green", "Mustard", "White"]),
            "weapon": set(["Candlestick", "Rope", "Pistol", "Knife"]),
            "room": set(["Living Room", "Hall", "Dining Room", "Kitchen", "Spa"])
        }
        self.cards = {
            "person": set(),
            "weapon": set(),
            "room": set()
        }
        self.game = None

    def assign_game(self, game):
        self.game = game

    def deal(self, type, card):
        self.cards[type].add(card)
        self.candidates[type].remove(card)

    def should_accuse(self):
        return(all([len(v) for v in self.candidates.values() == 1]))

    def accuse(self, person, weapon, room):
        return(self.game.check_envelope(person, weapon, room))

    def guess(self):
        # options = ["person", "weapon", "room"]
        pass

    def has_card(self, type, card):
        return(card in self.cards(type))