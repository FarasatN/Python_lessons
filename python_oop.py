# class Dog():
#     # class object attribute
#     species='mammals'
#     def __init__(self,breed,name):
#         self.breed=breed
#         self.name=name
#
# mydog=Dog(breed='lab',name='lucky')
# print(mydog.breed)
# print(mydog.name)

# class Circle():
#     pi=3.14
#     def __init__(self,radius=1):
#         self.radius=radius
#     def area(self):
#         return self.radius*self.radius*Circle.pi
#
# myc=Circle(2)
# print(myc.area())

# #inheritance
# class Animal():
#     def __init__(self):
#         print('ANIMAL CREATED')
#     def whoami(self):
#         print('ANIMAL')
#     def eat(self):
#         print('EATING')
#
# class Dog(Animal):
#     def __init__(self):
#         # Animal.__init__(self)
#         print('DOG CREATED')
#     def bark(self):
#         print('WOOF')
#     def eat(self):
#         print('DOG EATING')
#
#
# myd=Dog()
# myd.whoami()
# myd.eat()
# myd.bark()

# special methods
# class Book():
#     def __init__(self,title,author,pages):
#         self.title=title
#         self.author=author
#         self.pages=pages
#     def __str__(self):
#         return "title: {}, author: {}, pages: {}".format(self.title(),self.author(),self.pages())
#
# b=Book('Python','jose',200)
# print(b)




# CARD WARGAME PROJECT

# mycards= [(s,r for s in SUITE for r in RANKS )]
# mycards= []
# for r in RANKS:
#     for s in SUITE:
#         mycards.append((s,r))

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players.
    """
    def __init__(self):
        print("Creating New Ordered Deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS ]

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])

class Hand:
    '''
    This is the Hand class. Each player has a hand, and can add or remove
    cards from that hand.
    '''
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        print('\n')
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop(0))
            return war_cards

    def still_has_cards(self):
        """
        Returns True if player still has cards
        """
        return len(self.hand.cards) != 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Create New Deck and split in half
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

# Create Both Players
comp = Player("computer",Hand(half1))
name = input("What is your name player? ")
user = Player(name,Hand(half2))

# Set Round Count
total_rounds = 0
war_count = 0
# Let's play
while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(user.name+" count: "+str(len(user.hand.cards)))
    print(comp.name+" count: "+str(len(comp.hand.cards)))
    print("Both players play a card!")
    print('\n')

    # Cards on Table represented by list
    table_cards = []

    # Play cards
    c_card = comp.play_card()
    p_card = user.play_card()

    # Add to table_cards
    table_cards.append(c_card)
    table_cards.append(p_card)

    # Check for War!
    if c_card[1] == p_card[1]:
        war_count +=1
        print("We have a match, time for war!")
        print("Each player removes 3 cards 'face down' and then one card face up")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        # Play cards
        c_card = comp.play_card()
        p_card = user.play_card()

        # Add to table_cards
        table_cards.append(c_card)
        table_cards.append(p_card)

        # Check to see who had higher rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add(table_cards)

    else:
        # Check to see who had higher rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add(table_cards)

print("Great Game, it lasted: "+str(total_rounds))
print("A war occured "+str(war_count)+" times.")
