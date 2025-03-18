class Passenger:

    def __init__(self, name, age, dest ):
        self.name = name
        self.age = age
        self.dest = dest
        self.route = None
    
    def getRoute(self, cur, dest,curStr, routes):
        if curStr!= "" and cur == dest:
            if not self.route:
                self.route = curStr + cur
            elif len(curStr) < len(self.route):
                self.route = curStr + cur

            return
        if cur in routes.keys():
            for i in routes[cur]:
                self.getRoute(i, dest, curStr+cur, routes)
