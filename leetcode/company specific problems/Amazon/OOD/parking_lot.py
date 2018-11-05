#Parking lot slots
#number of slots
#how many vehicles are in parking lot
#how many slots are available, in each level
#is parking lot full
#bike slots, car , truck slot
#each slot has one vehicile
#price of all vehicles 10
#how many levels in parking lot 


#classes

class ParkingLot(object):
    def __init__(self):
        self.number_levels = number_levels
        self.number_slot_each_level = num_slots
        self.price_car = 10
        self.price_truck = 15
        self.price_motorbike = 8
        self.parking_spots_available = []


    def park_vehicle(self):
        # Assign level and parking spot
        # Updating particular slot and particular level
      

    def pay(self, type_vehicle, dollar):
        if type_vehicle == 0:
            return dollar - self.price_truck:

        elif vehicle_type == 1:
            return dollar - self.price_car
        else:
            return dollar - self.price_motorbike
  


class Level(object):
    def __init__(self, level_id, number_levels, number_slots, number_slots_available):
        self.level_id = level_id
        Self.car_slot_occupied = car_slot_occupied
        Self.bike_slot_occupied = bike_slot_occupied
        Self.truck_slot_occupied = truck_slot_occupied
        Self.car_slot_available = .car_slot_available 
        Self.truck_slot_available = truck_slot_available
        Self.bike_slot_available = bike_slot_available




class Slot(object):
    def __init__(self, level_id, total_number_slots, slot_id, slot_type_number):
        self.level = level_id
        self.slot_id = slot_id
        self.slot_type = Vehicle.vehicle_type_lst[self.slot_type_number]
        self.vehicle_id = vehicle_id
        self.is_slot_available = True 
        self.time_entered
        self.time_left



class Vehicle(object):
    def __init__(self, vehicle_id, vehicle_type, license_plate_number, name):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate_number
        self.owner_name = name



    vehicle_type_lst = ['Truck', 'Car', 'Motorbike']


    def where_to_park(self):
        return slot number and level



