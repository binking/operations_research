# -*- coding: utf8-*-
import random
import numpy as np
import time
import sys
from cities_data import cities, distances, geom_norm, read_uk_latlong
# import ipdb; ipdb.set_trace()
# domain = range(0, len(cities))  # 每一维的定义域
# test_cites = [
#         (50.568022, -2.442841), (50.563299, -2.449436),
#         (50.559373, -2.442251), (51.007011, -2.198346),
#         (52.161742, -0.420041), (50.945165, -2.516491)
#     ]
# cities = test_cites
cities = read_uk_latlong()


def pick_random_solution(domain):
    """
    Pick up random solution in domain, there are dim! possible soltions 
    :return: 
    """
    random_solution = []  # can not be repeated
    for d in range(len(cities)):
        d_value = random.choice([ele for ele in domain if ele not in random_solution])
        random_solution.append(d_value)
        sys.stdout.write("Picked up %.2f%% cities\r" % (len(random_solution) * 100.0 / len(cities)))
        sys.stdout.flush()
    return random_solution

def pick_closest_cities(domain):
    closest_solution = []
    next_cities = domain[:]
    cur_city = random.choice(domain)
    # cur_city = 4
    closest_solution.append(cur_city)
    next_cities.remove(cur_city)
    # find the cloest city to last city
    for _ in range(len(cities) - 1):
        dist2cur_city = [distances[cur_city][i] for i in next_cities]
        cur_city = next_cities[np.argmin(dist2cur_city)]
        closest_solution.append(cur_city)
        next_cities.remove(cur_city)
    return closest_solution


def cal_path_distance(indices2cites):
    return round(sum([distances[indices2cites[i]][indices2cites[i+1]] for i in range(len(indices2cites)-1)])
                 + distances[indices2cites[-1]][indices2cites[0]])


def pick_uk_closest_cities(domain):
    pickup_time = time.time()
    closest_solution = []
    next_cities = domain[:]
    cur_city = random.choice(domain)
    # cur_city = 4
    closest_solution.append(cur_city)
    next_cities.remove(cur_city)
    # find the cloest city to last city
    for _ in range(len(cities) - 1):
        dist2cur_city = [geom_norm(cities[cur_city], cities[i]) for i in next_cities]
        cur_city = next_cities[np.argmin(dist2cur_city)]
        closest_solution.append(cur_city)
        next_cities.remove(cur_city)
        sys.stdout.write("Picked up %.2f%% cities\r" % (len(closest_solution)*100.0 / len(cities)))
        sys.stdout.flush()
    print "Picking up closest solution costs %.2f seconds" % (time.time() - pickup_time)
    return closest_solution


def cal_uk_cities_path(indices2cites):
    route_dist = 0
    for i in range(len(indices2cites) - 1):
        temp = geom_norm(cities[indices2cites[i]], cities[indices2cites[i+1]])
        route_dist += temp
    route_dist + geom_norm(cities[indices2cites[-1]], cities[indices2cites[0]])
    return route_dist
