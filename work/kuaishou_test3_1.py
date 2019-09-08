import sys
n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
distance = list(map(int, line.split()))
line = sys.stdin.readline().strip()
energy = list(map(int, line.split()))

class solution:
    def __init__(self, max_dist, energy):
        self.max_dist = max_dist
        self.energy = energy
    
    def get_energy(self, i, dist, energy):
        if dist[i] > self.max_dist:
            self.energy = self.energy - 2 * self.max_dist + 2 * dist[i]
            self.energy = self.energy + energy[i]
            self.max_dist = dist[i]
        else:
            self.energy = self.energy + energy[i]

cur = []
cur_dist = 0
cur_energy = 0
for i in range(n):
    max_dist = 0
    max_energy = 0
    for i in range(n):
        if i not in cur:
            so = solution(cur_dist, cur_energy)
            so.get_energy(i, distance, energy)
            if so.energy > max_energy:
                max_ind = i
                max_energy = so.energy
                max_dist = so.max_dist
    print(max_energy)
    cur_dist = max_dist
    cur_energy = max_energy
    cur.append(max_ind)