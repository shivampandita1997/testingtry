
from car import Car

import pytest



def test_car_brake():
    car = Car(50)
    car.brake()
    assert car.speed == 45