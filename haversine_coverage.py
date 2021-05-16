"""
I would never "reinvent the wheel", so I would definitely use the `haversine` package to calculate the Haversine Formula
"""

import pprint
# from haversine import haversine
from math import radians, cos, sin, asin, sqrt

pp = pprint.PrettyPrinter(indent=2)

locations = [
    {'id': 1000, 'zip_code': '37069', 'lat': 45.35, 'lng': 10.84},
    {'id': 1001, 'zip_code': '37121', 'lat': 45.44, 'lng': 10.99},
    {'id': 1001, 'zip_code': '37129', 'lat': 45.44, 'lng': 11.00},
    {'id': 1001, 'zip_code': '37133', 'lat': 45.43, 'lng': 11.02},
]

shoppers = [
    {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': True},
    {'id': 'S2', 'lat': 45.46, 'lng': 10.12, 'enabled': True},
    {'id': 'S3', 'lat': 45.34, 'lng': 10.81, 'enabled': True},
    {'id': 'S4', 'lat': 45.76, 'lng': 10.57, 'enabled': True},
    {'id': 'S5', 'lat': 45.34, 'lng': 10.63, 'enabled': True},
    {'id': 'S6', 'lat': 45.42, 'lng': 10.81, 'enabled': True},
    {'id': 'S7', 'lat': 45.34, 'lng': 10.94, 'enabled': True},
]

def haversine(lat1: float, lng1: float, lat2: float, lng2: float):
    """
    However, I've copied from StackOverflow this function so we can check the formula
    It was copied from: https://stackoverflow.com/a/4913653/1422175

    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])

    # haversine formula
    dlng = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlng / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles

    return c * r

sorted = []

for shopper in shoppers:
    if not shopper['enabled']:
        continue

    covered = 0

    for location in locations:
        # distance = haversine((location['lat'], location['lng']), (shopper['lat'], shopper['lng']))
        distance = haversine(location['lat'], location['lng'], shopper['lat'], shopper['lng'])

        print(distance)

        if distance < 10:
            covered = covered + 1

    coverage = (covered / len(locations)) * 100

    sorted.append({'shopper_id': shopper['id'], 'coverage': coverage})

sorted.sort(key=lambda coverage: coverage['coverage'], reverse=True)

pp.pprint(sorted)
