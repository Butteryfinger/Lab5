import sys

def read_dot(f):
    Vert = []
    Edges = []
    a = f.readline()
    if "{" not in a or a == []:
        raise IndexError("Wrong Input form, unexact form")
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
        if (cur[0], cur[2]) not in Edges:
            if (cur[2], cur[0]) not in Edges:
                Edges.append((cur[0], cur[2]))
        else:
            Edges.append((cur[0], cur[2]))
        a = f.readline()
    DOT = Graf()
    for e in Edges:
        a, b = e
        DOT.insert_pair(a,b)
    for t in DOT.Dagraph():
        print(t, ";" ,DOT.vertex(t))

read_dot(sys.stdin)
