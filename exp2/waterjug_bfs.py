from collections import deque
from math import gcd

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    start = (0, 0)
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        jug1, jug2 = queue.popleft()

        if jug1 == target or jug2 == target:
            path = []
            state = (jug1, jug2)
            while state is not None:
                path.append(state)
                state = parent[state]
            return list(reversed(path))

        rules = [
            (jug1_capacity, jug2),
            (jug1, jug2_capacity),
            (0, jug2),
            (jug1, 0),
            (max(0, jug1 - (jug2_capacity - jug2)), min(jug2_capacity, jug1 + jug2)),
            (min(jug1_capacity, jug1 + jug2), max(0, jug2 - (jug1_capacity - jug1)))
        ]

        for next_state in rules:
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (jug1, jug2)
                queue.append(next_state)

    return None

if __name__ == "__main__":
    jug1_cap = int(input("Enter capacity of Jug 1: "))
    jug2_cap = int(input("Enter capacity of Jug 2: "))
    target = int(input("Enter the target amount: "))

    if target > max(jug1_cap, jug2_cap) or target % gcd(jug1_cap, jug2_cap) != 0:
        print("No solution found")
    else:
        result = water_jug_bfs(jug1_cap, jug2_cap, target)

        if result:
            print(f"Solution found for target {target}:")
            for i, state in enumerate(result):
                print(f"Step {i}: Jug1 = {state[0]}, Jug2 = {state[1]}")