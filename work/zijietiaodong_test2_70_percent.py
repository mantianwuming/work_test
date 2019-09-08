import sys

def pour(X,Y,Z, goal, start=(0,0,0)):
    if goal in start:
        return [start]
    explored = set()
    frontier = [[start]]
    while frontier:
        path = frontier.pop(0)
        (x,y,z) = path[-1]
        for (state, action) in successors(x, y, z, X, Y, Z).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if goal in state:
                    return path2
                else:
                    frontier.append(path2)
    return Fail
Fail = []

def successors(x, y, z, X, Y, Z):
    assert x <= X and y <= Y and z <= Z
    return {((0, x+y, z) if x+y < Y else (x-(Y-y), Y, z)): 'X->Y',
             (x+y, 0, z) if x+y < X else (X, y-(X-x),z): 'Y->X',
             (0, y, z+x) if z+x < Z else (x-(Z-z), y, Z): 'X->Z',
             (x, 0, z+y) if z+y < Z else (x, y-(Z-z), Z): 'Y->Z',
             (x, y+z, 0) if y+z < Y else (x, Y, z-(Y-y)): 'Z-Y',
             (x+z, y, 0) if x+z < X else (X, y, z-(X-x)): 'Z->X',
             (X,y,z): 'fill X', (x,Y,z):'fill Y', (x,y,Z):'fill Z',
             (x,0,z): 'empty Y', (0,y,z): 'empty X', (0,y,z): 'empty Z'}

[a, b, c, d] = [int(i) for i in sys.stdin.readline().split()]
res = pour(a, b, c, d, (0,0,0))
res = int((len(res)-1)/2)
print(res)