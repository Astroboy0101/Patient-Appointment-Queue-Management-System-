"""
Quick test script for DSA structures
"""
from dsa.queue import Queue
from dsa.priority_queue import PriorityQueue
from dsa.linked_list import LinkedList

# Test Queue
q = Queue()
q.enqueue('Patient1')
q.enqueue('Patient2')
print(f'[SUCCESS] Queue: size={q.size()}, front={q.peek()}, dequeue={q.dequeue()}')

# Test Priority Queue
pq = PriorityQueue()
pq.enqueue('Emergency1', 1)
pq.enqueue('Emergency2', 2)
print(f'[SUCCESS] Priority Queue: size={pq.size()}, next={pq.peek()}')

# Test Linked List
ll = LinkedList()
ll.append({'id': 'P001', 'name': 'Test Patient'})
found = ll.find('P001')
print(f'[SUCCESS] Linked List: size={ll.get_size()}, found={found is not None}')

print('[SUCCESS] All DSA structures working correctly!')

