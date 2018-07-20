#Design the data structures for a generic deck of cards, explain how you would subclass
#the data structures to implement blackjack


#clarifying questions to ask during interview:
#what do you mean by generic, are we assuming this is a standard deck of cards

# helpful resource: https://en.wikibooks.org/wiki/Think_Python/Inheritance

# Spades -> 3
# Hearts -> 2
# Diamonds -> 1
# Clubs -> 0


# Jack -> 11
# Queenv -> 12
# King -> 13

import random

class Card(object):
    """implementing basic playing card"""
    #default card is 2 of clubs
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['None', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __repr__(self):
        return "{}_of_{}".format(Card.rank_names[self.rank], Card.suit_names[self.suit])


class Deck(object):
    """create a deck from the cards"""

    def __init__(self):
        self.reset()

    def deal(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def add(self, card):
        if card in self.cards:
            print "card already in deck"
        else:
            self.cards.append(card)

    def reset(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)
        return random.shuffle(self.cards)

    def deal_hand(self, number):
        return [self.deal() for _ in range(number)]

    def move_cards(self, hand, nums):

        for card in range(nums):
            hand.add(self.deal())


    def __repr__(self):
        result = [str(card) for card in self.cards]
        print len(result)
        return "\n".join(result)

class Hand(Deck):

    def __init__(self, cards=[]):
        self.cards = cards

    def score(self):
        score = 0
        for card in self.cards:
            score += card.value()

        return score

class BlackJackCard(Card):

    def __init__(self, suit, rank)):
        super(BlackJackCard, self).__init__(suit, rank)

    def value(self):
        if is_ace():
            return 1
        elif self.rank >= 11 and self.rank <= 13:
            return 10
        else:
            return self.rank

    def min_value(self):
        return self.value(

    def max_value(self):
        if self.rank ==1:
            return 11
        else:
            return self.value()

    def is_ace(self):
        return self.rank == 1


class BlackJackHand(Hand):

    def __init__(self, cards=[]):
        super(BlackJackHand, self).__init__(cards)

    def poss_scores(self):
        scores = [0]
        for card in self.cards:
            for i in range(len(scores)):
                scores[1] += card.value()
            if card.is_ace():
                new_scores = score.copy()
                for i in range(len(new_scores))





