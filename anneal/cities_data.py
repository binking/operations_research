# -*- coding: utf8-*-
import math
cities = {0:'Almeria',1:'Cadiz',2:'Cordoba',3:'Granada',4:'Huelva',5:'Jaen',6:'Malaga',7:'Sevilla'}

#Distance between each pair of cities

w0 = [999,454,317,165,528,222,223,410]
w1 = [453,999,253,291,210,325,234,121]
w2 = [317,252,999,202,226,108,158,140]
w3 = [165,292,201,999,344,94,124,248]
w4 = [508,210,235,346,999,336,303,94]
w5 = [222,325,116,93,340,999,182,247]
w6 = [223,235,158,125,302,185,999,206]
w7 = [410,121,141,248,93,242,199,999]

distances = {0:w0,1:w1,2:w2,3:w3,4:w4,5:w5,6:w6,7:w7}

def haversine_distance(point1, point2):
    """
    Haversine
    formula:	a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
    c = 2 ⋅ atan2( √a, √(1−a) )
    d = R ⋅ c
    where	φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km);
    note that angles need to be in radians to pass to trig functions!
    :param point1: (latitude, longitude) 
    :param point2: (latitude, longitude)
    :return: haversine distance
    """
    R = 6371004.0
    lat1 = math.pi * point1[0] / 180.0
    lng1 = math.pi * point1[1] / 180.0
    lat2 = math.pi * point2[0] / 180.0
    lng2 = math.pi * point2[1] / 180.0
    a = pow(math.sin(lat1 - lat2)/2.0, 2) + math.cos(lat1) * math.cos(lat2) * pow(math.sin((lng1 - lng2)/2.0), 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c


def geom_norm(point1, point2):
    """    
    :return: 
    """
    lat1 = math.pi * point1[0] / 180.0
    lng1 = math.pi * point1[1] / 180.0
    lat2 = math.pi * point2[0] / 180.0
    lng2 = math.pi * point2[1] / 180.0

    q1 = math.cos(lat2) * math.sin(lng1 - lng2)
    q2 = math.sin((lng1 - lng2) / 2.0)
    q3 = math.cos((lng1 - lng2) / 2.0)
    q4 = math.sin(lat1 + lat2) * q2 * q2 - math.sin(lat1 - lat2) * q3 * q3
    q5 = math.cos(lat1 - lat2) * q3 * q3 - math.cos(lat1 + lat2) * q2 * q2
    return (6378388.0 * math.atan2(math.sqrt(q1*q1 + q4*q4), q5) + 1.0)  # 6378388.0


def spherical_law_of_cosines(point1, point2):
    """
    d = acos( sin φ1 ⋅ sin φ2 + cos φ1 ⋅ cos φ2 ⋅ cos Δλ ) ⋅ R
    SQL: 6371.004 *  ACOS( SIN(c1.latitude*PI()/180.0)*sin(c2.latitude*PI()/180.0) 
    + COS(c1.longitude*PI()/180.0 - c2.longitude*PI()/180.0) * 
    cos(c1.latitude*PI()/180.0)*cos(c2.latitude*PI()/180.0) ) 
    :param point1: 
    :param point2: 
    :return: 
    """
    R = 6371004.0
    lat1 = math.pi * point1[0] / 180.0
    lng1 = math.pi * point1[1] / 180.0
    lat2 = math.pi * point2[0] / 180.0
    lng2 = math.pi * point2[1] / 180.0
    return R * math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lng1 - lng2) * math.cos(lat1) * math.cos(lat2))


def read_uk_latlong():
    uk_cities = []
    with open('uk24727_latlong.txt', 'r') as fr:
        for line in fr.readlines():
            lat, lng = line.strip().split(' ')
            uk_cities.append((float(lat), float(lng)))
    return uk_cities


def read_optimal_solution():
    indices = []
    with open('uk24727_optimal.txt', 'r') as fr:
        for line in fr.readlines():
           indices.append(int(line.strip()))
    return indices