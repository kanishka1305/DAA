import heapq

def kClosest(points, k):
    return heapq.nsmallest(k, points, lambda x: x[0]**2 + x[1]**2)
