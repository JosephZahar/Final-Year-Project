import numpy as np
import imageio
from random import random
import random


def cancerSpread(grid_size_n, number_cancer_cell, number_robots):
    # cell types:
    # normal cell = 0, cancerous cell = 1, healed cell = 2, robot = 3
    global x, y
    NORMAL = 0
    CANCER = 1
    HEAL = 0
    ROBOT1 = 3
    ROBOT2 = 3
    ROBOT3 = 3
    ROBOT4 = 3
    ROBOT5 = 3
    ROBOT6 = 3
    ROBOT7 = 3
    ROBOT8 = 3
    ROBOT9 = 3
    ROBOT10 = 3
    BOUNDARY = 100
    BOUNDARY1 = 101
    BLOOD = 50

    Spreadprob1 = 0.5  # probability of affecting right cell
    Spreadprob2 = 0.3  # probability of affecting left cell
    Spreadprob3 = 0.7  # probability of affecting up cell
    Spreadprob4 = 0.6  # probability of affecting down cell

    time = 500  # total simulation time
    t1 = 70  # end of spread simulation and start of infection simulation
    t2 = 930  # end of infection simulation

    organ_size = [grid_size_n, grid_size_n]  # size of the grid 1000 cells
    cell_states = np.zeros((time, *organ_size))  # Initialize a matrix grid with only normal cells

    if number_cancer_cell == 1:
        cell_states[0, random.randint(0, grid_size_n), random.randint(0,
                                                                      grid_size_n)] = 1  # define random cancerous starting cells

    elif number_cancer_cell == 2:
        cell_states[0, random.randint(0, grid_size_n), random.randint(0, grid_size_n)] = 1
        cell_states[0, random.randint(0, grid_size_n), random.randint(0, grid_size_n)] = 1

    elif number_cancer_cell == 3:
        cell_states[0, random.randint(0, grid_size_n), random.randint(0, grid_size_n)] = 1
        cell_states[0, random.randint(0, grid_size_n), random.randint(0, grid_size_n)] = 1
        cell_states[0, random.randint(0, grid_size_n), random.randint(0, grid_size_n)] = 1

    else:
        print(f'the number of cancerous cells has to be between 1 and 3')
    for x in range(0, organ_size[0]):
        cell_states[0, x, 0] = BOUNDARY
        cell_states[0, x, 109] = BOUNDARY
    for y in range(0, organ_size[0]):
        cell_states[0, 0, y] = BOUNDARY
        cell_states[0, 109, y] = BOUNDARY
    cell_states[0, 1, 109] = BOUNDARY1
    cell_states[0, 109, 108] = BOUNDARY1
    cell_states[0, 0, 1] = BOUNDARY1
    cell_states[0, 108, 0] = BOUNDARY1

    cell_states[0, 90, 30] = BLOOD
    cell_states[0, 30, 80] = BLOOD
    cell_states[0, 60, 40] = BLOOD
    cell_states[0, 20, 20] = BLOOD
    cell_states[0, 49, 79] = BLOOD
    cell_states[0, 78, 48] = BLOOD
    cell_states[0, 40, 60] = BLOOD
    cell_states[0, 33, 99] = BLOOD

    for t in range(1, t1):
        cell_states[t] = cell_states[t - 1].copy()  # the previous cell states will be copied for t+1

        for x in range(1, organ_size[0] - 1):
            for y in range(1, organ_size[1] - 1):

                if cell_states[t - 1, x, y] == CANCER:  # when a cell is originally cancerous it stays cancerous
                    cell_states[t, x, y] = CANCER

                    if cell_states[t - 1, x + 1, y] == NORMAL and random.random() < Spreadprob1:  # spread going down
                        cell_states[t, x + 1, y] = CANCER

                    if cell_states[t - 1, x - 1, y] == NORMAL and random.random() < Spreadprob2:  # spread going up
                        cell_states[t, x - 1, y] = CANCER

                    if cell_states[t - 1, x, y + 1] == NORMAL and random.random() < Spreadprob3:  # spread going right
                        cell_states[t, x, y + 1] = CANCER

                    if cell_states[t - 1, x, y - 1] == NORMAL and random.random() < Spreadprob4:  # spread going left
                        cell_states[t, x, y - 1] = CANCER

    for t in range(t1, time - 2):

        if number_robots == 1:
            cell_states[t1, 10, 2] = ROBOT1
            cell_states[t1, 20, 2] = ROBOT2
            cell_states[t1, 30, 2] = ROBOT3
            cell_states[t1, 40, 2] = ROBOT4
            cell_states[t1, 50, 2] = ROBOT5
            cell_states[t1, 60, 2] = ROBOT6
            cell_states[t1, 70, 2] = ROBOT7
            cell_states[t1, 80, 2] = ROBOT8
            cell_states[t1, 90, 2] = ROBOT9
            cell_states[t1, 100, 2] = ROBOT10

        cell_states[t] = cell_states[t - 1].copy()  # the previous cell states will be copied for t+1
        for x in range(1, organ_size[0] - 1):
            for y in range(1, organ_size[1] - 1):

                def moving(particle):
                    # surrounded by cancer -> go right
                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == CANCER and \
                            cell_states[t - 1, x + 1, y] == CANCER and cell_states[t - 1, x - 1, y] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x + 1, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                    if cell_states[t - 1, x, y] == BOUNDARY:
                        cell_states[t + 1, x, y] = BOUNDARY

                    if cell_states[t - 1, x, y] == particle:
                        cell_states[t + 1, x, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == NORMAL and \
                            cell_states[t - 1, x + 1, y] == NORMAL and cell_states[t - 1, x - 1, y] == CANCER and \
                            cell_states[t - 1, x, y - 1] == NORMAL:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y + 1] = HEAL
                        cell_states[t, x, y - 1] = HEAL
                        cell_states[t, x - 1, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == BOUNDARY and \
                            cell_states[t - 1, x + 1, y] == NORMAL and cell_states[t - 1, x - 1, y] == NORMAL and \
                            cell_states[t - 1, x, y - 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x + 1, y] = HEAL
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x, y - 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == NORMAL and \
                            cell_states[t - 1, x + 1, y] == CANCER and cell_states[t - 1, x - 1, y] == NORMAL and \
                            cell_states[t - 1, x, y - 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y - 1] = HEAL
                        cell_states[t, x, y + 1] = HEAL
                        cell_states[t, x + 1, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == NORMAL and \
                            cell_states[t - 1, x + 1, y] == NORMAL and cell_states[t - 1, x - 1, y] == CANCER and \
                            cell_states[t - 1, x, y - 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y - 1] = HEAL
                        cell_states[t, x, y + 1] = HEAL
                        cell_states[t, x - 1, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == BOUNDARY and \
                            cell_states[t - 1, x + 1, y] == CANCER and cell_states[t - 1, x - 1, y] == CANCER and \
                            cell_states[t - 1, x, y - 1] == NORMAL:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x + 1, y] = HEAL
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x - 1, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == BOUNDARY and \
                            cell_states[t - 1, x - 1, y] == CANCER and cell_states[t - 1, x + 1, y] == NORMAL and \
                            cell_states[t - 1, x, y - 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y - 1] = HEAL
                        cell_states[t, x - 1, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == NORMAL and \
                            cell_states[t - 1, x - 1, y] == CANCER and cell_states[t - 1, x + 1, y] == CANCER and \
                            cell_states[t - 1, x, y - 1] == NORMAL:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x + 1, y] = HEAL
                        cell_states[t, x - 1, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == NORMAL and \
                            cell_states[t - 1, x - 1, y] == NORMAL and cell_states[t - 1, x + 1, y] == NORMAL and \
                            cell_states[t - 1, x, y - 1] == NORMAL:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x + 1, y] = HEAL
                        cell_states[t, x, y - 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == BOUNDARY:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y - 1] = HEAL
                        cell_states[t, x - 1, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == BOUNDARY and \
                                {cell_states[t - 1, x, y - i] == CANCER for i in list(range(5, 100))} and \
                                cell_states[t - 1, x - 1, y] == NORMAL and cell_states[t - 1, x, y - 1] == NORMAL:
                            cell_states[t, x, y - 1] = particle
                            cell_states[t, x - 1, y] = NORMAL

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x - 1, y] == BOUNDARY and \
                            cell_states[t - 1, x + 1, y] == NORMAL:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x + 1, y] = HEAL
                        cell_states[t, x, y - 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x + 1, y] == BOUNDARY:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y - 1] == BOUNDARY:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y + 1] = HEAL
                        cell_states[t, x + 1, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == NORMAL and \
                            cell_states[t - 1, x - 1, y] == NORMAL and cell_states[t - 1, x + 1, y] == NORMAL and \
                            cell_states[t - 1, x, y - 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x + 1, y] = HEAL
                        cell_states[t, x, y - 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == CANCER and \
                            cell_states[t - 1, x - 1, y] == NORMAL and cell_states[t - 1, x + 1, y] == BOUNDARY:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == CANCER and \
                            cell_states[t - 1, x - 1, y] == CANCER and cell_states[t - 1, x + 1, y] == BOUNDARY:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == NORMAL and \
                            cell_states[t - 1, x - 1, y] == NORMAL and cell_states[t - 1, x + 1, y] == CANCER and \
                            cell_states[t - 1, x, y - 1] == NORMAL:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y + 1] = HEAL
                        cell_states[t, x, y - 1] = HEAL
                        cell_states[t, x + 1, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == NORMAL and \
                            cell_states[t - 1, x - 1, y] == CANCER and cell_states[t - 1, x + 1, y] == CANCER and \
                            cell_states[t - 1, x, y - 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y + 1] = HEAL
                        cell_states[t, x, y - 1] = HEAL
                        cell_states[t, x - 1, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == BOUNDARY and \
                            cell_states[t - 1, x - 1, y] == NORMAL and cell_states[t - 1, x + 1, y] == NORMAL and \
                            cell_states[t - 1, x, y - 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x + 1, y] = HEAL
                        cell_states[t, x, y - 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == BLOOD:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y + 1] = BLOOD
                        cell_states[t, x, y - 1] = HEAL
                        cell_states[t, x - 1, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y - 1] == BLOOD:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y - 1] = BLOOD
                        cell_states[t, x, y + 1] = HEAL
                        cell_states[t, x - 1, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x + 1, y] == BLOOD and cell_states[
                        t - 1, x, y - 1] == NORMAL and cell_states[t - 1, x, y + 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x + 1, y] = BLOOD
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x + 1, y] == BLOOD and cell_states[
                        t - 1, x, y - 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x + 1, y] = BLOOD
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x, y - 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x + 1, y] == BLOOD and cell_states[
                        t - 1, x, y - 1] == NORMAL \
                            and cell_states[t - 1, x, y + 1] == NORMAL:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x + 1, y] = BLOOD
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x, y - 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x - 1, y] == BLOOD and cell_states[
                        t - 1, x, y - 1] == NORMAL \
                            and cell_states[t - 1, x, y + 1] == NORMAL:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = BLOOD
                        cell_states[t, x + 1, y] = HEAL
                        cell_states[t, x, y - 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x - 1, y] == BLOOD and cell_states[
                        t - 1, x, y - 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = BLOOD
                        cell_states[t, x + 1, y] = HEAL
                        cell_states[t, x, y - 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x - 1, y] == BLOOD and cell_states[
                        t - 1, x, y - 1] == NORMAL and cell_states[t - 1, x, y + 1] == NORMAL:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = BLOOD
                        cell_states[t, x + 1, y] = HEAL
                        cell_states[t, x, y - 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x - 1, y] == BLOOD and cell_states[
                        t - 1, x, y - 1] == NORMAL and cell_states[t - 1, x, y + 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = BLOOD
                        cell_states[t, x + 1, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x - 1, y] == BLOOD and cell_states[
                        t - 1, x, y - 1] == NORMAL \
                            and cell_states[t - 1, x, y + 1] == NORMAL and cell_states[t - 1, x + 1, y] == NORMAL:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = BLOOD
                        cell_states[t, x, y - 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x + 1, y] == BOUNDARY and \
                            cell_states[t - 1, x - 1, y] == CANCER and cell_states[t - 1, x, y - 1] == NORMAL and \
                            cell_states[t - 1, x, y + 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x + 1, y] == BOUNDARY and \
                            cell_states[t - 1, x - 1, y] == NORMAL and cell_states[t - 1, x, y + 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y + 1] == BOUNDARY and \
                            cell_states[t - 1, x + 1, y] == BOUNDARY1:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y - 1] = HEAL
                        cell_states[t, x - 1, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x + 1, y] == BOUNDARY and \
                            cell_states[t - 1, x, y + 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x + 1, y] == BOUNDARY and \
                            cell_states[t - 1, x - 1, y] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y + 1] = HEAL
                        cell_states[t, x - 1, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x - 1, y] == BOUNDARY and \
                            cell_states[t - 1, x + 1, y] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y + 1] = HEAL
                        cell_states[t, x + 1, y] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x, y - 1] == BOUNDARY and \
                            cell_states[t - 1, x, y + 1] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x + 1, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x - 1, y] == BOUNDARY and \
                            cell_states[t - 1, x, y + 1] == CANCER and cell_states[t - 1, x, y - 1] == CANCER and \
                            cell_states[t - 1, x + 1, y] == NORMAL:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y + 1] = HEAL
                        cell_states[t, x, x - 1] = BOUNDARY
                        cell_states[t, x, y - 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x - 1, y] == BOUNDARY and \
                            cell_states[t - 1, x, y + 1] == CANCER and cell_states[t - 1, x, y - 1] == NORMAL and \
                            cell_states[t - 1, x + 1, y] == NORMAL:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y + 1] = HEAL
                        cell_states[t, x, x - 1] = BOUNDARY
                        cell_states[t, x, y - 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x - 1, y] == BOUNDARY and \
                            cell_states[t - 1, x, y + 1] == CANCER and cell_states[t - 1, x, y - 1] == NORMAL:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                    if cell_states[t - 1, x, y] == particle and cell_states[t - 1, x + 1, y] == BOUNDARY and \
                            cell_states[t - 1, x, y + 1] == NORMAL and cell_states[t - 1, x, y - 1] == NORMAL \
                            and cell_states[t - 1, x - 1, y] == NORMAL and cell_states[t - 1, x, y - 2] == CANCER:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x - 1, y] = particle

                    if cell_states[t - 1, x, y] == ROBOT1 and cell_states[t - 1, x + 1, y] == BOUNDARY and \
                            cell_states[t - 1, x - 1, y + 1] == {
                        ROBOT2 or ROBOT3 or ROBOT4 or ROBOT5 or ROBOT6 or ROBOT7 or ROBOT8 or ROBOT9 or ROBOT10}:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                    if cell_states[t - 1, x, y] == ROBOT1 and \
                            cell_states[t - 1, x - 1, y + 1] == {
                        ROBOT2 or ROBOT3 or ROBOT4 or ROBOT5 or ROBOT6 or ROBOT7 or ROBOT8 or ROBOT9 or ROBOT10}:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                    if cell_states[t - 1, x, y] == ROBOT2 and \
                            cell_states[t - 1, x - 1, y + 1] == {
                        ROBOT1 or ROBOT3 or ROBOT4 or ROBOT5 or ROBOT6 or ROBOT7 or ROBOT8 or ROBOT9 or ROBOT10}:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                    if cell_states[t - 1, x, y] == ROBOT3 and \
                            cell_states[t - 1, x - 1, y + 1] == {
                        ROBOT2 or ROBOT3 or ROBOT4 or ROBOT5 or ROBOT6 or ROBOT7 or ROBOT8 or ROBOT9 or ROBOT10}:
                        cell_states[t, x, y] = HEAL
                        cell_states[t, x, y + 1] = particle

                moving(ROBOT1)
                moving(ROBOT2)
                moving(ROBOT3)
                moving(ROBOT4)
                moving(ROBOT5)
                moving(ROBOT6)
                moving(ROBOT7)
                moving(ROBOT8)
                moving(ROBOT9)
                moving(ROBOT10)

    # Colours for visualization: pink for NORMAL, dark for CANCER and green for HEAL
    colored = np.zeros((time, *organ_size, 3), dtype=np.uint8)

    for t in range(cell_states.shape[0]):
        for x in range(cell_states[t].shape[0]):
            for y in range(cell_states[t].shape[1]):
                value = cell_states[t, x, y].copy()

                if value == NORMAL:
                    colored[t, x, y] = [255, 209, 178]  # NORMAL

                elif value == CANCER:
                    colored[t, x, y] = [10, 10, 10]  # CANCER

                elif value == ROBOT1:
                    colored[t, x, y] = [100, 149, 237]  # ROBOT1

                elif value == ROBOT2:
                    colored[t, x, y] = [100, 149, 237]  # ROBOT2

                elif value == ROBOT3:
                    colored[t, x, y] = [100, 149, 237]  # ROBOT3

                elif value == ROBOT4:
                    colored[t, x, y] = [100, 149, 237]  # ROBOT4

                elif value == ROBOT5:
                    colored[t, x, y] = [100, 149, 237]  # ROBOT5

                elif value == ROBOT6:
                    colored[t, x, y] = [100, 149, 237]  # ROBOT6

                elif value == ROBOT7:
                    colored[t, x, y] = [100, 149, 237]  # ROBOT6

                elif value == ROBOT8:
                    colored[t, x, y] = [100, 149, 237]  # ROBOT6

                elif value == ROBOT9:
                    colored[t, x, y] = [100, 149, 237]  # ROBOT6

                elif value == ROBOT10:
                    colored[t, x, y] = [100, 149, 237]  # ROBOT6

                elif value == BOUNDARY:
                    colored[t, x, y] = [248, 248, 255]  # BOUNDARY

                elif value == BOUNDARY1:
                    colored[t, x, y] = [248, 248, 255]  # BOUNDARY

                elif value == BLOOD:
                    colored[t, x, y] = [255, 0, 0]  # BLOOD

    imageio.mimsave('./singleSI26.gif', colored)  # Save simulation as GIF

cancerSpread(110, 2, 1)
# Final
