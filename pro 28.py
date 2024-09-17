import heapq
from collections import defaultdict

def networkDelayTime(times, n, k):
    # Create a graph from the times list
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    # Min-heap to store the (time, node)
    min_heap = [(0, k)]
    # Dictionary to track the shortest time to each node
    shortest_times = {i: float('inf') for i in range(1, n + 1)}
    shortest_times[k] = 0

    while min_heap:
        current_time, current_node = heapq.heappop(min_heap)

        # If the current time is greater than the recorded shortest time, skip
        if current_time > shortest_times[current_node]:
            continue

        # Explore neighbors
        for neighbor, travel_time in graph[current_node]:
            time = current_time + travel_time
            # If a shorter time is found, update and push to the heap
            if time < shortest_times[neighbor]:
                shortest_times[neighbor] = time
                heapq.heappush(min_heap, (time, neighbor))

    # The maximum time taken to reach all nodes
    max_time = max(shortest_times.values())
    return max_time if max_time < float('inf') else -1
10:17 am







