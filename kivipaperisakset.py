# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:39:54 2024

@author: paavo

Usage: python kivipaperisakset.py [min_history]

"""

import sys
import random

class Hand(object):
    
    def __init__(self, kind):        
        self.kind = kind
    
    def __gt__(self, other):
        # Overridden in subclasses
        pass
    
    def __lt__(self, other):
        # Subclasses inherit this implementation
        return other.__gt__(self)
    
    def __eq__(self, other):
        # Subclasses inherit this implementation
        return not self.__gt__(other) and not self.__lt__(other)
    
class Scissors(Hand):
    
    def __init__(self):
        super().__init__('s')
    
    def __gt__(self, other):
        if other.kind == 'p':
            return True
        return False
    
    def __str__(self):
        return "Sakset"
    
class Paper(Hand):
    
    def __init__(self):
        super().__init__('p')
    
    def __gt__(self, other):
        if other.kind == 'k':
            return True
        return False
    
    def __str__(self):
        return "Paperi"
    
class Rock(Hand):
        
    def __init__(self):
        super().__init__('k')
        
    def __gt__(self, other):
        if other.kind == 's':
            return True
        return False

    def __str__(self):
        return "Kivi"

def parse_input():
    
    while True:
        hand = input("Choose your hand >> ")
        if hand == 'q':
            sys.exit()
        if hand == 'k':
            return Rock()
        elif hand == 'p':
            return Paper()
        elif hand == 's':
            return Scissors()
        else:
            print("Invalid hand: ", hand, "choose from k, p, s")
            continue

def predict_opponent(previous_hands, min_history):
    
    if len(previous_hands) > min_history:
        prev_triple = previous_hands[-3:]
        guesses = []
        # look through the history and look for the same pattern, and use what follows
        for i in range(len(previous_hands) - 3):
            if previous_hands[i:i+3] == prev_triple:
                #return previous_hands[i+4]
                guesses.append(previous_hands[i+3])
                
        if guesses:
            return guesses[-1] # return the most recent pattern
        else:
            return random.choice([Rock(), Paper(), Scissors()])
        
    #TODO: implement a better strategy that isn't just aiming for a tie
    # Something like this: if guess == Rock(), return Paper(), etc.
    #TODO: implement the loop so that it doesn't just return the first match
    # but the most common match 
    
    return random.choice([Rock(), Paper(), Scissors()])

def main(min_history=float('inf')):
    
    print(f"Welcome to rock-paper-scissors!")
    print("You will play against the computer, until you decide to quit.")
    print("Choose your hand: k, p, s, or q to quit.")
    
    # For some intelligence for the computer, we can keep track of the player's history
    # and try to predict the next move. The computer always goes for a Tie (at the moment).
    # If min_history is not set, the computer will always draw a random hand.
    player_history = []
    opponent_strategy = lambda x: predict_opponent(x, min_history)
    wins=0;losses=0;ties=0;count=1
    
    while True:
        print(f"---- Round {count} ----")

        player_hand = parse_input()
        player_history.append(player_hand)
        
        computer_hand = opponent_strategy(player_history)
        
        print("You chose: ", player_hand)
        print("Computer chose: ", computer_hand)
        
        if player_hand > computer_hand:
            print("You win!")
            wins+=1
        elif player_hand < computer_hand:
            print("You lose!")
            losses+=1
        else:
            print("It's a tie!")
            ties+=1
            
        print(f"Score: {wins} wins, {losses} losses, {ties} ties")
        count+=1
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main()
    
