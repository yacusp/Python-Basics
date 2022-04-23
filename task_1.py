# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

import time
import pygame as pg
import sys


class TrafficLight:
    def __init__(self):
        self.__color = 'red'
        self.__timer = 0
        self.__working = False

    def running(self, current_time):

        red_light_delay = 7
        red_with_yellow_delay = 2
        yellow_light_delay = 2
        green_light_delay = 7

        if not self.__working:
            self.__working = True
            self.__timer = current_time

        seconds_past = current_time - self.__timer

        if seconds_past > red_light_delay and self.__color == 'red':
            self.__timer = current_time
            self.__color = 'red and yellow'

        elif seconds_past > red_with_yellow_delay and self.__color == 'red and yellow':
            self.__timer = current_time
            self.__color = 'green'

        elif seconds_past > green_light_delay and self.__color == 'green':
            self.__timer = current_time
            self.__color = 'yellow'

        elif seconds_past > yellow_light_delay and self.__color == 'yellow':
            self.__timer = current_time
            self.__color = 'red'
            self.__working = False

        return self.__color


def make_color_list(color):
    grey = (125, 125, 125)
    red = (225, 50, 50)
    yellow = (225, 225, 0)
    green = (0, 200, 64)

    red_light_red = (red, (75, 75), 50)
    red_light_grey = (grey, (75, 75), 50)
    yellow_light_yellow = (yellow, (75, 200), 50)
    yellow_light_grey = (grey, (75, 200), 50)
    green_light_green = (green, (75, 325), 50)
    green_light_grey = (grey, (75, 325), 50)

    color_set_list = []

    if color == 'red':
        color_set_list = [red_light_red, yellow_light_grey, green_light_grey]
    elif color == 'red and yellow':
        color_set_list = [red_light_red, yellow_light_yellow, green_light_grey]
    elif color == 'yellow':
        color_set_list = [red_light_grey, yellow_light_yellow, green_light_grey]
    elif color == 'green':
        color_set_list = [red_light_grey, yellow_light_grey, green_light_green]

    return color_set_list


traffic_light = TrafficLight()
sc = pg.display.set_mode((150, 400))

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    time.sleep(1)
    print(traffic_light.running(time.time()))
    for el in make_color_list(traffic_light.running(time.time())):
        pg.draw.circle(sc, el[0], el[1], el[2])
    pg.display.update()
