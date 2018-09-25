# Heuristic search
from queue import Queue, PriorityQueue



def check_node(map, point, char):
    (x, y) = point
    if map[y][x] == char:
        return True
    else:
        return False


def neighbors(map, point):
    (x, y) = point
    results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
    def in_bounds(p1):
        (x, y) = p1
        return 0 <= x < len(map[0]) and 0 <= y < len(map)
    def passable(p2):
        return not check_node(map, p2, '*')

    results = [x for x in results if in_bounds(x)]
    results = [x for x in results if passable(x)]
    return results


def find_point(map, targetChar):
    col = 0
    for string in map:
        row = string.find(targetChar)
        if row > -1:
            return (row, col)
        else:
            col = col + 1
    return -1

def get_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    return path

def char_to_print(prev, next):
    if next == None:
        return 's'
    (px, py) = prev
    (nx, ny) = next
    if px == nx and py < ny:
        return '^'
    elif px == nx and py > ny:
        return 'v'
    elif px < nx:
        return '<'
    else:
        return '>'


def draw_grid(edges, map):
    i = 0
    new_map = [None] * len(map)
    for row in map:
        new_map[i] = list(row)
        i = i + 1
    for edge in edges:
        (x, y) = edge
        if new_map[y][x] != 'D':
            new_map[y][x] = char_to_print(edge, edges[edge])
    for row in new_map:
        print(''.join(row))
    return new_map


def draw_path(edges, map):
    for edge in edges:
        (x, y) = edge
        map[y][x] = '#'
    for row in map:
        print(''.join(row))

def heuristic(x, y):
    (x1, x2) = x
    (y1, y2) = y
    return abs(x1 - y1) + abs(x2 - y2)

def breadth_first_search(map):
    start = find_point(map, 's')
    if start == -1:
        return "No starting point"
    map_height = len(map)
    if map_height < 1:
        return "Invalid map"
    map_width = len(map[0])
    if map_width < 1:
        return "Invalid map"
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if check_node(map, current, 'D'):
            diamond = current
            break

        for next_point in neighbors(map, current):
            if next_point not in came_from:
                frontier.put(next_point)
                came_from[next_point] = current

    path = get_path(came_from, start, diamond)

    return came_from, path

def heuristic_search(map, goal):
    start = find_point(map, 's')
    if start == -1:
        return "No starting point"
    map_height = len(map)
    if map_height < 1:
        return "Invalid map"
    map_width = len(map[0])
    if map_width < 1:
        return "Invalid map"
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        _, current = frontier.get()

        if check_node(map, current, 'D'):
            diamond = current
            break

        for next_point in neighbors(map, current):
            if next_point not in came_from:
                priority = heuristic(goal, next_point)
                frontier.put((priority, next_point))
                came_from[next_point] = current
    path = get_path(came_from, start, diamond)

    return came_from, path

def astar(map, goal):
    start = find_point(map, 's')
    if start == -1:
        return "No starting point"
    map_height = len(map)
    if map_height < 1:
        return "Invalid map"
    map_width = len(map[0])
    if map_width < 1:
        return "Invalid map"
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    came_from[start] = None
    cost_so_far = {}
    cost_so_far[start] = 0

    while not frontier.empty():
        _, current = frontier.get()

        if check_node(map, current, 'D'):
            diamond = current
            break

        for next_point in neighbors(map, current):
            new_cost = cost_so_far[current] + 1
            if next_point not in came_from or new_cost < cost_so_far[next_point]:
                cost_so_far[next_point] = new_cost
                priority = heuristic(goal, next_point)
                frontier.put((priority, next_point))
                came_from[next_point] = current
    path = get_path(came_from, start, diamond)

    return came_from, path

def draw_results(came_from, path, map):
    print("Search results:")
    new_map = draw_grid(came_from, map)

    print("The path to the diamond:")
    draw_path(path, new_map)

def main():
    print("Cave 300x300")
    with open("cave300x300.txt") as f:
        map = [l.strip() for l in f.readlines() if len(l) > 1]
    goal = find_point(map, 'D')
    came_from, path = breadth_first_search(map)
    print("Breadth-first search:")
    print(len(path))
    # draw_results(came_from, path, map)
    came_from, path = heuristic_search(map, goal)
    print("Heuristic search:")
    print(len(path))
    # draw_results(came_from, path, map)
    came_from, path = astar(map, goal)
    print("A*:")
    print(len(path))
    #draw_results(came_from, path, map)

    print("Cave 600x600")
    with open("cave600x600.txt") as f:
        map = [l.strip() for l in f.readlines() if len(l) > 1]
    goal = find_point(map, 'D')
    came_from, path = breadth_first_search(map)
    print("Breadth-first search:")
    print(len(path))
    # draw_results(came_from, path, map)
    came_from, path = heuristic_search(map, goal)
    print("Heuristic search:")
    print(len(path))
    # draw_results(came_from, path, map)
    came_from, path = astar(map, goal)
    print("A*:")
    print(len(path))
    # draw_results(came_from, path, map)

    print("Cave 900x900")
    with open("cave900x900.txt") as f:
        map = [l.strip() for l in f.readlines() if len(l) > 1]
    goal = find_point(map, 'D')
    came_from, path = breadth_first_search(map)
    print("Breadth-first search:")
    print(len(path))
    # draw_results(came_from, path, map)
    came_from, path = heuristic_search(map, goal)
    print("Heuristic search:")
    print(len(path))
    # draw_results(came_from, path, map)
    came_from, path = astar(map, goal)
    print("A*:")
    print(len(path))
    # draw_results(came_from, path, map)

main()
