import sys

# Fel sökning, tom lista och första raden

f = sys.stdin

def read_dot():
    Vert = []
    Edges = []
    a = f.readline()
    a = f.readline()
    while a != "}\n":
        a = a.replace(";","")
        cur = a.split()
        if cur[1] != "--":
             raise IndexError("Wrong Input form, unexact form")
        if len(cur) > 3:
             raise IndexError("Wrong Input form, too many elements")
        if cur[0] not in Vert:
             Vert.append(cur[0])
        if cur[2] not in Vert:
             Vert.append(cur[2])
        if (cur[0], cur[2]) not in Edges and (cur[2], cur[0]) not in Edges:
             Edges.append((cur[0], cur[2]))
        a = f.readline()
    print(Vert)
    print(Edges)

read_dot()

