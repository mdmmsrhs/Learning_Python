#!/bin/python

class Card():
    suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rankList = ["narf", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",\
                "Jack", "Queen", "King"]
    def __init__(self, suit=0, rank=2):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return (self.rankList[self.rank] + " of " + self.suitList[self.suit])

    def __cmp__(self, other):
        # check the suits
        if self.suit > other.suit : return 1
        if self.suit < other.suit: return -1
        # check for aces
        if self.rank == 1 and other.rank > 1: return 1
        if self.rank > 1 and other.rank == 1: return -1
        # suits are the same, check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # it's a draw
        return 0

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " "*i + str(self.cards[i]) + "\n"
        return s

    def printDeck(self):
        for card in self.cards:
            print card

    def shuffle(self):
        import random
#        nCards = len(self.cards)
#        for i in range(nCards):
#           j = random.randrange(i, nCards)
#            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
        """shuffle without a sequence call using a builtin function"""
        random.shuffle(self.cards)

    def removeCard(self,card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def popCard(self):
        # deal from the bottom of the deck
        return self.cards.pop()

    def dealCard(self):
        # deal from the top of the deck
        return self.cards.pop(0)

    def isEmpty(self):
        return (len(self.cards) == 0)

    def deal(self,hands,nCards = 999):
        nHands = len(hands)
        for i in range(nCards):
            if self.isEmpty(): break
            card = self.popCard()
            hand = hands[i % nHands]
            hand.addCard(card)

class Hand(Deck):
    def __init__(self, name=""):
        self.cards=[]
        self.name=name

    def addCard(self,card):
        self.append(card)

def main():
    # threeOfClubs = Card(3,1)
    # print threeOfClubs
    #
    # card1 = Card(1,11)
    # card2 = Card(1,3)
    # card3 = Card(2,4)
    # card4 = Card(2,5)
    # card5 = Card(2,1)
    # card6 = Card(1,5)
    # card7 = Card(2,4)
    #
    # print card1, card2
    # print card2.suitList[1]
    #
    # print cmp(card3,card4)
    # print cmp(card4,card3)
    # print cmp(card3,card7)
    # print cmp(card4,card6)
    # print cmp(card4,card5)

    deck = Deck()
    for i in range(10):
        Deck.shuffle(deck)

    # Deck.printDeck(deck)
    # print deck
    # print deck.isEmpty()
    # card8 = Card(2,6)
    # print card8
    # print(deck.removeCard(card8))
    #
    # print (Deck.dealCard(deck))
    print "Here is your hand: "
    for i in range(0,5):
        print(Deck.dealCard(deck))


if __name__ == '__main__':
    main()

#end