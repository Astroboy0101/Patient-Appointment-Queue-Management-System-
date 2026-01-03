"""
Doctor Model
Represents a doctor in the system.
"""

class Doctor:
    """Doctor model class."""
    
    def __init__(self, id, name, specialization=None, available=True):
        """
        Initialize a doctor.
        
        Args:
            id: Unique doctor identifier
            name: Doctor full name
            specialization: Medical specialization (optional)
            available: Whether doctor is currently available
        """
        self.id = id
        self.name = name
        self.specialization = specialization
        self.available = available
    
    def to_dict(self):
        """Convert doctor to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'specialization': self.specialization,
            'available': self.available
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create doctor from dictionary."""
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            specialization=data.get('specialization'),
            available=data.get('available', True)
        )


