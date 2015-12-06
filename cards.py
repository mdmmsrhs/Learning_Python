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

def main():
    threeOfClubs = Card(3,1)
    print threeOfClubs

    card1 = Card(1,11)
    card2 = Card(1,3)
    print card1, card2

if __name__ == '__main__':
    main()

#end

