from collections import defaultdict

# ['P', 'Q']
# ['L', 'M', 'P']
# ['B', 'L', 'M']
# ['A', 'P', 'L']
# ['A', 'B', 'L']
# A
# B

count = [
    "Q", ["P"],
    "P", ["L", "M"],
    "M", ["B", "L"],
    "L", ["A", "P"],
    "L", ["A", "B"],
]

agenda = ["A", "B"]
# agenda = ["P", "Q", "L", "M", "B", "A"]

def fc_entails(count, agenda, q):
    inferred = defaultdict(bool)
    while agenda:
        p = agenda.pop()
        if p == q:
            return True
        if not inferred[p]:
            inferred[p] = True
            for c in count(p):
                count[c] -= 1
                if count[c] == 0:
                    agenda.append(c.args[1])
    return False

res = fc_entails(count, agenda, "Q")

