import random

class Player:
    def __init__(self, name):
        self.name = name
        self.candidates = {
            "person": ["Peacock", "Scarlet", "Plum", "Green", "Mustard", "White"],
            "weapon": ["Candlestick", "Rope", "Pistol", "Knife"],
            "room": ["Living Room", "Hall", "Dining Room", "Kitchen", "Spa"]
        }
        self.cards = {
            "person": set(),
            "weapon": set(),
            "room": set()
        }
        self.game = None

    def get_name(self):
        return(self.name)

    def assign_game(self, game):
        self.game = game

    def deal(self, type, card):
        self.cards[type].add(card)
        self.candidates[type].remove(card)

    def should_accuse(self):
        return(all([elem == 1 for elem in [len(v) for v in self.candidates.values()]]))

    def accuse(self):
        person = random.sample(self.candidates["person"], 1)[0]
        weapon = random.sample(self.candidates["weapon"], 1)[0]
        room = random.sample(self.candidates["room"], 1)[0]
        return(self.game.check_envelope(person, weapon, room))

    def guess(self):
        options = ["person", "weapon", "room"]
        type1, type2 = random.sample(options, 2)
        card1 = random.sample(self.candidates[type1], 1)[0]
        card2 = random.sample(self.candidates[type2], 1)[0]
        return(type1, card1, type2, card2)

    def show_card(self, type1, card1, type2, card2):
        if card1 in self.cards[type1] and card2 in self.cards[type2]:
            if random.randint(0,1) == 0:
                return(type1, card1)
            else:
                return(type2, card2)
        elif card1 in self.cards[type1]:
            return(type1, card1)
        elif card2 in self.cards[type2]:
            return(type2, card2)
        else:
            return(None, None)

    def process_shown_card(self, shower, type, card, guesstype1 = None, guesscard1 = None, guesstype2 = None, guesscard2 = None):
        if not shower:
            if guesscard1 not in self.cards[guesstype1]:
                self.candidates[guesstype1] = set([guesscard1])
            if guesscard2 not in self.cards[guesstype2]:
                self.candidates[guesstype2] = set([guesscard2])
        elif card in self.candidates[type]:
            self.candidates[type].remove(card)








