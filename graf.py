#Tuple implement with dict()
import random

# Ändrar om för privata variable, class metod

class Graf:

    def __init__(self):
        self.graph = dict()
        self.dummy = dict()

    # Tuple input such as (A, B)
    def insert_pair(self, a, b): # O(3)
        if a in self.graph:
            if b in self.graph[a]:
                print("Edge already existing")
                return
            self.graph[a].append(b)
        else:
            self.graph[a] = [b]
        if b in self.graph:
            if a in self.graph[a]:
                print("Edge already existing")
                return
            self.graph[b].append(a)
        else:
            self.graph[b] = [a]

    def remove(self, con): # O(3)
        if len(con) > 2:
            raise IndexError
        a, b = con
        if a in self.graph:
            if b in self.graph[a]:
                if [b] == self.graph[a]:
                    del self.graph[a]
                else:
                    self.graph[a].remove(b)
        # Kanske onödigt
        if b in self.graph:
            if a in self.graph[b]:
                if [a] == self.graph[b]:
                    del self.graph[b]
                else:
                    self.graph[b].remove(a)


    def clear(self):
        self.graph = dict()


    def vertex(self, v):
        return self.graph[v]

    def sort_edges(self):
        for a in self.graph:
            self.graph[a].sort()

    def check_all(self): 
        for a in self.graph:
            print(a, self.graph[a])

    # Dess komplexit kommer från att den skapa en koppling mellan alla vert
    def random(self, n, p): # O(n(1-n)/2)
        self.clear()
        Vert = list(range(1,n+1))
        for alt in Vert:
            self.graph[alt] = []
        for e in Vert :
            for t in range(e+1, n+1):
                if p >= random.random():
                    self.graph[e].append(t)
                    self.graph[t].append(e)



    # O(V + E) kollar alla koppling som sen kollas efter deras kopplingar
    # Ser en lite ineffektivitet vid E då den kollar kopplingen från
    # föregående Node, Lägger till en extra koppling koll
    def distance(self, start):
        self.dummy = dict()
        if self.graph[start] == []:
            print("invalid start")
            return
        self.dummy[1] = self.graph[start]
        self._dist(self.graph[start], 2, list(set([start]).union(self.graph[start])))


    def _dist(self, connected, count, visited):
        valid = []
        # samla alla kopplade kanter
        for e in connected:
            valid = list(set(self.graph[e]).union(valid))
        # tar bort gamla kanter
        valid = list(set(valid)-set(visited))
        if valid == []:
            return
        else:
            visited = list(set(valid).union(visited))
            self.dummy[count] = valid
            self._dist(valid, count+1, visited)
                

    def __setitem__(self, vert, end):
        self.insert_pair(vert, end)

    def __getitem__(self, inp):
        return self.vertex(inp)

    
if __name__ == "__main__":
    ahoy = Graf()
    # ahoy.random(5, 0.5)
    ahoy.insert_pair("A", "B")
    ahoy.insert_pair("C", "B")
    ahoy.insert_pair("E", "B")
    ahoy.insert_pair("A", "E")
    ahoy["C"] = "E"
    ahoy["B"] = "A" # Error check
    print(ahoy["E"])
    ahoy.check_all()
    print("")
    ahoy.remove(("B", "E"))
    ahoy.check_all()



    # Random func test

    print("random test")

    ahoy.random(10, 0.5)
    ahoy.check_all()
    print("")
    ahoy.distance(1)
    print(ahoy.dummy)
    print(len(ahoy.dummy))
    for e in ahoy.dummy:
        print(e)
