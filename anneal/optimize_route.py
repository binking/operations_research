# -*- coding: utf8-*-
# Solving UK 24727
import time
time_load_module = time.time()
from cities_data import read_optimal_solution
from solve_tsp import pick_uk_closest_cities, cities, cal_uk_cities_path
from simulated_anneal import SimulatedAnneal
print "Load module costs %.2f seconds." % (time.time() - time_load_module)


domain = range(0, len(cities))
domain_range = (0, len(cities) - 1)



def solve_uk24727():
    print "Optimal solution's fitness is ", cal_uk_cities_path(read_optimal_solution())
    print "Pickup closest's fitness is ", cal_uk_cities_path(pick_uk_closest_cities(domain))
    value_domain = [domain_range for _ in domain]
    sa = SimulatedAnneal(
        domain=value_domain, cost_f=cal_uk_cities_path, init_solution=pick_uk_closest_cities(domain),
        temperature=10*5, cooling_speed=0.99, stopping_temp=10*4, max_iter=1000
    )
    sa.anneal()
    print "=" * 20, "Using Simulated Anneal", "=" * 20
    print "Best fitness: ", sa.best_fitness
    print "Best solution: ", sa.best_solution
    print "Current fitness: ", sa.current_fitness
    print "Current solution: ", sa.current_solution


if __name__ == '__main__':
    solve_uk24727()
