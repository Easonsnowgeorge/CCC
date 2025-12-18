import sys

def solve():
    try:
        line = sys.stdin.read().split()
    except Exception:
        return

    if not line:
        return

    iterator = iter(line)
    try:
        n_str = next(iterator)
        n = int(n_str)
    except StopIteration:
        return

    sheeps = []
    for i in range(n):
        x = float(next(iterator))
        y = float(next(iterator))
        sheeps.append({'x': x, 'y': y, 'id': i, 'eaten': False})

    # Check points along the road (y=0) from x=0 to x=1000
    # We use a fine granularity. 
    # C++ used 100000 steps for 0-1000, so step size 0.01.
    
    steps = 100000
    max_x = 1000.0
    step_size = max_x / steps
    
    for i in range(steps + 1):
        px = i * step_size
        
        min_dist_sq = float('inf')
        
        # Find min distance
        for s in sheeps:
            dist_sq = (s['x'] - px)**2 + s['y']**2
            if dist_sq < min_dist_sq:
                min_dist_sq = dist_sq
        
        # Mark sheep within epsilon of min distance
        epsilon = 1e-9
        for s in sheeps:
            dist_sq = (s['x'] - px)**2 + s['y']**2
            if dist_sq <= min_dist_sq + epsilon:
                s['eaten'] = True

    for s in sheeps:
        if s['eaten']:
            print(f"The sheep at ({s['x']:.2f}, {s['y']:.2f}) might be eaten.")

if __name__ == '__main__':
    solve()
