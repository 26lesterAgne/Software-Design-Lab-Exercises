from collections import deque
q = deque()
q.append('angel')
q.append('brandon')
q.append('caroline')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
print("\nQueue after removing elements")
print(q)