# https://en.wikibooks.org/wiki/Think_Python/Inheritance#Decks

# Design data structures for generic deck of cards. 

# Lets assume that the deck is a standard 52-card set


#52 deck of card: spades(13, black), clubs(13,black), hearts(13, red),
# diamond(13,red)


#Encoding for Suits
# Spades  ---->  3
# Hearts  ---->   2
# Diamonds ---->   1
# Clubs   ---->   0

import random

class Card(object):
    def __init__(self, suit, value):
        #instance attribute
        self.suit = suit
        self.rank = value

    #class attributes
    suit_name = ['Club', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2','3','4','5','6','7','8','9','10',
                    'Jack', 'Queen', 'King']

    def __repr__(self):
        return ' {} of {} '.format(Card.rank_names[self.rank],
                                    Card.suit_name[self.suit])

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for num in range(1,14):
                card = Card(suit, num)
                self.cards.append(card)

    def __repr__(self):
        ret = [str(card) for card in self.cards]
        return ' '.join(ret)


    def add_card(self, card):
     
        self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()


    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    def sort_card_deck(self):
        self.cards.sort()
        return self

    def move_cards_to_hand(self, num, hand):

        for i in range(num):
            hand.add_card(self.pop_card())

        return hand.cards

    def deal_card(self, num):

        dealt_cards = []
        for i in range(num):
            dealt_cards.append(self.cards.pop())

        return dealt_cards

    def deal_hand(self, num_hands, num_cards_per_hand):
        hands = []
        count = 0
        for i in range(num_hands):
            count += 1
            hand = Hand('player {} hand '.format(count))
            cards_in_hand = deck.deal_card(num_cards_per_hand)
            print hand, ': ', cards_in_hand
            hands.append(cards_in_hand)


        return




#Hand is child of Deck, inheriting from Deck
#multiple scores for blackjack hand, goal is to return highest score
#that's under 21 or the lowest score thats over

class Hand(Deck):
    """Represents hand of playing cards"""
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def __repr__(self):
        return self.label

    def return_card_to_deck(self, num, deck):
        for i in range(num):
            deck.cards.append(self.pop_card())


class BlackJackHand(Hand):


    #Jack, Queen, King ==> 10
    #Ace either 11 or 1
    def possible_score(self, hand):
        """return list of all possible scores
        this hand could have evaluating Aces as both 1 and 11"""


        return hand.cards



# class BlackJackCard(Card):


if __name__ == '__main__':
    # card1 = Card(2,11)
    # print card1
    deck = Deck()
    # print deck
    # print '################################################################################'
    # deck.shuffle()
    # print deck
    # print '################################################################################'
    # deck.shuffle()
    # print deck
    # print '################################################################################'
    # print deck.sort_card_deck()
    hand1 = Hand('Gabriela Hand')
    deck.shuffle()
    deck.move_cards_to_hand(2, hand1)
    print hand1.cards
    # black_jack_hand = BlackJackHand(Hand)
    # print black_jack_hand.possible_score(hand1)
    # deck.shuffle()
    # card = deck.pop_card()
    # hand.add_card(card)
    # card = deck.pop_card()
    # hand.add_card(card)
    # print hand.cards
    # deck.move_cards_(4, hand)
    # print hand.cards
    # hand.return_card_to_deck(3, deck)
    # print hand.cards
    # print deck.deal_hand(2,5)

