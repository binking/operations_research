# -*- coding: utf8-*-
# Solving UK 24727
import random
import time
time_load_module = time.time()
from cities_data import read_optimal_solution
from solve_tsp import pick_random_solution, cities, cal_uk_cities_path
from simulated_anneal import SimulatedAnneal
print "Load module costs %.2f seconds." % (time.time() - time_load_module)


domain = range(0, len(cities))
domain_range = (0, len(cities) - 1)



def solve_uk24727():
    print "Optimal solution's fitness is ", cal_uk_cities_path(read_optimal_solution())
    # print "Pickup closest's fitness is ", cal_uk_cities_path(pick_uk_closest_cities(domain))
    value_domain = [domain_range for _ in domain]
    random_cities = domain[:]
    random.shuffle(random_cities)
    # print "Random solution's fitness is ", cal_uk_cities_path(pick_random_solution(domain))
    print "Random solution's fitness is ", cal_uk_cities_path(random_cities)
    sa = SimulatedAnneal(
        domain=value_domain, cost_f=cal_uk_cities_path, init_solution=random_cities,
        temperature=10**6, cooling_speed=0.995, stopping_temp=0.1**6, max_iter=10**5
    )
    anneal_time = time.time()
    sa.anneal()
    print "Anneal Process costs %.2f seconds" % (time.time() - anneal_time)
    print "=" * 20, "Using Simulated Anneal", "=" * 20
    print "Best fitness: ", sa.best_fitness
    # print "Best solution: ", sa.best_solution
    print "Current fitness: ", sa.current_fitness
    # print "Current solution: ", sa.current_solution


if __name__ == '__main__':
    solve_uk24727()
