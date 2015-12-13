#!usr/bin/python

import cards

class Hand(cards.Deck):
    def __init__(self, name=""):
        self.cards=[]
        self.name=name
    
    def addCard(self,card):
        self.cards.append(card)
    
def main():
    if __name__ == '__main__':
        main()
        
#end