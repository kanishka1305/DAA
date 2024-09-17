from collections import defaultdict
import heapq

def maxProbability(n, edges, succProb, start, end):
    graph = defaultdict(list)
    
    # Build the graph
    for (a, b), prob in zip(edges, succProb):
        graph[a].append((b, prob))
        graph[b].append((a, prob))
    
    # Max heap to store the probabilities
    max_heap = [(-1.0, start)]  # Store negative probability for max heap
    visited = set()
    
    while max_heap:
        prob, node = heapq.heappop(max_heap)
        prob = -prob  # Convert back to positive probability
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == end:
            return prob
        
        for neighbor, edge_prob in graph[node]:
            if neighbor not in visited:
                heapq.heappush(max_heap, (-(prob * edge_prob), neighbor))
    
    return 0.0
