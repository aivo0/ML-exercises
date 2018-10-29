from collections import defaultdict

# ['P', 'Q']
# ['L', 'M', 'P']
# ['B', 'L', 'M']
# ['A', 'P', 'L']
# ['A', 'B', 'L']
# A
# B

kb = [
    ["Q", "P"],
    ["P", "L", "M"],
    ["M", "B", "L"],
    ["L", "A", "P"],
    ["L", "A", "B"],
    ["A"],
    ["B"]
]

cmap = {
    "A": [3, 4, 5],
    "B": [4, 6],
    "P": [0,1,3],
    "Q": [0],
    "L": [1, 2, 3, 4],
    "M": [2]
}

counts = {
    "A": 2,
    "B": 1,
    "P": 3,
    "Q": 1,
    "L": 4,
    "M": 2
}

agenda = ["A", "B"]
# agenda = ["P", "Q", "L", "M", "B", "A"]

def fc_entails(kb, counts, agenda, cmap, q):
    inferred = defaultdict(bool)
    while agenda:
        print(agenda)
        p = agenda.pop()
        if p == q:
            return True
        if not inferred[p]:
            inferred[p] = True
            for c in cmap[p]:
                clause = kb[c]
                print("clause: ", clause)
                counts[p] -= 1
                if counts[p] == 0:
                    agenda.append(clause[-1])
    return False

res = fc_entails(kb, counts, agenda, cmap, "Q")
print(res)
