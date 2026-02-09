from math import gcd

def water_jug_dfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    path = []
    
    def dfs(jug1, jug2):
        if jug1 == target or jug2 == target:
            path.append((jug1, jug2))
            return True
        
        state = (jug1, jug2)
        if state in visited:
            return False
        
        visited.add(state)
        path.append(state)
        operations = [
            (jug1_capacity, jug2), 
            (jug1, jug2_capacity),  
            (0, jug2),         
            (jug1, 0),          
            (max(0, jug1 - (jug2_capacity - jug2)), min(jug2_capacity, jug1 + jug2)),
            (min(jug1_capacity, jug1 + jug2), max(0, jug2 - (jug1_capacity - jug1)))
        ]
        
        for next_state in operations:
            if dfs(next_state[0], next_state[1]):
                return True
        
        path.pop()
        return False   
    
    if dfs(0, 0):
        return path
    return None

if __name__ == "__main__":
    jug1_cap = int(input("Enter capacity of Jug 1: "))
    jug2_cap = int(input("Enter capacity of Jug 2: "))
    target = int(input("Enter the target amount: "))
    
    if target > max(jug1_cap, jug2_cap) or target % gcd(jug1_cap, jug2_cap) != 0:
        print("No solution found (mathematically impossible)")
    else:
        result = water_jug_dfs(jug1_cap, jug2_cap, target)
        
        if result:
            print(f"Solution found for target {target}:")
            for i, state in enumerate(result):
                print(f"Step {i}: Jug1 = {state[0]}, Jug2 = {state[1]}")
        else:
            print("No solution found")