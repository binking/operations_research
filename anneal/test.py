# -*-coding: utf-8 -*-
from cities_data import cities, distances, geom_norm, haversine_distance, spherical_law_of_cosines
from solve_tsp import cal_path_distance, pick_random_solution, pick_closest_cities, cal_uk_cities_path
from simulated_anneal import SimulatedAnneal

def test_pick_random_solution():
    """
    Suppose there are 7 cites
    :return: 
    """
    print "Random pickup solution: ", pick_random_solution()
    print "Closest pickup solution: ", pick_closest_cities()



def test_cal_path_distance():
    """
    Test the cost function
    :return: 
    """
    travel_route = ['Huelva', 'Sevilla', 'Cordoba', 'Jaen', 'Granada', 'Almeria', 'Malaga', 'Cadiz']
    city2index = dict([(v,k) for k,v in cities.items()])
    travel_route_index = [city2index[c] for c in travel_route]
    cost = 0
    for idx in range(len(travel_route) - 1):
        cost += distances[city2index[travel_route[idx]]][city2index[travel_route[idx+1]]]
    cost += distances[city2index['Cadiz']][city2index['Huelva']]
    print "Target Cost: ", cost
    print "Compute Cost: ", cal_path_distance(travel_route_index)
    assert cost == cal_path_distance(travel_route_index)


def test_sa():
    test_domain = [
        (0, len(cities)-1) for _ in range(len(cities))
    ]
    sa = SimulatedAnneal(
        domain=test_domain, cost_f=cal_path_distance, init_solution=pick_closest_cities(test_domain),
        cooling_speed=0.9995, temperature=10**6, stopping_temp=0.1 ** 6, max_iter=10**5
    )
    sa.anneal()
    print "Best fitness: ", sa.best_fitness
    print "Best solution: ", sa.best_solution
    print "Current fitness: ", sa.current_fitness
    print "Current solution: ", sa.current_solution


def test_geom_norm():
    test_point1 = (50.873880, 0.611211)
    test_point2 = (50.873880, -0.341747)
    print geom_norm(test_point1, test_point2)

def test_haversine_distance():
    test_point1 = (50.873880, 0.611211)
    test_point2 = (50.873880, -0.341747)
    print haversine_distance(test_point1, test_point2)

def test_spherical_law_of_cosines():
    test_point1 = (50.873880, 0.611211)
    test_point2 = (50.873880, -0.341747)
    print spherical_law_of_cosines(test_point1, test_point2)

def test_cal_uk_cities_path():
    test_cites = [
        (50.568022, -2.442841), (50.563299, -2.449436),
        (50.559373, -2.442251), (51.007011, -2.198346),
        (52.161742, -0.420041), (50.945165, -2.516491)
    ]
    print cal_uk_cities_path(range(len(test_cites)))

if __name__ == '__main__':
    # test_pick_random_solution()
    # test_cal_path_distance()
    # print cal_path_distance([4, 7, 1, 6, 3, 5, 2, 0])
    # test_sa()
    test_geom_norm()
    test_haversine_distance()
    test_spherical_law_of_cosines()
    test_cal_uk_cities_path()