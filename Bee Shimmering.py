import numpy as np
import imageio
from random import random
import random
import matplotlib.pyplot as plt
import seaborn as sns


def BeeShimmering(grid_size_n):
    global x, y
    G_A = 1
    G_I = 2
    G_R = 3
    B_A = 4
    B_I = 0
    B_R = 6
    INACTIVE = 7
    C_T = 8
    BOUNDARY = 100

    r1 = 0.7
    r2 = 0.99
    r3 = 0.99
    r4 = 0.001

    time = 100
    bee_hive = [grid_size_n, grid_size_n]
    cell_states = np.zeros((time, *bee_hive))
    cell_states[0] = np.random.choice([G_I, B_I, G_A, C_T], size=bee_hive, p=[0.009, 0.69, 0, 0.301])
    for x in range(0, bee_hive[0]):
        cell_states[0, x, 0] = BOUNDARY
        cell_states[0, x, grid_size_n - 1] = BOUNDARY
    for y in range(0, bee_hive[0]):
        cell_states[0, 0, y] = BOUNDARY
        cell_states[0, grid_size_n - 1, y] = BOUNDARY

    for t in range(1, time):
        cell_states[t] = cell_states[t - 1].copy()

        for x in range(1, bee_hive[0] - 1):
            for y in range(1, bee_hive[1] - 1):

                if cell_states[t - 1, x, y] == G_A and random.random() < r2:
                    cell_states[t, x, y] = G_R

                if cell_states[t - 1, x, y] == C_T:
                    cell_states[t, x, y] = C_T

                if cell_states[t - 1, x, y] == B_A and random.random() < r2:
                    cell_states[t, x, y] = B_R

                if cell_states[t - 1, x, y] == G_R and random.random() < r3:
                    cell_states[t, x, y] = INACTIVE

                if cell_states[t - 1, x, y] == B_R and random.random() < r3:
                    cell_states[t, x, y] = INACTIVE

                if cell_states[t - 1, x, y] == G_I and random.random() < r4:
                    cell_states[t, x, y] = G_A

                if cell_states[t - 1, x, y] == G_A:
                    if cell_states[t - 1, x + 1, y] == B_I and random.random() < r1:
                        cell_states[t, x + 1, y] = B_A
                    if cell_states[t - 1, x - 1, y] == B_I and random.random() < r1:
                        cell_states[t, x - 1, y] = B_A
                    if cell_states[t - 1, x, y + 1] == B_I and random.random() < r1:
                        cell_states[t, x, y + 1] = B_A
                    if cell_states[t - 1, x, y - 1] == B_I and random.random() < r1:
                        cell_states[t, x, y - 1] = B_A
                    if cell_states[t - 1, x + 1, y + 1] == B_I and random.random() < r1:
                        cell_states[t, x + 1, y + 1] = B_A
                    if cell_states[t - 1, x - 1, y + 1] == B_I and random.random() < r1:
                        cell_states[t, x - 1, y + 1] = B_A
                    if cell_states[t - 1, x + 1, y - 1] == B_I and random.random() < r1:
                        cell_states[t, x + 1, y - 1] = B_A
                    if cell_states[t - 1, x - 1, y - 1] == B_I and random.random() < r1:
                        cell_states[t, x - 1, y - 1] = B_A

                if cell_states[t - 1, x, y] == B_A:
                    if cell_states[t - 1, x + 1, y] == B_I and random.random() < r1:
                        cell_states[t, x + 1, y] = B_A
                    if cell_states[t - 1, x - 1, y] == B_I and random.random() < r1:
                        cell_states[t, x - 1, y] = B_A
                    if cell_states[t - 1, x, y + 1] == B_I and random.random() < r1:
                        cell_states[t, x, y + 1] = B_A
                    if cell_states[t - 1, x, y - 1] == B_I and random.random() < r1:
                        cell_states[t, x, y - 1] = B_A
                    if cell_states[t - 1, x + 1, y + 1] == B_I and random.random() < r1:
                        cell_states[t, x + 1, y + 1] = B_A
                    if cell_states[t - 1, x - 1, y + 1] == B_I and random.random() < r1:
                        cell_states[t, x - 1, y + 1] = B_A
                    if cell_states[t - 1, x + 1, y - 1] == B_I and random.random() < r1:
                        cell_states[t, x + 1, y - 1] = B_A
                    if cell_states[t - 1, x - 1, y - 1] == B_I and random.random() < r1:
                        cell_states[t, x - 1, y - 1] = B_A

    colored = np.zeros((time, *bee_hive, 3), dtype=np.uint8)

    for t in range(cell_states.shape[0]):
        for x in range(cell_states[t].shape[0]):
            for y in range(cell_states[t].shape[1]):
                value = cell_states[t, x, y].copy()

                if value == G_A:
                    colored[t, x, y] = [255, 239, 15]

                elif value == G_I:
                    colored[t, x, y] = [196, 171, 15]

                elif value == G_R:
                    colored[t, x, y] = [139, 69, 19]

                if value == B_A:
                    colored[t, x, y] = [255, 239, 15]

                elif value == B_I:
                    colored[t, x, y] = [196, 171, 15]

                elif value == B_R:
                    colored[t, x, y] = [139, 69, 19]

                elif value == INACTIVE:
                    colored[t, x, y] = [196, 171, 15]

                elif value == C_T:
                    colored[t, x, y] = [196, 171, 15]

                elif value == BOUNDARY:
                    colored[t, x, y] = [255, 255, 255]

    imageio.mimsave('./BeeShimmeringC_T5.gif', colored)

BeeShimmering(100)
