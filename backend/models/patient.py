"""
Patient Model
Represents a patient in the system.
"""

class Patient:
    """Patient model class."""
    
    def __init__(self, id, name, age=None, phone=None, email=None, condition=None, is_emergency=False, priority=5):
        """
        Initialize a patient.
        
        Args:
            id: Unique patient identifier
            name: Patient full name
            age: Patient age (optional)
            phone: Contact phone number (optional)
            email: Contact email (optional)
            condition: Medical condition description (optional)
            is_emergency: True if emergency case
            priority: Priority level (1-5, 1 is highest)
        """
        self.id = id
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email
        self.condition = condition
        self.is_emergency = is_emergency
        self.priority = priority
    
    def to_dict(self):
        """Convert patient to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'phone': self.phone,
            'email': self.email,
            'condition': self.condition,
            'is_emergency': self.is_emergency,
            'priority': self.priority
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create patient from dictionary."""
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            age=data.get('age'),
            phone=data.get('phone'),
            email=data.get('email'),
            condition=data.get('condition'),
            is_emergency=data.get('is_emergency', False),
            priority=data.get('priority', 5)
        )


