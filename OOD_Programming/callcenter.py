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
    def __init__(self, *employees) -> None:
        '''creates the call queue and adds employees to it if they are available'''
        self.callqueue = CallQueue()
        for employee in employees:
            if employee.is_available():
                self.callqueue.add_employee(employee=employee)

    def addEmployee(self, employee):
        self.callqueue.add_employee(employee)

from collections import deque
class CallQueue():
    '''
    A queue of respondants , manager, and director queues
    '''
    def __init__(self) -> None:
        # initialize a dequeue for each type 
        self.respondants = deque([])
        self.managers = deque([])
        self.directors = deque([])
        # master array of queues where we check left to right each time
        self.masterqueue = [
            self.respondants,
            self.managers,
            self.directors,
        ]

    def add_employee(self, employee):
        if not employee.is_available(): raise self.EmployeeUnavailableError
        # else, add the employee to the appropriate queue:
        if isinstance(employee, Respondant):
            self.respondants.append(employee)
        elif isinstance(employee, Manager):
            self.managers.append(employee)
        elif isinstance(employee, Director):
            self.directors.append(employee)

    def add_employees(self, *employees):
        for employee in employees:
            self.add_employee(employee)

    def __str__(self) -> str:
        res = ""
        for queue in self.masterqueue:
            for employee in queue:
                res+= employee.type + " " + employee.name + " ==> "
        return res + "END"

    class EmployeeUnavailableError(Exception):
        pass

class Employee():
    def __init__(self, name) -> None:
        self.name = name
        self.available = True
        self.type = "General Employee"

    def receive_call(self) -> None:
        self.available = False

    def is_available(self) -> bool:
        return self.available

    def set_availability(self, available) -> None:
        self.available = available
         
    def __str__(self) -> str:
        return self.type + " " + self.name + " available: " + str(self.available)

class Respondant(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Respondant"
         
    def __str__(self) -> str:
        return super().__str__()

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Manager"
         
    def __str__(self) -> str:
        return super().__str__()

class Director(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Director"
         
    def __str__(self) -> str:
        return super().__str__()


if __name__ == "__main__":
    r1 = Respondant("Adam")
    r2 = Respondant("Bill")
    r3 = Respondant("Cameron")
    m1 = Manager("Piero")
    d1 = Director("Jorge")
    daCrew = [r1, r2, r3, m1, d1]
    for r in daCrew:
        print(r)

    myQueue = CallQueue()
    myQueue.add_employees(*daCrew)
    print(myQueue)