'''
Call Center

Piero Orderique
23 Jan 2021

3 levels of employee: respondent, manager, and director
An incoming call must be allocated to a free respondent. 
    if none are available to take the call, it goes to a manager
    if the manager is not available, it goes to director
    (if director unavailable, we lose the call or can add to a waitlist!)

Design the classes and ADT for this problem. 
Implement a method called dispatchCall() which assigns a call to the first available employee
'''
from collections import deque

class CallCenter():
    '''
    Creates a call center

    Needs a list of respondants, a manager, and a director to function properly
    '''
    def __init__(self, *employees) -> None:
        '''creates the call queue and adds employees to it if they are available'''
        self.all_employees = []
        self.callqueue = CallQueue()
        for employee in employees:
            self.all_employees.append(employee)
            if employee.is_available():
                self.callqueue.add_employee(employee=employee)

    def add_employee(self, employee):
        if employee.is_available():
            self.all_employees.append(employee)
            self.callqueue.add_employee(employee)

    def add_employees(self, *employees):
        for employee in employees:
            if employee.is_available():
                self.all_employees.append(employee)
                self.callqueue.add_employee(employee=employee)

    def dispatchCall(self, call):
        ''' assign a call to first available employee '''
        employee = self.callqueue.pop_employee()
        employee.call = call
        return employee

    def __str__(self) -> str:
        rep = ""
        for employee in self.all_employees:
            if employee.call:
                rep += employee.name + " on call " + str(employee.call.id) + "\n"
            else:
                rep += str(employee) + "\n"
        return rep

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

    def pop_employee(self):
        '''iterate trough master queue and pop first one we can'''
        for queue in self.masterqueue:
            if len(queue):
                # pop from queue if its not empty
                employee = queue.popleft()
                employee.set_availability(False)
                return employee
        # else all are empty so raise error
        raise self.EmployeeUnavailableError("Queue is empty")

    def employee_available(self):
        ''' like isNotEmpty method '''
        # there will always be an employee available so long as there is a director available
        return bool(len(self.directors))

    def __str__(self) -> str:
        res = ""
        for queue in self.masterqueue:
            for employee in queue:
                res+= employee.type + " " + employee.name + " ==> "
        return res + "END"

    class EmployeeUnavailableError(Exception):
        pass

class Call():
    def __init__(self, id) -> None:
        self.id = id

    def __str__(self) -> str:
        return "CALLER ID: " + str(self.id)

class Employee():
    def __init__(self, name) -> None:
        self.name = name
        self.available = True
        self.type = "General Employee"
        self.call = None

    def receive_call(self, call:Call) -> None:
        self.available = False
        self.call = call

    def is_available(self) -> bool:
        return self.available

    def set_availability(self, available) -> None:
        self.available = available
        if available:
            self.call = None
         
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
    # for r in daCrew:
    #     print(r)
    # myQueue = CallQueue()
    # myQueue.add_employees(*daCrew)
    # print(myQueue.pop_employee())
    # print(myQueue.pop_employee())
    # print(myQueue.pop_employee())
    # print(myQueue.pop_employee())
    # print(myQueue.pop_employee())

    # final testing
    ebay_customer_services = CallCenter()
    ebay_customer_services.add_employees(*daCrew)
    print(ebay_customer_services)
    # assign calls in order
    ebay_customer_services.dispatchCall(Call(7066077066))
    ebay_customer_services.dispatchCall(Call(6789998212)) 
    ebay_customer_services.dispatchCall(Call(1118675309))
    print(ebay_customer_services)
    ebay_customer_services.dispatchCall(Call(1800588267))
    ebay_customer_services.dispatchCall(Call(4044044044))
    print(ebay_customer_services)