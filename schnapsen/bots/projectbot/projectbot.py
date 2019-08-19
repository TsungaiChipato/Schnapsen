#!/usr/bin/env python
"""
This is a bot that applies propositional logic reasoning to determine its strategy.
The strategy it uses is determined by what is defined in load.py. Here it is to always
pick a Jack to play whenever this is a legal move.

It loads general information about the game, as well as the definition of a strategy,
from load.py.
"""

from api import State, util
import random
from . import load
from .kb import KB, Boolean, Integer

class Bot:
    strategy1 = ""
    strategy2 = ""
    def __init__(self):
        pass

    def get_move(self, state):

        moves = state.moves()
        chosen_moves = moves[0]
        random.shuffle(moves)
        
        if state.get_stock_size() == 10 and state.whose_turn() == state.leader():
            Bot.strategy2 = "Marriage"
        if state.get_stock_size() == 0 and state.whose_turn() == state.leader():
            Bot.strategy2 = "PlayA"
            Bot.strategy1 = "Playhigh"

        if Bot.strategy2 == "PlayA":
            for move in moves:
                if not self.kb_consistent_playa(state, move):
                    return move
            return random.choice(moves)

        elif Bot.strategy1 == "Playhigh":
            for move in moves:
                if not self.kb_consistent_playhigh(state, move):
                    return move
            return random.choice(moves)
        elif Bot.strategy2 == "Marriage":
            for move in moves:
                if not self.kb_consistent_marriage(state, move):
                    return move
            return random.choice(moves)
        else:
            #We return a random move
            return random.choice(moves)
       
        
    # Note: In this example, the state object is not used,
    # but you might want to do it for your own strategy.
    def kb_consistent_playhigh(self, state, move):
    # type: (State, move) -> bool

        # each time we check for consistency we initialise a new knowledge-base
        kb = KB()

        # Add general information about the game
        load.general_information(kb)

        # Add the necessary knowledge about the strategy
        load.strategy_knowledge(kb)

        # This line stores the index of the card in the deck.
        # If this doesn't make sense, refer to _deck.py for the card index mapping
        index = move[0]

        # This creates the string which is used to make the strategy_variable.
        # Note that as far as kb.py is concerned, two objects created with the same
        # string in the constructor are equivalent, and are seen as the same symbol.
        # Here we use "pj" to indicate that the card with index "index" should be played with the
        # PlayJack heuristics that was defined in class. Initialise a different variable if 
        # you want to apply a different strategy (that you will have to define in load.py)
        variable_string = "ph" + str(index)
        strategy_variable = Boolean(variable_string)

        # Add the relevant clause to the loaded knowledge base
        kb.add_clause(~strategy_variable)

        # If the knowledge base is not satisfiable, the strategy variable is
        # entailed (proof by refutation)
        return kb.satisfiable()

    def kb_consistent_playa(self, state, move):
         # type: (State, move) -> bool
         
         # each time we check for consistency we initialise a new knowledge-base
         kb = KB()
         
         # Add general information about the game
         load.general_information(kb)
         
         # Add the necessary knowledge about the strategy
         load.strategy_knowledge(kb)
         
         # This line stores the index of the card in the deck.
         # If this doesn't make sense, refer to _deck.py for the card index mapping
         index = move[0]
         
         # This creates the string which is used to make the strategy_variable.
         # Note that as far as kb.py is concerned, two objects created with the same
         # string in the constructor are equivalent, and are seen as the same symbol.
         # Here we use "pj" to indicate that the card with index "index" should be played with the
         # PlayJack heuristics that was defined in class. Initialise a different variable if
         # you want to apply a different strategy (that you will have to define in load.py)
         variable_string = "pa" + str(index)
         strategy_variable = Boolean(variable_string)
         
         # Add the relevant clause to the loaded knowledge base
         kb.add_clause(~strategy_variable)
         
         # If the knowledge base is not satisfiable, the strategy variable is
         # entailed (proof by refutation)
         return kb.satisfiable()
     
    def kb_consistent_marriage(self, state, move):
         # type: (State, move) -> bool
         
         # each time we check for consistency we initialise a new knowledge-base
         kb = KB()

         # Add general information about the game
         load.general_information(kb)
         
         # Add the necessary knowledge about the strategy
         load.strategy_knowledge(kb)
             
         # This line stores the index of the card in the deck.
         # If this doesn't make sense, refer to _deck.py for the card index mapping
         index = move[0]
         
         # This creates the string which is used to make the strategy_variable.
         # Note that as far as kb.py is concerned, two objects created with the same
         # string in the constructor are equivalent, and are seen as the same symbol.
         # Here we use "pj" to indicate that the card with index "index" should be played with the
         # PlayJack heuristics that was defined in class. Initialise a different variable if
         # you want to apply a different strategy (that you will have to define in load.py)
         variable_string = "pm" + str(index)
         strategy_variable = Boolean(variable_string)
     
         # Add the relevant clause to the loaded knowledge base
         kb.add_clause(~strategy_variable)
             
        # If the knowledge base is not satisfiable, the strategy variable is
        # entailed (proof by refutation)
         return kb.satisfiable()

    


