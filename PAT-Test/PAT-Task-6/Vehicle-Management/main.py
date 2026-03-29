# -----------------------------
# Base Class
# -----------------------------

class Vehicle:

    def __init__(self, model, rental_rate):                                 # constructor
        self.model = model                                                  # vehicle model name
        self.rental_rate = rental_rate                                      # cost per day
                                          
    def calculate_rental(self, num_days):                                   # method to calculate rental (will be overridden)
        return self.rental_rate * num_days


# -----------------------------
# Car Class
# -----------------------------

class Car(Vehicle):

    def __init__(self, model, rental_rate, seats):                          # constructor
        super().__init__(model, rental_rate)                                # call parent constructor
        self.seats = seats                                                  # number of seats

    def calculate_rental(self, num_days):                                   # override method
        total = self.rental_rate * num_days + 100                           # extra fixed charge
        return total

# -----------------------------
# Ebike Class
# -----------------------------

class Ebike(Vehicle):

  
    def __init__(self, model, rental_rate, helmet_included):                # constructor
        super().__init__(model, rental_rate)                                # call parent constructor
        self.helmet_included = helmet_included                              # True or False

    def calculate_rental(self, num_days):                                   # override method
        total = self.rental_rate * num_days                                 # base cost

        if not self.helmet_included:                                        # discount if helmet not included
            total = total - 100

        return total


# -----------------------------
# Evehicle Class
# -----------------------------

class Evehicle(Vehicle):

   
    def __init__(self, model, rental_rate, load_capacity):                  # constructor
        super().__init__(model, rental_rate)
        self.load_capacity = load_capacity                                  # in tons

    def calculate_rental(self, num_days):                                   # override method
        total = self.rental_rate * num_days + (self.load_capacity * 100)    # extra charge based on load capacity
        return total


# -----------------------------
# Main Program
# -----------------------------

v1 = Car("Hyundai i20", 2000, 5)                                            # create objects
v2 = Ebike("OLA E S1pro", 1000, True)
v3 = Evehicle("Tata PunchEV", 3000, 10)

vehicles = [v1, v2, v3]                                                     # list of vehicles

days = 3                                                                    # rental duration

for v in vehicles:                                                          # loop through all vehicles
    print("Model:", v.model)                                                
    print("Rental: Rs.", v.calculate_rental(days), "/- for", days, "days.") # polymorphism
    print("------")