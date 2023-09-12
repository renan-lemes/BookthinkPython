import random 
## Exercicios do cap 18
## Ec 18.1 ✅
## Ex 18.2

class Card :
    """
    Representa as cartas
        suit -> espadas etc ...
        rank -> qual carta 
    """
    def __init__(self, suit = 0 , rank = 2 ): 
        self.suit = suit
        self.rank = rank
    suit_names = ['Paus', 'Ouros', 'Copas', 'Espadas']
    rank_name = [None, 'As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
    def __str__(self) -> str:
        return '%s de %s' % (Card.rank_name[self.rank], Card.suit_names[self.suit])
    
    def __lt__(self, other):
        ## para conferir os naipes
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False

        ## Comparacao de tuplas
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    ''' 
        Inicializando meu deck aqui 
    '''
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    def __str__(self) -> str:
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)

    def suffle(self):
        ''' 
            Pegar uma carta aleatoria
        '''
        random.shuffle(self.cards)

class Hand(Deck):
    '''
        Representa a mao do jogador
    '''
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())





## exemplo 
# queen_diamonds = Card(1, 12)

# print(queen_diamonds)

hand = Hand('new hand')
deck = Deck()

# print(deck)

card = deck.pop_card()
hand.add_card(card)
# print(hand)