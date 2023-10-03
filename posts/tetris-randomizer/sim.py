# simple simulation of O(1) piece dist calculation
# for random bag7-like tetris randomizer

import random
from matplotlib import pyplot as plt
import numpy as np

PIECES = ['L', 'J', 'I', 'O', 'S', 'T', 'Z']

DENOMINATOR = 10

def alter_weights(current_weights, chosen_piece_index):
    offset = (DENOMINATOR - 1) * current_weights[chosen_piece_index] / DENOMINATOR
    updated_weights = [
        weight + (offset / (len(PIECES) - 1)) if i != chosen_piece_index else weight - offset
        for i,weight in enumerate(current_weights)
    ]
    return updated_weights

def choose_piece(weights):
    return random.choices(range(len(PIECES)), weights=weights, k=1)[0]

def copy(some_list):
    return [i for i in some_list]

def simulate(N):
    weights_over_time = []
    pieces = []
    weights = [1] * len(PIECES)
    weights_over_time.append(copy(weights))
    for _ in range(N):
        next_piece = choose_piece(weights)
        pieces.append(next_piece)
        weights = alter_weights(weights, next_piece)
        weights_over_time.append(copy(weights))
    return weights_over_time, pieces

def label(pair):
    num, piece = pair
    if type(piece) == int:
        return str(num) + ':' + PIECES[piece]
    return str(num) + ':' + piece

def stacked_barplot(weights_over_time, pieces):
    x = [label(x) for x in zip(range(1, len(weights_over_time) + 1), ['(None)'] + pieces)]
    y = []
    for i in range(len(PIECES)):
        y.append(
            np.array(
                [weights[i] for weights in weights_over_time]
            )
        )
    for i in range(len(PIECES)):
        plt.bar(x, y[i], bottom=sum(y[:i]))
    plt.xlabel('Piece #')
    plt.ylabel('Piece Weight Distribution')
    plt.title('Piece weight distribution over time')
    plt.legend(PIECES)
    plt.show()

def piece_frequency_histogram(pieces):
    plt.hist(pieces, bins=len(PIECES), density=True, rwidth=0.5)
    plt.title(f'Histogram of piece frequency ({N} iterations)')
    plt.show()

# sample data
N = 1000
sample_data, pieces = simulate(N)

stacked_barplot(sample_data, pieces)
piece_frequency_histogram(pieces)
# piece_names = [PIECES[piece] for piece in pieces]
# print(''.join(name.lower() for name in piece_names))