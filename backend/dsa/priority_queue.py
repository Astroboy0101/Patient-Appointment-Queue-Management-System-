"""
Priority Queue Data Structure Implementation
Used for handling emergency patients - higher priority patients are served first.
"""

class PriorityQueue:
    """
    A priority queue implementation for emergency cases.
    Lower priority number = higher priority (1 is highest, 5 is lowest).
    """
    
    def __init__(self):
        """Initialize an empty priority queue."""
        self.items = []
    
    def enqueue(self, item, priority):
        """
        Add an item with a priority to the queue.
        Items are automatically sorted by priority.
        
        Args:
            item: The item to add (e.g., patient data)
            priority: Priority level (1 = highest, 5 = lowest)
        """
        entry = {'item': item, 'priority': priority}
        self.items.append(entry)
        # Sort by priority (lower number = higher priority)
        self.items.sort(key=lambda x: x['priority'])
    
    def dequeue(self):
        """
        Remove and return the highest priority item.
        
        Returns:
            The highest priority item, or None if queue is empty
        """
        if self.is_empty():
            return None
        return self.items.pop(0)['item']
    
    def is_empty(self):
        """
        Check if the priority queue is empty.
        
        Returns:
            True if empty, False otherwise
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get the number of items in the priority queue.
        
        Returns:
            The size of the queue
        """
        return len(self.items)
    
    def peek(self):
        """
        View the highest priority item without removing it.
        
        Returns:
            The highest priority item, or None if queue is empty
        """
        if self.is_empty():
            return None
        return self.items[0]['item']
    
    def display(self):
        """
        Get all items in priority order (for display purposes).
        
        Returns:
            List of all items sorted by priority
        """
        return [entry['item'] for entry in self.items]


