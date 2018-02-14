def queue_time(customers, n):
    ListQueue = []
    if n == 0 or len(customers) == 0:
        return 0
    for x in range(n):
        ListQueue.append(0)
    x =0
    for x in range(len(customers)):
        ClientToAllocate = customers[x]
        ListQueue[ListQueue.index(min(ListQueue))] = ListQueue[ListQueue.index(min(ListQueue))]+ClientToAllocate
    return max(ListQueue)

print(queue_time([5,3,4], 1))
queue_time([10,2,3,3], 2)
queue_time([2,3,10], 2)