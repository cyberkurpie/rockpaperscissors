#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
import random

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


    def beats(one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)



class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.score()
        print()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")

    def score(self, beats):
        if beats(move1, move2):
            self.p1_score += 1
            self.p2_score += 0
            print("PLAYER 1 WINS")
            print(f"Score Player 1 {self.p1_score}, Player Two {self.p2_score}")
        elif beats(move2, move1):
            self.p1_score += 0
            self.p2_score += 1
            print("PLAYER 2 WINS")
            print(f"Score Player 1 {self.p1_score}, Player Two {self.p2_score}")
        else:
            self.p1_score += 0
            self.p2_score += 0
            print("TIE")
            print(f"Score Player 1 {self.p1_score}, Player Two {self.p2_score}")




if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
