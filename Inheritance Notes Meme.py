class Vehicle(object):
    def __init__(self, source, material, seat, speed, passengers):
        self.power_source = source
        self.material = material
        self.seat_location = seat
        self.max_speed = speed
        self.passengers = passengers

    def move(self):
        print('You move forward')

    def change_direction(self):
        print('You change directions')


class Car(Vehicle):
    def __init__(self, material, seat, speed, passengers, windows):
        super(Car, self).__init__('engine', material, seat, speed, passengers)
        self.windows = windows

    def roll_down_windows(self):
        print("You roll down the windows")

    def turn_on(self):
        print("You turn the key and the engine starts")


test_car = Car('Aluminium', 'Driver Side', 140, 2, True)
test_car.change_direction()


class KeylessCar(Car):
    def __init__(self, material, seat, speed, passengers, windows):
        super(KeylessCar, self).__init__(material, seat, speed, passengers, windows)

    def turn_on(self):
        print('You push the button and the car turns on')


test_car.turn_on()
cool_car = KeylessCar('Aluminium', 'Driver Side', 140, 2, True)
cool_car.turn_on()


class Tesla(Car):
    def __init__(self, material, seat, speed, passengers, windows):
        super(Tesla, self).__init__(material, seat, speed, passengers, windows)

    def fly(self):
        print('You launch the car into low earth orbit')
