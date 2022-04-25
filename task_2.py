# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calculate_fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, title, size):
        self.title = title
        self.v = size

    @property
    def calculate_fabric(self):
        return self.v/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, title, height):
        self.title = title
        self.h = height

    @property
    def calculate_fabric(self):
        return self.h*2 + 0.3


coat_1 = Coat('Black_coat', 52)

print(coat_1.calculate_fabric)

tuxedo_1 = Suit('Fantastic_suit', 185)

print(tuxedo_1.calculate_fabric)

# Результаты расчетов меня смущают.