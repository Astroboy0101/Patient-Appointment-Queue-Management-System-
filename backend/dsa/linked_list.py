"""
Linked List Data Structure Implementation
Used for dynamic patient record management.
"""

class Node:
    """A node in the linked list containing patient data."""
    
    def __init__(self, data):
        """
        Initialize a node with data.
        
        Args:
            data: The patient data to store
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list implementation for patient records.
    Allows dynamic addition and removal of patient records.
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.size = 0
    
    def append(self, data):
        """
        Add a new patient record to the end of the list.
        
        Args:
            data: Patient data to add
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, data):
        """
        Add a new patient record to the beginning of the list.
        
        Args:
            data: Patient data to add
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def remove(self, patient_id):
        """
        Remove a patient record by ID.
        
        Args:
            patient_id: The ID of the patient to remove
            
        Returns:
            True if patient was found and removed, False otherwise
        """
        if self.head is None:
            return False
        
        # If head node needs to be removed
        if self.head.data.get('id') == patient_id:
            self.head = self.head.next
            self.size -= 1
            return True
        
        # Search for the node to remove
        current = self.head
        while current.next is not None:
            if current.next.data.get('id') == patient_id:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def find(self, patient_id):
        """
        Find a patient record by ID.
        
        Args:
            patient_id: The ID of the patient to find
            
        Returns:
            Patient data if found, None otherwise
        """
        current = self.head
        while current is not None:
            if current.data.get('id') == patient_id:
                return current.data
            current = current.next
        return None
    
    def display(self):
        """
        Get all patient records as a list.
        
        Returns:
            List of all patient data
        """
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result
    
    def is_empty(self):
        """
        Check if the linked list is empty.
        
        Returns:
            True if empty, False otherwise
        """
        return self.head is None
    
    def get_size(self):
        """
        Get the number of patient records in the list.
        
        Returns:
            The size of the list
        """
        return self.size


