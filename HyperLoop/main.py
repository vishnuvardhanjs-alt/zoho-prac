from passenger import Passenger
import heapq

class HyperLoop:
    def __init__(self, count, start):
        self.start = start
        self.routes = self.getRoutes(count)
        self.Passengers = []

        

    def getRoutes(self, count):
        dic = {}

        for i in range(count):
            curinp = input().split()


            temp = dic.get(curinp[0], [])
            temp.append(curinp[1])

            dic[curinp[0]] = temp
        
        print(dic)

        return dic
    

    def addPassenger(self, name, age, dest):
        tempPassenger = Passenger(name, age, dest)
        tempPassenger.getRoute(self.start, dest, "", self.routes)
        heapq.heappush(self.Passengers, (-1*age, tempPassenger))
    
    def startPod(self):
        _, passenger = heapq.heappop(self.Passengers)
        print(passenger.name, " ", passenger.route)

    def printQueue(self):
        print(len(self.Passengers))
        for i, j in self.Passengers:
            print(j.name, " ", j.age)
    

head = HyperLoop(7, "A")

head.addPassenger("ravi", 22, "C")
head.addPassenger("hari", 33, "D")
head.addPassenger("bala", 10, "E")
head.startPod()
head.printQueue()


