# -*- coding: utf8-*-
import sys


class GeneticAlgo:
    def __inti__(self, mutate_rate=0.2, cross_rate=0.4):
        self.mutation_rate = mutate_rate
        self.crossover_rate = cross_rate
        self.current_fitness = sys.maxint
        self.current_solution =