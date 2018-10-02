import search

class EightPuzzle(search.Problem):
    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        self.initial = initial
        self.goal = goal
        search.Problem.__init__(self, initial, goal)

    def actions(self, state):
        # returnib actionite listi

        allowed_actions = ['üles', 'alla', 'vasak', 'parem']
        empty_square = state.index(0)
        # kasutame array nummerdust, mitte goal nummerdus, sest jagub 3-ga paremini
        if empty_square % 3 == 0:
            allowed_actions.remove('vasak')
        if empty_square < 3:
            allowed_actions.remove('üles')
        if empty_square % 3 == 2:
            allowed_actions.remove('parem')
        if empty_square > 5:
            allowed_actions.remove('alla')

        return allowed_actions
    
    def result(self, state, action):
        # returnib UUE oleku
        empty_square = state.index(0)
        new_state = list(state)

        change = {'üles':-3, 'alla':3, 'vasak':-1, 'parem':1}
        neighbor = empty_square + change[action]
        new_state[empty_square], new_state[neighbor] = new_state[neighbor], new_state[empty_square]

        return tuple(new_state)

    def goal_test(self, state):
        # returnib True kui state on lõppolek
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1    # uus cost peale ühe sammu tegemist

    def h1(self, node):
        # Manhattan kaugus iga ruudu jaoks, mis pole eesmärgis
        # Kui liita ruudu index % 3 jääk ja 3ga jagamise tulemus, siis saab hea costmapi
        return sum(abs(s % 3 + s // 3 - g % 3 + g // 3) for (s, g) in zip(node.state, self.goal))


inistate1 = (1,2,3,7,0,5,8,4,6)
inistate2 = (1,8,2,0,4,3,7,6,5)
inistate3 = (5,4,0,6,1,8,7,3,2)
inistate4 = (8,6,7,2,5,4,3,0,1)

problem1 = EightPuzzle(inistate1)
problem2 = EightPuzzle(inistate2)
problem3 = EightPuzzle(inistate3)
problem4 = EightPuzzle(inistate4)

#goalnode = search.breadth_first_graph_search(problem)
# sammud (tegevused, käigud) algolekust lõppolekuni
#print(goalnode.solution())
# olekud algolekust lõppolekuni
#print(goalnode.path())

# search.breadth_first_graph_search - lõpetab 10000 läbivaatamise järel
# search.depth_first_graph_search - lõpetab 10000 läbivaatamise järel
# search.iterative_deepening_search - maksimaalne sügavus: 10
# astar_h1 - lõpetab 10000 läbivaatamise järel
search.compare_searchers([problem1], ["Probleem 1", "Samme lõpuni/Katseid/Olekuid/Lahendusi"],
                      searchers=[search.astar_h1, search.breadth_first_graph_search, search.depth_first_graph_search, search.iterative_deepening_search])
search.compare_searchers([problem2], ["Probleem 2", "Samme lõpuni/Katseid/Olekuid/Lahendusi"],
                      searchers=[search.astar_h1, search.breadth_first_graph_search, search.depth_first_graph_search, search.iterative_deepening_search])
search.compare_searchers([problem3], ["Probleem 3", "Samme lõpuni/Katseid/Olekuid/Lahendusi"],
                      searchers=[search.astar_h1, search.breadth_first_graph_search, search.depth_first_graph_search,
                                    search.iterative_deepening_search])
search.compare_searchers([problem4], ["Probleem 4", "Samme lõpuni/Katseid/Olekuid/Lahendusi"],
                      searchers=[search.astar_h1, search.breadth_first_graph_search, search.depth_first_graph_search,
                                    search.iterative_deepening_search])
# Tulemus: A* on kõige efektiivsem, breadth_first_graph_search järgmine. 3. ja 4. ei lahenda ükski otsing ette antud piirides. 3. lahendus on A*-l 64339 sammu
