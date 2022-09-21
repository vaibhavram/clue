class Player:
    def __init__(self, name):
        self.name = name
        self.candidates = {
            "person": set("Peacock", "Scarlet", "Plum", "Green", "Mustard", "White"),
            "weapon": set("Candlestick", "Rope", "Pistol", "Knife"),
            "room": set("Living Room", "Hall", "Dining Room", "Kitchen", "Spa")
        }
        self.cards = {
            "person": set(),
            "weapon": set(),
            "room": set()
        }

    @abstractmethod
    def should_accuse(self):
        pass

    @abstractmethod
    def accuse(self):
        pass

    @abstractmethod
    def guess(self):
        pass

    def has_card(self, type, card):
        return(card in self.cards(type))