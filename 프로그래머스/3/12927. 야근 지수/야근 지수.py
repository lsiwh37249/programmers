import heapq

def solution(n, works):
    
    heap = [-w for w in works]
    heapq.heapify(heap)  

    for _ in range(n):
        largest = heapq.heappop(heap) 
        if largest == 0:  
            break
        largest += 1  
        heapq.heappush(heap, largest)

    return sum((w ** 2) for w in heap)