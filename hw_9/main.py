import time

# 1
# class TrafficLight:
#     __color = 'red'
#
#     def running(self, __color='red'):
#         print(__color)
#         time.sleep(7)
#         __color = 'yellow'
#         print(__color)
#         time.sleep(2)
#         __color = 'green'
#         print(__color)
#         time.sleep(7)
#         __color = 'red'
#
# test_trafficlight = TrafficLight()
# test_trafficlight.running()

# 2

# class Road:
#
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def material_counter(self, material_per_cm, depth):
#         return self._length * self._width * material_per_cm * depth
#
#
# test_road = Road(20, 5000)
# print(test_road.material_counter(25, 5))

# 3
# class Worker:
#     def __init__(self):
#         self.name = ''
#         self.surname = ''
#         self.position = ''
#         self._income = {'wage': 1000, 'bonus': 2000}
#
#     def set_income(self, wage, bonus):
#         self._income['wage'] = wage
#         self._income['bonus'] = bonus
#
#
# class Position(Worker):
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def get_total_income(self):
#         return self._income['wage'] + self._income['bonus']
#
#
# w = Position()
# w.set_income(10000, 2000)
# w.name = 'Andrew'
# w.surname = 'Johnes'
#
# print(w.get_total_income())
# print(w.get_full_name())
#
#
# wa = Position()
# wa.set_income(25000, 700)
# wa.name = 'Boris'
# wa.surname = 'Smith'
#
# print(wa.get_total_income())
# print(wa.get_full_name())

# 4

# class Car:
#     def __init__(self):
#         self.speed = 0
#         self.color = 0
#         self.name = 0
#         self.is_police = False
#
#     def go(self):
#         print('Машина поехала')
#
#     def stop(self):
#         print('Машина остановилась')
#
#     def turn(self, direction):
#         if direction.lower() == 'налево' or direction.lower() == 'направо':
#             print(f'Машина повернула {direction.lower()}')
#         else:
#             print('Некорректно введено направление поворота')
#
#     def show_speed(self):
#         print(f'Скорость автомобиля равна {self.speed}')
#
#
# class TownCar(Car):
#     def __init__(self):
#         self.is_police = False
#     def show_speed(self):
#         if self.speed > 60:
#             print(f'Скорость автомобиля равна {self.speed}, вы превышаете скорость!')
#         else:
#             print(f'Скорость автомобиля равна {self.speed}')
#
# class SportCar(Car):
#
#     def __init__(self):
#         self.is_police = False
#
# class WorkCar(Car):
#
#     def __init__(self):
#         self.is_police = False
#
#     def show_speed(self):
#         if self.speed > 40:
#             print(f'Скорость автомобиля равна {self.speed}, вы превышаете скорость!')
#         else:
#             print(f'Скорость автомобиля равна {self.speed}')
#
# class PoliceCar(Car):
#
#     def __init__(self):
#         self.is_police = True
#
#
# test_towncar = TownCar()
# test_towncar.speed = 61
# test_towncar.show_speed()
# test_towncar.go()
# test_towncar.turn('Налево')
#
#
# test_sportcar = SportCar()
# test_sportcar.speed = 90
# test_sportcar.show_speed()
#
# test_workcar = WorkCar()
# test_workcar.speed = 43
# test_workcar.show_speed()
#
# test_policecar = PoliceCar()
# print(test_policecar.is_police)

# # 5
# class Stationary:
#     def __init__(self):
#         self.title = ''
#
#     def draw(self):
#         print('Запуск отрисовки')
#
# class Pen(Stationary):
#
#     def draw(self):
#         print('Запуск отрисовки ручкой')
#
#
# class Pencil(Stationary):
#
#     def draw(self):
#         print('Запуск отрисовки карандашом')
#
#
# class Handle(Stationary):
#
#     def draw(self):
#         print('Запуск отрисовки маркером')
#
# test_pen = Pen()
# test_pen.draw()
#
# test_pencil = Pencil()
# test_pencil.draw()
#
# test_handle = Handle()
# test_handle.draw()