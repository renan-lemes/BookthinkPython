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
        self.rank = 2
    suit_names = ['Paus', 'Ouros', 'Copas', 'Espadas']
    rank_name = [None, 'As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
    def __str__(self) -> str:
        return '%s de %s' % (Card.rank_name[self.rank], Card.suit_names[self.suit]) 

## exemplo 
queen_diamonds = Card(1, 12)

print(queen_diamonds)
