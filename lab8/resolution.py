# k6ikide numbriga ruutude peal kutsun välja cnf_sweeper()
# enne peab olema teada kinniste naabrite list


def cnf_sweeper(m, neighbors):
    """CNF komponent ühe ruudu kohta
    parameetrid: m - miinide arv
                neighbors - naabrite list"""
    n = len(neighbors)
    cnf = []
    for i in range(2**n):
        binform = "{:0{n}b}".format(i, n=n)
        ones = 0
        clause = []
        for j in range(n):
            if binform[j] == "1":
                ones += 1
                clause.append(-neighbors[j])
            else:
                clause.append(neighbors[j])
        if ones != m:
            cnf.append(tuple(clause))
            #print(binform, ones, clause)
    return cnf


def pl_resolution(KB, alpha):
    clauses = KB.copy()
    clauses.append(alpha)
    new = set()
    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j])
                 for i in range(n) for j in range(i+1, n)]
        for (ci, cj) in pairs:
            # print(pairs)
            resolvents = pl_resolve(ci, cj)
            print(len(resolvents))
            if () in resolvents:
                return True
            new = new.union(set(resolvents))
        if new.issubset(set(clauses)):
            return False
        for c in new:
            if c not in clauses:
                clauses.append(c)


def pl_resolve(ci, cj):
    clauses = []
    for di in ci:
        for dj in cj:
            #print("di dj ", di, dj)
            if di == (-1*dj) or (-1*di) == dj:
                dnew = list(set((removeall(di, ci) +
                                 removeall(dj, cj))))
                clauses.append(tuple(dnew))
    return clauses


def removeall(el, lst):
    return [x for x in lst if x != el]


# Lahendame Minesweeper väljaku
# 110
# ?1?
# 110
f1 = cnf_sweeper(1, [2, 4, 5])
f2 = cnf_sweeper(1, [1, 3, 4, 5, 6])
f5 = cnf_sweeper(1, [1, 2, 4, 6, 7, 8])
f7 = cnf_sweeper(1, [4, 5, 8])
f8 = cnf_sweeper(1, [4, 5, 6, 7])
# print(f1)
KB_init = f1 + f2 + f5 + f7 + f8
# print(len(KB_init))
KB = list(set(KB_init))
# print(len(KB))

q1 = pl_resolution(KB, (-4,))
print("Ruudul 4: ", q1)
#q2 = pl_resolution(KB, (-6,))
#print("Ruudul 6: ", q2)
