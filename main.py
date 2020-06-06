import random

class Card (object):
  def __init__(self,suit,value):
    self.suite=suit
    self.value=value

  def show(self):
    print ( "{} of {}".format(self.value,self.suite))

class Deck(object):
  def __init__(self):
    self.cards=[]
    self.build()

  def build(self):
    for s in ["Spades","Clubs","hearts","Diamonds"]:
        for v in range(1,14):
          self.cards.append(Card(s,v))
           #print ("{} of {}".format(v,s))

  def show(self):
    for c in self.cards:
      c.show()

  def shuffle(self):
    for i in range(len(self.cards)-1,0,-1):
      r = random.randint(0,i)
      self.cards[i],self.cards[r]=self.cards[r],self.cards[i]
      
  def draw(self):
    return self.cards.pop()

class Player (object):
  def __init__(self,name):
    self.hand=[]
    self.name=name

  def draw (self, deck):
    self.hand.append(deck.draw())
    return self

  def showhand(self):
    for card in self.hand:
      card.show()

#card = Card("Clubs",8)
#card.show()

dec= Deck()
dec.shuffle()
#dec.show()
bob = Player("bob")
bob.draw(dec).draw(dec)
bob.showhand()

#ard=dec.draw()
#card.show()