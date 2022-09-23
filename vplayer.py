from player import Player

class VPlayer(Player):
    def __init__(self, name):
        Player.__init__(name)

    def should_accuse(self):
        pass

    def accuse(self):
        pass

    def guess(self):
        pass

    def show_card(self, type1, card1, type2, card2):
        pass

    def process_shown_card(self, shower, type, card, guesstype1 = None, guesscard1 = None, guesstype2 = None, guesscard2 = None):
        pass