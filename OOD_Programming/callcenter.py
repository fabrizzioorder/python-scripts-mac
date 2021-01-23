'''
Call Center

3 levels of employee: respondent, manager, and director
An incoming call must be allocated to a free respondent. 
    if none are available to take the call, it goes to a manager
    if the manager is not available, it goes to director
    (if director unavailable, we lose the call or can add to a waitlist!)

Design the classes and ADT for this problem. 
Implement a method called dispatchCall() which assigns a call to the first available employee
'''
from abc import ABC, abstractmethod

class CallCenter():
    '''
    Creates a call center

    Needs a list of respondants, a manager, and a director to function properly
    '''
    def __init__(self) -> None:
        # individual queue for each employee type
        self.callqueue = CallQueue()

    def addEmployee(self, employee):
        self.callqueue.add_employee(employee)


class CallQueue():
    '''
    A queue of respondants list, manager, and director
    '''
    def __init__(self) -> None:
        repondants = []

    def add_employee(self, employee):
        pass

class Employee(ABC):
    def __init__(self, name) -> None:
        self.name = name
        self.available = True
    def __str__(self) -> str:
        return self.name + " available: " + str(self.available)
    @abstractmethod
    def receive_call(self) -> None:
        pass
    @abstractmethod
    def is_available(self) -> bool:
        pass
    @abstractmethod
    def set_availability(self, available) -> None:
        pass

class Respondant(Employee):
    def __init__(self, name):
        super().__init__(name)

    def receive_call(self) -> None:
        self.available = False

    def is_available(self) -> bool:
        return self.available

    def set_availability(self, available) -> None:
        self.available = available
         
    def __str__(self) -> str:
        return "Respondant " + super().__str__()

# def Manager(Employee):
#     pass

# def Director(Employee):
#     pass

p1 = Respondant("Bill")
print(p1)