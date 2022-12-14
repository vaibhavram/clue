import random
from player import Player
from vplayer import VPlayer

class Main:
    def __init__(self, players, verbose = False):
        self.players = players
        # need some notion of which players are active/inactive in the game
        self.verbose = verbose
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
        if self.verbose:
            print("Envelope: " + str(self.envelope))
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
        #     print(player.name + str(player.candidates))

    def check_envelope(self, person, weapon, room):
        return(self.envelope["person"] == person and self.envelope["weapon"] == weapon and self.envelope["room"] == room)

    def game(self):
        self.deal()
        n = 0
        turn_index = 0
        winner = None
        while not winner:
            if self.verbose:
                print()
                print("--TURN " + str(n) + ": " + self.players[turn_index].get_name() + "--")
                print(self.players[turn_index].candidates)
            if self.players[turn_index].should_accuse():
                if self.players[turn_index].accuse():
                    winner = self.players[turn_index].get_name()
                # since computer cannot handle speed condition, I'll handle accusations in order of turn
                elif self.players[(turn_index + 1) % len(self.players)].should_accuse() and self.players[(turn_index + 1) % len(self.players)].accuse():
                    winner = self.players[(turn_index + 1) % len(self.players)].get_name()
                elif self.players[(turn_index + 2) % len(self.players)].should_accuse() and self.players[(turn_index + 2) % len(self.players)].accuse():
                    winner = self.players[(turn_index + 2) % len(self.players)].get_name()
                elif self.players[(turn_index + 3) % len(self.players)].should_accuse() and self.players[(turn_index + 3) % len(self.players)].accuse():
                    winner = self.players[(turn_index + 2) % len(self.players)].get_name()
                # TODO: handle case where all 4 accuse and all 4 are wrong
            else:
                type1, card1, type2, card2 = self.players[turn_index].guess()
                if self.verbose:
                    print("GUESS: " + self.players[turn_index].get_name() + " guesses " + card1 + ", " + card2)
                shown = False
                for i in range(len(self.players) - 1):
                    type, card = self.players[(turn_index + i + 1) % len(self.players)].show_card(type1, card1, type2, card2)
                    if type and card:
                        shower = self.players[(turn_index + i + 1) % len(self.players)].get_name()
                        if self.verbose:
                            print("SHOW: " + shower + " shows " + card)
                        self.players[turn_index].process_shown_card(shower, type, card)
                        shown = True
                        break
                    else:
                        if self.verbose:
                            print("SHOW: " + self.players[(turn_index + i + 1) % len(self.players)].get_name() + " does not show")
                if not shown:
                    self.players[turn_index].process_shown_card(None, None, None, type1, card1, type2, card2)
            if turn_index == len(self.players) - 1:
                turn_index = 0
            else:
                turn_index += 1
            n += 1
        return(winner)

# players = [VPlayer("Vaibhav"), Player("Kaanchana"), Player("Sruthi"), Player("Rohith")]
# game = Main(players, verbose)
# winner = game.game()
# print("+++++ " + winner.upper() + " WINS +++++")