# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print('Drawing started')


class Pen(Stationery):
    def draw(self):
        print('Drawing thin blue line on paper that could not be erased.')


class Pencil(Stationery):
    def draw(self):
        print('Drawing thin black line on paper that could be erased.')


class Handle(Stationery):
    def draw(self):
        print('Drawing thick line on anything that could not ever be erased!')


stationery = Stationery('some_stationery')
stationery.draw()
print('\n')

pen = Pen('blue_pen')
pen.draw()
print('\n')

pencil = Pencil('2b_pencil')
pencil.draw()
print('\n')

handle = Handle('marker')
handle.draw()
print('\n')
