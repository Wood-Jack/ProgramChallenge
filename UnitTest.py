
from TrainStation import TrainStation


#
#
# Project Name:   UnitTest
# Programmer:    Woodrow Jackson
#
#
# Description: This is the driver of the program that will create sample graph
#  to answer all programming challenges answers. Then we move towards asking for user input
# to make the graph and give distance in between.
#
#


tgraph = {'A':{'B': 5, 'D':5 , 'E': 7}, 'B':{'C': 4},
          'C':{'D':8 , 'E':2}, 'D':{'C': 8, 'E': 6},
          'E':{'B': 3}}

testTrain = TrainStation(tgraph)

#tests output 1
def testingInBetween_ABC(): assert testTrain.inBetweenDistance(['A', 'B', 'C']) == 9

#tests output 2
def testingInBetween_AD(): assert testTrain.inBetweenDistance( ['A', 'D']) == 5


#tests output 3
def testingInBetween_ADC():  assert testTrain.inBetweenDistance( ['A', 'D','C']) == 13

#tests output 4
def testingInBetween_AEBCD(): assert testTrain.inBetweenDistance(['A','E','B', 'C','D']) == 22

#tests output 5

def testingInBetween_AED(): assert testTrain.inBetweenDistance( ['A', 'E','D']) == "No Such Route"

#tests output 6

def testingStopCounter_CC3(): assert testTrain.stopCounter('C','C',3) ==3

#output 7 yet to be completed
#
#
#

#tests output 8
def testingShortPath_AC(): assert testTrain.shortPath('A','C')== 9

# tests output 9
def testingShortPath_BB(): assert testTrain.shortPath('B','B') == 9


#output 10 yet to be resolved
#
#
#
#
#