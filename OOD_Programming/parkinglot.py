'''
Parking Lot

Piero Orderique

Design a parking lot using OOD principles

I chose to design an apartment parking lot supporting:
    Multiple Levels - multiple rows of spots at each level
        Store what vehicle in parked in what spot
    
User = someone trying to park their vehicle:
    See how many spots are available at each floor
    parkVehicle() at nearest spot available at a certain floor (default = 0)
'''
class ParkingLot():
    '''
    Structures:
        array of Floors with 0 index being main/1st floor
    Methods:
        see_available_count()
        accept_vechicle(vechicle)
    '''

class Floor():
    '''
    Structures:
        array of rows of Spots
    Methods:
        see_available_count()
        accept_vechicle(vechicle)
    '''

class Spot():
    '''
    Structures:
        boolean isAvailable
        Vechicle vehicle (thats parked here)
    Methods:
        is_available(return isAvailable)
        set_vehicle(vehicle)
    '''

class User():
    '''
    Structures:
        string name
        Vehicle vechicleType
        boolean isParked
    Methods:
        is_parked()
    '''

class Vehicle():
    '''
    Structures:
        protected int wheels
        protected double size
    '''

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass