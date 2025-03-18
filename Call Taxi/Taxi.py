class Taxi:
    def __init__(self,):
        self.taxi_id = None
        self.cur_loc = "A"
        self.customer_id = None
        self.pickupLoc = None
        self.dropLoc = None
        self.pickTime = None
        self.tripEnd = None
        self.earnings = 0
        self.curEarning = 0

    

    def calculateTripEnd(self):
        locs = ["A", "B", "C", "D", "E", "F"]
        tripDistance = abs(locs.index(self.dropLoc) - locs.index(self.pickupLoc))
        
        self.tripEnd = self.pickTime + tripDistance

    def calculateEarnings(self):
        locs = ["A", "B", "C", "D", "E", "F"]
        tripDistance = abs(locs.index(self.dropLoc) - locs.index(self.pickupLoc)) * 15
        curEarning = 100

        tripDistance -= 5

        curEarning += (tripDistance*10)

        self.curEarning = curEarning
        self.earnings = self.earnings +  curEarning
        #print(self.earnings)


    def isFree(self, pickTime):
        if pickTime >=  self.tripEnd:
            return True
        else:
            return False


# temp = Taxi()

# temp.calculateTripEnd()

