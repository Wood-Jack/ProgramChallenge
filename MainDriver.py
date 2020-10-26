
from TrainStation import TrainStation


#
#
# Project Name:   Programming Challenge
# Programmer:    Woodrow Jackson
#
#
# Description: This is the driver of the program that will create sample graph
#  to answer all programming challenges answers. Then we move towards asking for user input
# to make the graph and give distance in between.
#
#

graph1 = {'A':{'B': 5, 'D':5 , 'E': 7}, 'B':{'C': 4},
          'C':{'D':8 , 'E':2}, 'D':{'C': 8, 'E': 6},
          'E':{'B': 3}}


train = TrainStation(graph1)

#distance of route A-B-C.
print("Output 1 Distance in between :", train.inBetweenDistance(['A', 'B', 'C']))

#distance of route A-D

print("Output 2 Distance in between :", train.inBetweenDistance(['A', 'D']))

#distance of route A-D-C.
print("Output 3 Distance in between :", train.inBetweenDistance(['A', 'D', 'C']))

# Distance of  A-E-B-C-D.
print("Output 4 Distance in between :", train.inBetweenDistance(['A', 'E', 'B', 'C']))

# distance of A-E-D

print("Output 5 Distance in between Cities: ", train.inBetweenDistance(['A', 'E', 'D']))

# number of stops Start at C and end at C max of 3
print("Output 6: Number of stops: ", train.stopCounter('C', 'C', 3))

# Number of stops starting at A and ending at C max of 4
#print("Output 7: Exact Number of stops: ", routes.findExactStops('A','C', 4))

#Length of shortest route A-C
print("Output 8: Shortest Route ", train.shortPath('A', 'C'))

#length of shortest route B-B
print("Output 9: Shortest Route ", train.shortPath('B', 'B'))

#number of different routes
print("Output 10: Different Routes:", train.routesWithin('C', 'C', 30))
