from collections import defaultdict
from itertools import permutations, repeat

# 0 ['P', 'Q']
# 1 ['L', 'M', 'P']
# 2 ['B', 'L', 'M']
# 3 ['A', 'P', 'L']
# 4 ['A', 'B', 'L']
# 5 A
# 6 B

kb = [
    ["P", "Q"],
    ["L", "M", "P"],
    ["B", "L", "M"],
    ["A", "P", "L"],
    ["A", "B", "L"],
    ["A"],
    ["B"]
]

cmap = {
    "A": [3, 4],
    "B": [2, 4],
    "P": [0, 3],
    "Q": [],
    "L": [1, 2],
    "M": [1]
}

counts = {
    0: 1,
    1: 2,
    2: 2,
    3: 2,
    4: 2,
    5: 1,
    6: 1
}
agenda = ["A", "B"]


def fc_entails(kb, counts, agenda, cmap, q):
    inferred = defaultdict(bool)
    while agenda:
        #print("agenda:", agenda)
        p = agenda.pop()
        if p == q:
            return True
        if not inferred[p]:
            inferred[p] = True
            for c in cmap[p]:
                clause = kb[c]
                #print("clause:", c, clause[-1])
                counts[c] -= 1
                # print(counts)
                if counts[c] == 0:
                    agenda.append(clause[-1])
                    #print("new agenda:", agenda)
    return False


res = fc_entails(kb, counts, agenda, cmap, "Q")
# print(res)

kb2 = []
kb_solutions = ["KI", "PA", "KÄ"]
kb_elems = list(kb_solutions)
perm = permutations(kb_elems)
for i in list(perm):
    kb2.append([i[0]+"1", i[1]+"2", i[2]])
    if not i[0]+"1" in kb_elems:
        kb_elems.append(i[0]+"1")
    if not i[1]+"2" in kb_elems:
        kb_elems.append(i[1]+"2")
# kb2.append(["KI1", "PA2", "KÄ"])
# kb2.append(["PA1", "KÄ2", "KI"])
# kb2.append(["KÄ1", "KI2", "PA"])
for i in list(range(len(kb_solutions))):
    item = list(repeat(kb_elems[i], 3))
    kb2.append([item[0]+"1", item[1]+"2", item[2]])
#print("kb2", kb2)
#print("kb_elems", kb_elems)
counts2 = list(repeat(2, len(kb2)))
#print("counts2", counts2)

premises = [item for item in kb_elems if item not in kb_solutions]
#cmap2 = dict(zip(list(premises), list(repeat(list([]), len(premises)))))
cmap2 = {
    "KI1": [],
    "KI2": [],
    "PA1": [],
    "PA2": [],
    "KÄ1": [],
    "KÄ2": [],
    "KI": [],
    "PA": [],
    "KÄ": []
}
#print("premises", premises)

index = 0
for sentence in kb2:
    for move in premises:
        if move in sentence[0:2]:
            cmap2[move].append(index)
    index = index + 1
#print("cmap2", cmap2)


def get_agenda(m1, m2):
    return [m1+"1", m2+"2"]


def translate(move):
    if move == "Kivi":
        return "KI"
    if move == "Paber":
        return "PA"
    else:
        return "KÄ"


def clever_move(prediction):
    if prediction == "KI":
        return "Paber"
    if prediction == "PA":
        return "Käärid"
    else:
        return "Kivi"


def kkp(move1, move2):
    m1 = translate(move1)
    m2 = translate(move2)
    prediction = ""
    for move in kb_solutions:
        # Pass only copies so that if function mutates parameters, there won't be side-effects
        if fc_entails(list(kb2), list(counts2), list(get_agenda(m1, m2)), cmap2.copy(), move):
            prediction = move
            break
    print("inimene käis:", move1, move2)
    print("roboti käik:", clever_move(prediction))


kkp("Paber", "Käärid")
kkp("Kivi", "Kivi")
