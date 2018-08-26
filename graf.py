#Tuple implement with dict()
import random

# Class Method and private variable
# diameter fix

class Graf:

    def __init__(self):
        self.__graph = dict()
        self.__dummy = dict()

    # Tuple input such as (A, B)
    # Kanske har det som A, B så inmatningen ser bättre ut
    def insert_pair(self, a, b): # O(2)
        if a in self.__graph:
            if b in self.__graph[a]:
                print("Edge already existing")
                return
            self.__graph[a].append(b)
        else:
            self.__graph[a] = [b]
        # Kanske onödigt
        if b in self.__graph:
            if a in self.__graph[a]:
                print("Edge already existing")
                return
            self.__graph[b].append(a)
        else:
            self.__graph[b] = [a]


    def remove(self, con): # O(3)
        if len(con) > 2:
            raise IndexError
        a, b = con
        if a in self.__graph:
            if b in self.__graph[a]:
                if [b] == self.__graph[a]:
                    del self.__graph[a]
                else:
                    self.__graph[a].remove(b)
        # Kanske onödigt
        if b in self.__graph:
            if a in self.__graph[b]:
                if [a] == self.__graph[b]:
                    del self.__graph[b]
                else:
                    self.__graph[b].remove(a)


    def clear(self):
        self.__graph = dict()

    def Dagraph(self):
        return self.__graph

    def vertex(self, v):
        return self.__graph[v]

    def sort_edges(self):
        for a in self.__graph:
            self.__graph[a].sort()

    def check_all(self): 
        for a in self.__graph:
            print(a, self.__graph[a])

    # Dess komplexit kommer från att den skapa en koppling mellan alla vert
    @classmethod
    def random(cls, n, p): # O(n(1-n)/2)
        NEW = cls()
        Vert = list(range(1,n+1))
        for alt in Vert:
           NEW.__graph[alt] = []
        for e in Vert :
            for t in range(e+1, n+1):
                if p >= random.random():
                    NEW.__graph[e].append(t)
                    NEW.__graph[t].append(e)
        return NEW


    # O(V + E)  returnerar en dict() med avståndet till noder som 1 : [1,2,5]
    def distance(self, start):
        self.__dummy = dict()
        if self.__graph[start] == []:
            return self.__dummy
        self.__dummy[1] = self.__graph[start]
        self._dist(self.__graph[start], 2, list(set([start]).union(self.__graph[start])))
        return self.__dummy


    def _dist(self, connected, count, visited):
        valid = []
        # samla alla kopplade kanter
        for e in connected:
            valid = list(set(self.__graph[e]).union(valid))
        # tar bort gamla kanter
        valid = list(set(valid)-set(visited))
        if valid == []:
            if len(visited) < len(self.__graph): # Ser om antalet besök är färre än antalet vertex. dvs disconnected
                self.__dummy = dict()
            return
        else:
            visited = list(set(valid).union(visited))
            self.__dummy[count] = valid
            self._dist(valid, count+1, visited)
                

    def __setitem__(self, inp, val):
        self.insert_pair(inp, val)

    def __getitem__(self, inp):
        return self.vertex(inp)

    
if __name__ == "__main__":
    ahoy = Graf()
    # ahoy.random(5, 0.5)
    ahoy.insert_pair("A", "B")
    ahoy.insert_pair("C", "B")
    ahoy.insert_pair("E", "B")
    ahoy["A"] = "E"
    print(ahoy["E"])
    ahoy.remove(("B", "E"))
    ahoy.check_all()


    # Random func test
    

    Rand = Graf.random(100, 0.1)
    print(type(Rand))
    print(Rand.check_all(), "All")
    print(len(Rand.distance(1)))


