def min_containers(weights, max_capacity):
    weights.sort(reverse=True)
    containers = 0
    current_capacity = 0
    for weight in weights:
        if current_capacity + weight > max_capacity:
            containers += 1
            current_capacity = weight
        else:
            current_capacity += weight

    if current_capacity > 0:
        containers += 1
    return containers
n = 7
weights = [5, 10, 15, 20, 25, 30, 35]
max_capacity = 50
output = min_containers(weights, max_capacity)
print(output) 
