class Deck(object):
    def __init__(self):
        self.cards = []

        #rather than doing inheritance, composition, only referring to a class
        #for a specific task, rather than inheriting all the methods
        for i in range(4):
            for j range(1, 14):
                card = Card(i, j)
                self.cards.append(card)


class Card(object):
    #instance attributes
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    #class attributes
    self.suit_lst = ['Diamond', 'King', 'Queen', 'Jack']
    self.value_lst = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9,'Jack', 'Queen', 'King']

    def __repr__(self):
        return '{} of {}'.format(Card.value_lst[self.value], Card.suit_lst[self.suit])


# class Hand(object):


if __name__ == '__main__':
    deck = Deck()


