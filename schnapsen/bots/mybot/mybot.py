"""
MyBot --
"""

# Import the API objects
from api import State, Deck
import random


class Bot:

    def __init__(self):
        pass

    def get_move(self, state):
        # type: (State) -> tuple[int, int]
        """
        Function that gets called every turn. This is where to implement the strategies.
        Be sure to make a legal move. Illegal moves, like giving an index of a card you
        don't own or proposing an illegal mariage, will lose you the game.
        :param State state: An object representing the gamestate. This includes a link to
            the states of all the cards, the trick and the points.
        :return: A tuple of integers or a tuple of an integer and None,
            indicating a move; the first indicates the card played in the trick, the second a
            potential spouse.
        """

        # All legal moves
        moves = state.moves()
        chosen_move = moves[0]

        # If it is the computers turn
        if state.get_opponents_played_card() is not None:
            case = []
            # Store all cards of the same suit in an array
            for index, move in enumerate(moves):
                if move[0] is not None:
                    if Deck.get_suit(move[0]) == Deck.get_suit(state.get_opponents_played_card()):
                        case.append(move)
      
            # Check if we have the same suit as the opponent
            if len(case) > 0:
                high = []
                for index, move in enumerate(case):
                    if move[0] is not None:
                        # A higher ranked card of the same suit
                        if case[0][0] % 5 <= state.get_opponents_played_card() % 5:
                            high.append(move)
                            chosen_move = move
                # Return the higest card with the same suit
                if len(high) > 0:
                    chosen_move = high[0]
                    return chosen_move
            else:
                trump_suit = []
                for index, move in enumerate(moves):
                    if move[0] is not None and Deck.get_suit(move[0]) == state.get_trump_suit():
                        trump_suit.append(move)
                # Check if we have any trumps
                if len(trump_suit) > 0:
                    high_trump =[]
                    for index, move in enumerate(moves):
                        # if the opponent has played a trump suit
                        if state.get_trump_suit() == Deck.get_suit(state.get_opponents_played_card()):
                            #If we have a higher trump card than the opponent.
                            if trump_suit[0][0] % 5 <= state.get_opponents_played_card() % 5:
                                high_trump.append(move)
                
                    if len(high_trump) > 0:
                        chosen_move = high_trump[0]
                        return chosen_move
                else:
                    #if we have no trump or card of the same suit
                    for index, move in enumerate(moves):
                        if move[0] is not None and move[0] % 5 >= chosen_move[0] % 5:
                            chosen_move = move
                        
        # If opponent has not played a card
        else:
            # Get move with highest rank of card of any suit
            for index, move in enumerate(moves):
                if move[0] is not None and move[0] % 5 <= chosen_move[0] % 5:
                    chosen_move = move
            # Return the choice
        return chosen_move


