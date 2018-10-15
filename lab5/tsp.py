import search
import random
import csv


class TSP(search.Problem):
    def __init__(self, cities):
        self.cities = cities
        search.Problem.__init__(self, cities)

    # https://en.wikipedia.org/wiki/2-opt
    def two_opt_swap(self, cities):
        route = cities[:]
        first = random.randint(0, len(route) - 1)
        second = random.randint(0, len(route) - 1)
        if first > second:
            first, second = second, first
        route[first: second + 1] = reversed(route[first: second + 1])
        return route

    def actions(self, cities):
        return [self.two_opt_swap]

    def result(self, cities, action):
        return action(cities)

    def cost(self, state):
        # Cost is total distance if in state
        cost = 0
        for i in range(len(state) - 1):
            cost += distances[state[i]][state[i + 1]]
        cost += distances[state[0]][state[-1]]
        return cost

    def value(self, state):
        # kuna valmis otsingufunktsioonid arvavad, et mida suurem väärtus, seda parem, siis meie minimeerimisülesande TSP
        # lahendamiseks tuleb teepikkusest pöördväärtus võtta.
        return 1/(self.cost(state)+1)


distances = []

# Change filename here to try other inputs
with open('gr120.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    row_count = int(reader.__next__()[0])

    for row in reader:
        ints = list(map(int, row))
        distances.append(ints)

cities = list(range(len(distances)))

p = search.InstrumentedProblem(TSP(cities))
g = search.hill_climbing(p)
print("Hill climbing:", g)
print(p.cost(g))

g = search.simulated_annealing(p)
p = search.InstrumentedProblem(TSP(cities))
print("Simulated anneling:", g)
print(p.cost(g))

g = search.simulated_annealing(p, search.exp_schedule(limit=100000))
p = search.InstrumentedProblem(TSP(cities))
print("Extended simulated anneling", g)
print(p.cost(g))

# achieved costs with gr120.txt: 50021, 41988, 7562. Best known result is 6942
