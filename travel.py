#!/usr/bin/env python
# sixie6e@distherapy
import math
import numpy as np
from python_tsp.distances import great_circle_distance_matrix
from python_tsp.exact import solve_tsp_dynamic_programming
import python_tsp
import random
#import matplotlib.pyplot as plt
'''Vehicles/drivers kill 3700+ daily and that is not including wildlife or resources wasted and environmental garbage. If we can consolidate transportation and purpose, we might make it as a species. People make too many trips in personal vehicles and most of the time those could wait until another trip to do everything at once, or are just existentially unnecessary. Hillbillies in trucks, motorcycle gangs, thugs in caddies on 22's, suburban mothers in suburbans, motorsports, citizens mindlessly mowing the lawn, so much damage is done(much of it uninentional, apathetic, conditioned behavior). "Buy gas thangs!", say the hillbillies and gas/oil corporations,. "Buy electric items!", say the virtue signaling corporate types....or...how about you just stop driving so goddamn much, sitting down to move around the planet, killing people and wildlife. Don't waste resources and purposelessly consume then cry about gas prices. Anthropocentric remedials.'''
# https://www.youtube.com/shorts/gaZL-faODew is a major motivating factor for me slowly putting this together.
gas_comm_air = 95000000000 / 365 #~260.27million gal per day
gas_prv_air = 743000  * 42 / 365 #barrels to gal per day
gas_off_road = 2200000000 / 365 #~6.03million gal per day
gas_class8 = 29.4 #gal per day each
miles_class_8 = 62169 / 365 #~170.3 daily each
gas_trash_trucks = 27.6 #gal per day each
miles_trash_trucks = 25000 / 365 #~68.49 daily each
gas_city_bus = 26.3 #gal per day each
miles_city_bus = 42940 / 365 #~117.64 daily each
gas_school_bus = 5.8 #gal per day each
miles_school_bus = 14084 / 365 #~38.58 daily each
gas_van = 1.7 #gal per day each
miles_van = 11318 / 365 #~31.01 daily each
gas_sedan =  1.18 #gal per day each
miles_sedan = 10573 / 365 #~28.96 daily each
gas_maritime = 87000000000 / 365 #~238.35million gak per day
air_miles = 573380000000 / 365 #~1.57billion per day
perc_oil_air = 7.8
perc_oil_maritime = 6.1
perc_oil_land = 87.5
lawnmower_market = 8100000000 / 365 #~22million dollars daily

#pyramid(similar)scheme/racket:
insurance_air = 14900000000 / 365 #~40.8million dollars daily
insurance_land = 2150000000000 / 365 #5.8billion dollars daily
insurance_maritime = 960000000 / 365 #2.63million dollars daily

#logistics solutions starting with tsp:
sources = np.array([
    [0,  5, 4, 10],
    [5,  0, 8,  5],
    [4,  8, 0,  3],
    [10, 5, 3,  0]
])
distance_matrix = np.array([
    [ 40.73024833, -73.79440675],
    [ 41.47362495, -73.92783272],
    [ 41.26591   , -73.21026228],
    [ 41.3249908 , -73.507788  ]

])
distance_matrix = great_circle_distance_matrix(sources)
permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
print(distance, permutation)
print(distance_matrix)

