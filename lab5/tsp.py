import search

# heuristik
def 2optSwap(route, i, k)
       new_route = []
       #1. take route[0] to route[i-1] and add them in order to new_route
       #2. take route[i] to route[k] and add them in reverse order to new_route
       #3. take route[k+1] to end and add them in order to new_route
       return new_route


class TSP(search.Problem):
    def __init__(self, instance):
        # laadi sisse ülesanne sobival kujul
        # genereeri algolek (võib olla list linnade indeksitest)

    def actions(self, state):
        # siin genereerime võimalikud lahti ühendatavate graafi kaarte paarid 2-Opt jaoks

    def result(self, state, action):
        # siin tekitame uue oleku, kus mingid kaared lahti ühendatakse ja teistpidi kokku ühendatakse, kasutades ülalolevat pseudokoodi.
        # action on üks i, j paar.

    def cost(self, state):
        # arvuta (või leia muul viisil) praeguse marsruudi kogupikkus. Ära unusta, et marsruut on suletud.

    def value(self, state)
        # kuna valmis otsingufunktsioonid arvavad, et mida suurem väärtus, seda parem, siis meie minimeerimisülesande TSP
        # lahendamiseks tuleb teepikkusest pöördväärtus võtta.
        return 1/(self.cost(state)+1)

p = search.InstrumentedProblem(TSP("gr48"))
g = search.hill_climbing(p)
print(g.state)
print(p.cost(g.state))

#SA kasutamine vaikimisi parameetritega ja natuke pikendatud otsinguga:

#g = search.simulated_annealing(p)
#g = search.simulated_annealing(p, search.exp_schedule(limit=10000))