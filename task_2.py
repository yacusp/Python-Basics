# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

        self.__thickness = 5  # cm
        self.__weight_per_square = 25  # kg per 1 square meter with 1 cm thickness

    def calculate_asphalt_wight_kg(self):
        return self._length * self._width * self.__thickness * self.__weight_per_square


my_road = Road(5000, 20)

print('Asphalt wight is:', my_road.calculate_asphalt_wight_kg() / 1000, 'tons.')
