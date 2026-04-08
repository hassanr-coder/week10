'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 10 Assignment 1
'''


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        return f"Car Brand: {self.brand}, Top Speed: {self.speed} mph"
    
    @staticmethod
    def create_car(brand, speed):
        try:
            speed = float(speed)
            if speed <= 0:
                raise ValueError("Top speed must be greater than 0.")
            return Car(brand, speed)
        except ValueError as e:
            print(f"Could not create car: {e}")
            return None


def show_car_details(car):
    try:
        if not isinstance(car, Car):
            raise TypeError("No valid car object provided.")
        print(car.display_info())
    except TypeError as e:
        print(f"Error showing car details: {e}")


def run_demo():
    try:
        print("---Testing Valid Car---")
        car = Car.create_car("Toyota", 120)
        show_car_details(car)

        print("\n---Testing Invalid Car---")
        bad_car = Car.create_car("Honda", -50)
        show_car_details(bad_car)
    except Exception as e:
        print(f"Unexpected error in car demo: {e}")


if __name__ == "__main__":
    run_demo()