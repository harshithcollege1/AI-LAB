import random, time
from collections import deque
GOAL = (1, 2, 3, 4, 0, 5, 6, 7, 8)
def neighbors(state):
    i = state.index(0)
    r, c = divmod(i, 3)
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            s = list(state)
            s[i], s[j] = s[j], s[i]
            yield tuple(s)
def random_state(moves=15):
    s = GOAL
    for _ in range(moves):
        s = random.choice(list(neighbors(s)))
    return s
def bfs(start):
    q, seen = deque([(start, [start])]), {start}
    while q:
        state, path = q.popleft()
        if state == GOAL:
            return path
        for n in neighbors(state):
            if n not in seen:
                seen.add(n)
                q.append((n, path + [n]))
def dfs(start, limit=25):
    stack, seen = [(start, [start])], {start: 0}
    while stack:
        state, path = stack.pop()
        if state == GOAL:
            return path
        if len(path) <= limit:
            for n in neighbors(state):
                if n not in seen or seen[n] > len(path):
                    seen[n] = len(path)
                    stack.append((n, path + [n]))
def run(name, fn, start):
    t = time.perf_counter()
    path = fn(start)
    dt = time.perf_counter() - t
    moves = len(path) - 1 if path else "no solution"
    print(f"{name:4} moves: {moves}   time: {dt:.3f}s")
start = random_state()
print("Start state:")
for i in range(0, 9, 3):
    print(*start[i:i+3])
print()
run("BFS", bfs, start)
run("DFS", dfs, start)