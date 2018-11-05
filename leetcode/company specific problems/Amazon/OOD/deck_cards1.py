import random
class Deck():
    def __init__(self):
        self.cards = []

        #rather than doing inheritance, composition, only referring to a class
        #for a specific task, rather than inheriting all the methods
        for i in range(4):
            for j in range(1, 14):
                card = Card(i, j)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_hand(self, num):

        hand = Hand()
        for _ in range(num):
            card = self.cards.pop()
            hand.card_in_hand.append(card)
        return hand

    def deal_a_card(self, hand):
        card = self.cards.pop()
        hand.card_in_hand.append(card)



class Card(object):
    #instance attributes
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    #class attributes
    suit_lst = ['Diamond', 'King', 'Queen', 'Jack']
    value_lst = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    def __repr__(self):
        return '{} of {}'.format(Card.value_lst[self.value], Card.suit_lst[self.suit])


class Hand(object):
    def __init__(self):
        self.card_in_hand = []

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    hand1 = deck.deal_hand(4)
    deck.deal_a_card(hand1)


