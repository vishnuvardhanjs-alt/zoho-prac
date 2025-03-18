from Taxi import Taxi
import copy

class Main:
    def __init__(self, taxiCount):
        self.taxiCount = taxiCount
        self.History = {}
        self.Locations = {"A":[], "B":[], "C":[], "D":[], "E":[], "F": []}
        self.freeTaxi = []
        for i in range(taxiCount):
            temp = Taxi()
            temp.taxi_id = taxiCount - i
            self.freeTaxi.append(temp)

    def getNearestTaxi(self, curLoc, pickTime):
        locs = ["A","B", "C", "D", "E", "F"]

        curPos = ord(curLoc)%ord("A")


        min_dis = float("inf")
        min_loc = None
        min_earnings = float("inf")

        for i in range(curPos, len(locs)):
            if self.Locations[locs[i]]:
                for taxi in self.Locations[locs[i]]:
                    if taxi.isFree(pickTime):
                        if taxi.earnings < min_earnings:
                            min_earnings = taxi.earnings
                            min_dis = i - curPos
                            min_loc = taxi
                        
                if min_loc != None:
                    break
        
        min_earnings = float("inf")
        for j in range(curPos, -1,-1):
            if self.Locations[locs[j]]:
                for taxi in self.Locations[locs[j]]:
                    cur_min_dis = 0
                    if taxi.isFree(pickTime):
                        cur_min_dis = curPos - j
                        if cur_min_dis < min_dis:
                            if taxi.earnings < min_earnings:
                                min_loc = taxi
                            
        
        return min_loc


    def bookTaxi(self, customer_id, pickupLoc, dropLoc, pickTime):
        curTaxi = None
        
        
        curTaxi = self.getNearestTaxi(pickupLoc, pickTime)

        if curTaxi == None:
            if self.freeTaxi:
                curTaxi = self.freeTaxi.pop()
            
        if curTaxi:
            curTaxi.customer_id = customer_id
            curTaxi.pickupLoc = pickupLoc
            curTaxi.dropLoc = dropLoc
            curTaxi.pickTime = pickTime
            curTaxi.cur_loc = dropLoc
            curTaxi.calculateTripEnd()
            curTaxi.calculateEarnings()
            for i,j in self.Locations.items():
                for p in range(len(j)):
                    if j[p] == curTaxi:
                        self.Locations[i].pop(p)
                        break
            self.Locations[dropLoc].append(curTaxi)

            curHis = self.History.get(curTaxi.taxi_id, [])
            curHis.append(copy.deepcopy(curTaxi))
            self.History[curTaxi.taxi_id] = curHis
            #print(curTaxi.taxi_id)
            return curTaxi.taxi_id
        else:
            return False
        
    def printDetails(self):
        for i, j in self.History.items():
            print("Taxi_Number - ", i, " Total Earnings = ", j[-1].earnings)
            print("CustomerId\tFrom\tTo\tPickupTime\tDropTime\tAmount")
            for taxi in j:
                print(f"{taxi.customer_id}\t\t{taxi.pickupLoc}\t{taxi.dropLoc}\t{taxi.pickTime}\t\t{taxi.tripEnd}\t\t{taxi.curEarning}")
            
            print()



cur = Main(4)

cusId = 1

while True:
    print("1. Book Taxi")
    print("2. Get Details")

    opt = int(input())
    if opt == 1:
        pick = input("Pickup Location : ").upper()
        drop = input("Drop Location : ").upper()
        time = int(input("Pickup Time : "))
        book = cur.bookTaxi(cusId, pick, drop, time)
        if book != False:
            print("Booking Successful!")
            print("Taxi ", book, "Alloted")
            cusId += 1
        else:
            print("All Taxi's are Busy!")
    elif opt == 2:
        cur.printDetails()
    else:
        print("Enter Correct Option")
    
    print()


        


