# -*-coding: utf-8 -*
import random
import math
import sys


class SimulatedAnneal:
    def __init__(self, domain, init_solution, cost_f,
                 cooling_speed=0.995, temperature=10**6, max_iter=10*5,
                 stopping_temp=0.1**8):
        """
        
        :param domain: list of tuples, each tuple is the domain of its dimensionalty 
        :param cooling_speed: 
        :param temperature: 
        :param max_iter: 
        """
        # The domain of the problem
        self.domain = domain
        self.dim = len(domain)
        # Cooling schedule
        self.cooling_speed = cooling_speed
        self.temperature = temperature
        self.stopping_temp = stopping_temp
        self.max_iter = max_iter
        self.cost_function = cost_f
        # Record solution
        self.best_solution = init_solution
        self.best_fitness = sys.maxint
        self.current_solution = init_solution
        self.current_fitness = sys.maxint

    def prob_accept(self, eb):
        """
        P(dE) = exp( dE / kT)
        :param eb: 
        :return: 
        """
        return math.exp( -abs(eb - self.current_fitness) / self.temperature )

    def accept(self, new_solution):
        """
        Metropolis method:  p = 1             , if dE < 0
                                exp(- dE / T) , otherwise
        :return: 
        """
        new_energy = self.cost_function(new_solution)
        # import ipdb; ipdb.set_trace()
        if new_energy < self.current_fitness:
            self.current_fitness = new_energy
            self.current_solution = new_solution
            if new_energy < self.best_fitness:
                # update best choice
                self.best_fitness = new_energy
                self.best_solution = new_solution
        else:  # accept worse solution with some probability
            if random.random() < self.prob_accept(new_energy):
                self.current_fitness = new_energy
                self.current_solution = new_solution

    def jump_to_neighbor(self):
        new_solution = self.current_solution[:]
        step = random.randint(2, self.dim-1)
        start = random.randint(0, self.dim-step)
        # print old_solution
        new_solution[start:start+step] = self.current_solution[start:start+step][::-1]
        return new_solution
        # print self.current_solution
        # self.current_fitness = self.cost_function(self.current_solution)

    def anneal(self):
        """
        The process of Annealing
        :return: 
        """
        t = self.temperature
        it = 0
        # import ipdb; ipdb.set_trace()
        while t >= self.stopping_temp and it < self.max_iter:
            next_solution = self.jump_to_neighbor()
            self.accept(next_solution)
            t *= self.cooling_speed  # temrature calm down
            it += 1
            sys.stdout.write("Run %.3f%% iterations\r" % ((it + 1) * 100.0 / self.max_iter))
            sys.stdout.flush()
        print