"""
Greedy Scheduling Algorithm Implementation
Assigns patients to doctors efficiently using a greedy approach.
"""

from .queue import Queue
from .priority_queue import PriorityQueue


class Scheduler:
    """
    Greedy scheduling algorithm for assigning patients to doctors.
    
    Greedy Strategy:
    1. Always assign the highest priority patient first (emergency cases)
    2. Assign to the doctor with the least current workload
    3. This ensures urgent cases are handled quickly and workload is balanced
    """
    
    def __init__(self, doctors):
        """
        Initialize the scheduler with available doctors.
        
        Args:
            doctors: List of doctor objects with their availability
        """
        self.doctors = doctors
        self.regular_queue = Queue()
        self.emergency_queue = PriorityQueue()
        self.assignments = {}  # Track doctor-patient assignments
    
    def add_patient(self, patient, is_emergency=False, priority=5):
        """
        Add a patient to the appropriate queue.
        
        Args:
            patient: Patient data dictionary
            is_emergency: True if emergency case, False otherwise
            priority: Priority level (1-5, 1 is highest) for emergencies
        """
        if is_emergency:
            self.emergency_queue.enqueue(patient, priority)
        else:
            self.regular_queue.enqueue(patient)
    
    def assign_patients(self):
        """
        Greedy algorithm to assign patients to doctors.
        
        Algorithm Steps:
        1. First, assign all emergency patients (highest priority first)
        2. Then, assign regular patients
        3. For each patient, choose the doctor with minimum current workload
        
        Returns:
            Dictionary of doctor-patient assignments
        """
        assignments = {}
        
        # Initialize doctor workload tracking
        doctor_workload = {doc['id']: 0 for doc in self.doctors}
        
        # Step 1: Assign emergency patients first (greedy: always handle urgent cases first)
        while not self.emergency_queue.is_empty():
            patient = self.emergency_queue.dequeue()
            # Greedy choice: assign to doctor with least workload
            best_doctor = min(doctor_workload.items(), key=lambda x: x[1])[0]
            if best_doctor not in assignments:
                assignments[best_doctor] = []
            assignments[best_doctor].append(patient)
            doctor_workload[best_doctor] += 1
        
        # Step 2: Assign regular patients (greedy: balance workload)
        while not self.regular_queue.is_empty():
            patient = self.regular_queue.dequeue()
            # Greedy choice: assign to doctor with least workload
            best_doctor = min(doctor_workload.items(), key=lambda x: x[1])[0]
            if best_doctor not in assignments:
                assignments[best_doctor] = []
            assignments[best_doctor].append(patient)
            doctor_workload[best_doctor] += 1
        
        self.assignments = assignments
        return assignments
    
    def get_queue_status(self):
        """
        Get current status of both queues.
        
        Returns:
            Dictionary with queue sizes and next patients
        """
        return {
            'regular_queue_size': self.regular_queue.size(),
            'emergency_queue_size': self.emergency_queue.size(),
            'next_regular': self.regular_queue.peek(),
            'next_emergency': self.emergency_queue.peek()
        }


