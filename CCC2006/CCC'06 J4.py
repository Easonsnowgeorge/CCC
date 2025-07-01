import heapq

# Initial in-degree for each task (number of tasks that must be completed before this one)
reqs = [999, 1, 0, 0, 2, 1, 0, 1]  # 0 is not a valid task number, it's just there for 1-indexing
# Original list representing the graph (dependencies between tasks)
graph = {
    1: [4, 7],
    2: [1],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: []
}

# Loop to take additional input for task dependencies
while True:
    before = int(input())
    after = int(input())
    if before == 0:
        break
    reqs[after] += 1  # Increment in-degree for the task that depends on another
    graph[before].append(after)  # Update the graph with the new dependency

# Priority queue for tasks with no prerequisites
pq = []
for i, val in enumerate(reqs):
    if val == 0:
        pq.append(i)
heapq.heapify(pq)  # Convert the list into a priority queue

# List to store the order in which tasks can be completed
order = []
while pq:
    task = heapq.heappop(pq)  # Pop the task with the smallest number
    order.append(task)

    # Reduce the in-degree of adjacent tasks and add them to the queue if they have no remaining prerequisites
    for adj in graph[task]:
        reqs[adj] -= 1
        if reqs[adj] == 0:
            heapq.heappush(pq, adj)

# Check if all tasks can be completed
if len(order) == 7:
    print(*order)
else:  # Some tasks couldn't be completed due to cyclic dependencies
    print("Cannot complete these tasks. Going to bed.")
