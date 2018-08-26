from graf import Graf
#import matplotlib.pyplot as plt

# Ändrad för ändringar i graf.py
# Ignorerar nu disconnects, neat

def dia(): # Complexiteten är O(n(V+E)) för varje graf då alla vertex distans beräknas
    p = 1
    meter = []
    point = []
    while not p/10 >= 1:	# Bug med float tal addition, speciellt med 0.1 + 0.1 + 0.1
        mean = []
        e = 0
        while e < 100:
            grp = Graf.random(100, p/10)
            for vert in grp.Dagraph():
                old_vert = 0 # Längsta diameter
                cur = grp.distance(vert)
                if len(cur) == 0: # Ignorera disconnects,  bör göra saker smidigare
                    break
                elif len(cur) > old_vert:
                    old_vert = len(cur)
            if old_vert == 0: # Skippar en iteration för disconnects
                pass
            else:
                mean.append(old_vert)
                e += 1
        meter.append(sum(mean)/100)
        point.append(p/10)
        p += 1 
    # Skriver en tabell för stdout
    for e in range(0, len(point)):
        print(meter[e], point[e])
    #plt.plot(meter, point)
    #plt.savefig("Graph_Diameter")
    #Lär säkert fungera i skolan
if __name__ == "__main__":
    dia()

# Personlingen tycker jag att 0,01 till 0,1 ger mer intressant resultat
