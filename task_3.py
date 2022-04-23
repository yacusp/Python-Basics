# 3. Реализовать базовый класс Worker (работник).
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print('Full name is:', self.name, self.surname)

    def get_total_income(self):
        print('Total income is:', self._income['wage'] + self._income['bonus'])


first_person = Position('Ivan', 'Petrov', 1000, 500)

first_person.get_full_name()
first_person.get_total_income()
