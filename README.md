# ProgramChallenge


This was quite a hard programming challenge I was thinking of doing this challenge in Java or C++. I finally decided to do it in Python. Because it was one of the skills listed in the posting and I'm also familiar with it.

I would also create less classes in Python then the other programming languages needed.I started off with trying to create a class class named Edge.
Stop programming the Edge Class and primary focuse on these two class that does it all.

For the programming challenge I used two classes one is named TrainStation and another is called MainDriver

The TrainStation class is a class that holds all the information needed to be able to  calculate the distance inbetween the Nodes, number of stops , shortest route, and 
give the different number of routes within a given limit. The trainstation will take in a dictionary

Within the Train Station Functions I will list some of its functions

def inBetweenDistance(self, city = []):Creating this function with an array because when your searching throught things you need an array to do that
with. I check if an entry exists and adding the weight to for the total distance

def searchRoute(self, begin, dest, depth, stops): This is a searcher function in which will help another function named stopCounter. With the Search Route function it will keep track of the visited routes. It will also increment the route if it matches.

def stopCounter(self,begin,dest,stops): is a wrapper function in which it takes the searchRoute and uses it to search around the route. It will only need to take in Begining node and ending node as well as the max number of stops

Same as before but with the previous two functions I use it to complete the shortest path function

def shortPathFinder(self,begin,dest,weight,shortPath, visits = [] ): This is another searcher function in which it will search around for the shortest route. It will first check if the begin and dest nodes exist. It will check if the destantion matches and then it will compare its weight with a one the shortest routes. If destination doesnt match and dest node has not been visited it keeps searching



The MainDriver Class is where all the action takes place.I first import the TrainStation class into the MainDriver class. I create a graph of the challenge givent to me.

I create an object of TrainStation class named train from the train object I do several tasks.

with train I call the functions of the TrainStation and then continue to display them on the screen.  





