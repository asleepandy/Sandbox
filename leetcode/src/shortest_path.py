import time

neighbours = {
    'A': {'B': 3, 'C': 4},
    'B': {'D': 2},
    'C': {'D': 1, 'E': 1, 'F': 6},
    'D': {'H': 1},
    'E': {'H': 7},
    'F': {'G': 1},
    'G': {},
    'H': {'G': 3}
}
V = {}
P = {}


def find_shortest_path(begin, end):
    # cost = 0
    # path = ''
    # if begin == end:
    #     return
    if begin not in V:
        V[begin] = 0
        P[begin] = [begin]

    for v in neighbours:
        if begin == v:
            for s in neighbours[v]:
                t = V[begin] + neighbours[v][s]
                p = P[begin] + [s]
                if s not in V or t < V[s]:
                    V[s] = t
                    P[s] = p

                find_shortest_path(s, end)
    # print P


def run():
    f = 'A'
    t = 'G'
    start = time.time() * 1000
    find_shortest_path(f, t)
    print P[t]
    end = time.time() * 1000
    print end - start
