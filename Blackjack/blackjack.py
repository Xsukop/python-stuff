import random

# Konštanty
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


# Trieda pre jednu kartu
class Card:
    def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit


# Trieda pre balíček kariet
class Deck:
    def __init__(self):
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()   


# Trieda pre ruku hráča alebo dealera
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, new_card):
        self.cards.append(new_card)
        self.value += new_card.value
        if new_card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_ace()
        
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# Trieda pre žetóny
class Chips:
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet
        
    def __str__(self):
        return f"Current total chips: {self.total}"


# Pomocné funkcie
def show_all(player_hand, dealer_hand):
    print("\nDealer's Hand:")
    for card in dealer_hand.cards:
        print(f" {card}")
    print(f"Value: {dealer_hand.value}")

    print("\nPlayer's Hand:")
    for card in player_hand.cards:
        print(f" {card}")
    print(f"Value: {player_hand.value}")


def evaluate_game(player_hand, dealer_hand, player_chips):
    if player_hand.value > 21:
        print("Player busts!")
        player_chips.lose_bet()
    elif dealer_hand.value > 21:
        print("Dealer busts! Player wins!")
        player_chips.win_bet()
    elif player_hand.value > dealer_hand.value:
        print("Player wins!")
        player_chips.win_bet()
    elif player_hand.value < dealer_hand.value:
        print("Dealer wins!")
        player_chips.lose_bet()
    else:
        print("Push! It's a tie.")


def hit(deck, hand):
    hand.add_card(deck.deal_one())


def stand():
    global playing
    print("Player stands. Dealer is playing.")
    playing = False


# Hlavný herný cyklus
player_chips = Chips()

while True:
    # Vytvor a zamiešaj balíček
    deck = Deck()
    deck.shuffle()

    # Vytvor ruky
    player_hand = Hand()
    dealer_hand = Hand()

    # Rozdaj po 2 karty
    for _ in range(2):
        player_hand.add_card(deck.deal_one())
        dealer_hand.add_card(deck.deal_one())

    # Zadaj stávku
    while True:
        try:
            bet = int(input(f"\nYou have {player_chips.total} chips. How many chips would you like to bet? "))
        except ValueError:
            print("Please enter a valid integer.")
        else:
            if bet > player_chips.total:
                print("You don't have enough chips!")
            else:
                player_chips.bet = bet
                break

    # Hráčov cyklus
    playing = True
    while playing:
        print("\nDealer's Hand:")
        print(" <card hidden>")
        print(f" {dealer_hand.cards[1]}")

        print("\nPlayer's Hand:")
        for card in player_hand.cards:
            print(f" {card}")
        print(f"Value: {player_hand.value}")

        choice = input("\nWould you like to Hit or Stand? Enter 'h' or 's': ")

        if choice.lower() == 'h':
            hit(deck, player_hand)
            if player_hand.value > 21:
                break

        elif choice.lower() == 's':
            stand()
        else:
            print("Sorry, please enter 'h' or 's' only.")
            continue

    # Dealer hrá, ak hráč neprehral
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

    # Vyhodnotenie
    show_all(player_hand, dealer_hand)
    evaluate_game(player_hand, dealer_hand, player_chips)
    print(player_chips)

    # Nová hra?
    if player_chips.total <= 0:
        print("You're out of chips! Game over.")
        break

    new_game = input("\nWould you like to play another hand? (y/n): ")
    if new_game.lower() != 'y':
        print("Thanks for playing!")
        break
