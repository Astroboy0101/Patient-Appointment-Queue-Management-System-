"""
Queue Data Structure Implementation
A simple FIFO (First In First Out) queue for managing patient appointments.
"""

class Queue:
    """
    A basic queue implementation using a list.
    Follows FIFO principle - first patient in is first patient out.
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []
    
    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        
        Args:
            item: The item to add to the queue
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Remove and return the front item from the queue.
        
        Returns:
            The front item, or None if queue is empty
        """
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            True if queue is empty, False otherwise
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get the number of items in the queue.
        
        Returns:
            The size of the queue
        """
        return len(self.items)
    
    def peek(self):
        """
        View the front item without removing it.
        
        Returns:
            The front item, or None if queue is empty
        """
        if self.is_empty():
            return None
        return self.items[0]
    
    def display(self):
        """
        Get all items in the queue (for display purposes).
        
        Returns:
            List of all items in the queue
        """
        return self.items.copy()


