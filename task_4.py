# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'{self.name} moves with speed: {self.speed} km/h.')

    def stop(self):
        print(f'{self.name} stopped.')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.with_spoiler = True


class TownCar(Car):
    def show_speed(self):
        print(f'Current speed is: {self.speed} km/h.')
        if self.speed > 40:
            print('Speed is over the limit!')


class WorkCar(Car):
    def show_speed(self):
        print(f'Current speed is: {self.speed} km/h.')
        if self.speed > 40:
            print('Speed is over the limit!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


car_1 = Car(50, 'black', 'common_car')

print(car_1.name, car_1.speed)
car_1.go()
car_1.turn('left')
car_1.stop()
print('\n')

racer_1 = SportCar(100, 'red', 'speedster')

print(racer_1.name, racer_1.speed)
racer_1.go()
racer_1.turn('left')
racer_1.stop()
print('\n')

taxi_1 = TownCar(80, 'yellow', 'cab')

print(taxi_1.name, taxi_1.speed)
taxi_1.go()
taxi_1.show_speed()
taxi_1.turn('left')
taxi_1.stop()
print('\n')

tractor_1 = TownCar(30, 'green', 'farmer')

print(tractor_1.name, tractor_1.speed)
tractor_1.go()
tractor_1.show_speed()
tractor_1.turn('left')
tractor_1.stop()
print('\n')

police_1 = PoliceCar(120, 'black and white', 'inspector')
print(police_1.name, police_1.speed, police_1.is_police)
police_1.go()
police_1.turn('left')
police_1.stop()
print('\n')
