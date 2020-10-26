




#
#
# Project Name:   Programming Challenge
# Programmer:    Woodrow Jackson
#
#
# Description: The trainStation class holds all the information needed to help produce the graph.
# The trains station does all the calculations of finding the distance in between cities , searches the routes,
# counts the number of stops, finds the shortest path , and try find a route that has exactly 4 stops
#
#
# from Edge import Edge
class TrainStation:

    # begin = Edge().begin
    # dest = Edge().dest
    # weight = Edge().weight

    depth = 0
    #creating default of a dictionary within constructor
    def __init__(self, routes = {}):
        self.routes = routes


    #distance inbetween cities
    def inBetweenDistance(self, city = []) :
        i =0
        distance =0


        # if there is no distance between no cities or 1
        if(len(city) < 2):
            return 0

        #For each city in the list check if entry exists in the dictionary
        for c in range(len(city)):
            beginNode = city[c]
            if c + 1  < len(city):
                nextNode = city[c+1]

                #if the key exits check if route from key to next city exists

                if nextNode in self.routes[beginNode]:
                    distance = distance + self.routes[beginNode][nextNode]
                else:
                    return "No Such Route"
        return distance


    def searchRoute(self, begin, dest, depth, stops):

        #keep tracks of the visted routes
        visits =[]

        aRoute =0

        if begin in self.routes and self.routes and dest in self.routes:
            depth = depth +1

            #If depth level is within limmit
            if depth > stops:
                return 0
            visits.append(begin)

            for i in self.routes[begin]:

                # if destintion matches route increments

                if i == dest:
                    aRoute = aRoute + 1

                # if destination doesnt match destination has not been vistied
                if i not in visits and i != dest:
                    depth = depth -1
                    aRoute += self.searchRoute(i, dest,depth,stops)

        else:
            return "No Such route"
        if begin in visits:
            visits.remove(begin)
        return aRoute


    #Finding the num of stops
    def stopCounter(self,begin,dest,stops):
        #a wrapper function in which it takes the StopCounter
        # and uses it searchRoute to accomplish
        return self.searchRoute(begin,dest,0,stops)

    # find the shortest path recursively
    def shortPath(self,begin,dest):

        return self.shortPathFinder(begin,dest,0,0)

    def shortPathFinder(self,begin,dest,weight,shortPath, visits = [] ):

        if begin in self.routes and dest in self.routes:
            #the start of the visits
            visits.append(begin)

        for i in self.routes[begin]:

            if(i == dest or i not in visits):

                weight += self.routes[begin][i]


            # Checks if  destination matches, compares weight route
            # to shortest route along the way and makes change

            if i == dest:
                if shortPath == 0 or weight < shortPath:
                    shortPath = weight
                visits.remove(begin)
                return shortPath

            # If the destination does not match
            # as well as the  destination node has not been visited
            # recursively traverse destination node

            if i not in visits:
                shortPath = self.shortPathFinder(i,dest,weight,shortPath,visits)
                weight -= self.routes[begin][i]


            else:
                return "Route does not exist"

            if begin in visits:
                visits.remove(begin)

            return shortPath

    def findRouteInside(self,begin,dest,weight,topDistance,route = 0):
        #checking if the node exists which will then go
        #routes and for each, check if it has destination
        if begin in self.routes and dest in self.routes:

            for i in self.routes[begin]:
                weight += self.routes[begin][i]
                #take the distance if under the max keep moving
                # even if a match is found until distance

                if weight <= topDistance:
                    if i == dest:
                        routes = routes +1
                        routes += self.findRouteInside(i,dest,weight,topDistance)
                    else:
                        routes += self.findRouteInside(i,dest,weight,topDistance)
                        weight -= self.routes[begin][i]

                else:
                    weight -= self.routes[begin][i]

        else:
            print("Route does not Exist")
        return route

    #wrapper function to find the number of routes with the limits
    def routesWithin(self,begin,dest,topDistance):
        return self.findRouteInside(begin,dest,0,topDistance)

    #detects the cycle  in a graph
    def detectCycle(self, begin, path, same, count):

        visits= []
        for nodes_beside in self.routes[begin]:
            if nodes_beside not in visits:
                count = self.cycleFinder(nodes_beside,begin,path,visits,same,count)

        return count

    # goes through the cycle to find the path in the  graph
    def cycleFinder(self, begin, dest,path, visits, same, count):

        visits.append(begin)
        path.append(begin)


        if begin == dest:
            if len(path) == same + 1:
                count = count +1
                print(path)

            else:
                for beside_node in self.routes[begin]:
                    if beside_node not in visits:
                        count = self.cycleFinder(beside_node,dest,path,visits, same, count)

            path.pop()
            visits.remove(begin)

            return count



    #going to method for the cycle detection
    def printAllPaths(self, begin, finish, visits, path, same, counter):

        visits.append(begin)
        path.append(begin)
        if begin == finish:
            if len(path)< same:
                counter = self.cycleFinder(finish, path, same, counter)

            if len(path) == same +1:
                print(path)
                counter = counter + 1

        else:
            for node_beside in self.routes[begin]:
                if node_beside not in visits:
                    counter = self.printAllPaths(node_beside, finish, visits, path, same, counter)


        path.pop()
        visits.remove(begin)

        return counter


    def findExactStops(self, begin, finish, same):
        counter = 0
        visits = []
        path = []

        path.append(begin)
        visits.append(begin)

        for node_beside in self.routes[begin]:

            if node_beside not in visits:

                counter = self.printAllPaths(node_beside, finish, visits, path, same, counter)

        return counter




