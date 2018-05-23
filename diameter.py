from graf import Graf
#import matplotlib.pyplot as plt

# Ändrad för ändringar i graf.py

def dia():
    p = 1
    meter = []
    point = []
    while not p/10 >= 1:	# Bug med float tal addition, speciellt med 0.1 + 0.1 + 0.1
        grp = Graf.random(100, p/10)
        old_vert = 0
        for vert in grp.Dagraph():
            cur = grp.distance(vert)
            if len(cur) > old_vert:
                old_vert = len(cur)
        meter.append(old_vert)
        point.append(p/10)
        p += 1 
    # Skriver en tabell för stdout
    for e in range(0, len(point)):
        print(meter[e], point[e])
    #plt.plot(meter, point)
    #plt.savefig("Graph_Diameter")
    #Lär säkert fungera i skolan

dia()

# Personlingen tycker jag att 0,01 till 0,1 ger mer intressant resultat
