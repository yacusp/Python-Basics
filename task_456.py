# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
# оргтехники на склад и передачу в определённое подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from abc import abstractmethod


class Depot:
    total_equipment_counter = 0

    def __init__(self, name):
        self.name = name
        self.equipment_dict = dict()

    @classmethod
    def count_all_equipment(cls):
        print(f'Total amount of equipment in all depots is: {cls.total_equipment_counter}')

    @staticmethod
    def repair(element):
        if not isinstance(element, list):
            element = [element]
        for el in element:
            el.repair()
        print('Everything repaired!')

    def __str__(self):
        result_string = str(f'{self.name} status is:\n')
        for key in self.equipment_dict:
            result_string += str(f'{key}:\n')
            result_string += ' On duty:\n'
            for el in self.equipment_dict[key]:
                if el.on_duty_status:
                    result_string += str(el)
            result_string += '\n'

            result_string += str(' Stored:\n')
            for el in self.equipment_dict[key]:
                if el.storing_status:
                    result_string += str(el)
            result_string += '\n'
        return result_string

    def register_new_equipment(self, input_list):
        if not isinstance(input_list, list):
            input_list = [input_list]
        for eq in input_list:
            if eq.equipment_type in self.equipment_dict:
                local_list = self.equipment_dict.pop(eq.equipment_type)
                if eq not in local_list:
                    local_list.append(eq)
                    eq.store()
                    Depot.total_equipment_counter += 1
                else:
                    print(f'{eq.name} was already registered in {self.name} before!')
                self.equipment_dict[eq.equipment_type] = local_list
            else:
                self.equipment_dict[eq.equipment_type] = list([eq])
                eq.store()
                Depot.total_equipment_counter += 1

    def store_equipment(self, input_list):
        if not isinstance(input_list, list):
            input_list = [input_list]
        for eq in input_list:
            if eq.equipment_type in self.equipment_dict:
                local_list = self.equipment_dict.pop(eq.equipment_type)
                if eq in local_list:
                    eq.store()
                    print(f'{eq.name} is stored now!')
                else:
                    print(f'There is no {eq.name} registered in {self.name}!')
                self.equipment_dict[eq.equipment_type] = local_list
            else:
                print(f'There is no {eq.equipment_type} category registered in {self.name}!')

    def release_equipment(self, input_list):
        if not isinstance(input_list, list):
            input_list = [input_list]
        for eq in input_list:
            if eq.equipment_type in self.equipment_dict:
                local_list = self.equipment_dict.pop(eq.equipment_type)
                if eq in local_list:
                    if not eq.broken_status:
                        eq.release()
                        print(f'{eq.name} is on duty now!')
                    else:
                        print(f'{eq.name} was not released. It is broken!')
                else:
                    print(f'There is no {eq.name} registered in {self.name}!')
                self.equipment_dict[eq.equipment_type] = local_list
            else:
                print(f'There is no {eq.equipment_type} category registered in {self.name}!')

    def repair_stored_equipment(self):
        equip_counter = 0
        for key in self.equipment_dict:
            for el in self.equipment_dict[key]:
                if el.storing_status and el.broken_status:
                    el.repair()
                    equip_counter += 1
        print('All broken equipment at store fixed!')
        print(f'Total units repaired: {equip_counter}.')

    def run_equipment_on_duty(self, times=1):
        work_counter = 0
        for i in range(0, times):
            for key in self.equipment_dict:
                for el in self.equipment_dict[key]:
                    if el.on_duty_status and not el.broken_status:
                        el.work()
                        work_counter += 1

        print('All equipment on duty worked!')
        print(f'Total units run: {work_counter}.')

    def remove_equipment(self, input_list):
        if not isinstance(input_list, list):
            input_list = [input_list]
        for eq in input_list:
            if eq.equipment_type in self.equipment_dict:
                local_list = self.equipment_dict.pop(eq.equipment_type)
                if eq in local_list:
                    local_list.remove(eq)
                    eq.on_duty_status = False
                    eq.storing_status = False
                    Depot.total_equipment_counter -= 1
                    print(f'{eq.name} was removed from {self.name}')
                else:
                    print(f'There is no {eq.name} registered in {self.name}!')
                if len(local_list) > 0:
                    self.equipment_dict[eq.equipment_type] = local_list
            else:
                print(f'There is no {eq.equipment_type} category registered in {self.name}!')


class OfficeEquipment:
    def __init__(self, name, color='white'):
        self.name = name
        self.color = color
        self.on_duty_status = False
        self.storing_status = False
        self.broken_status = False

    def __str__(self):
        if self.broken_status:
            return str(f'  {self.name}, color: {self.color}, condition: broken.\n')
        else:
            return str(f'  {self.name}, color: {self.color}.\n')

    @abstractmethod
    def work(self):
        pass

    def store(self):
        self.on_duty_status = False
        self.storing_status = True

    def release(self):
        self.on_duty_status = True
        self.storing_status = False

    @abstractmethod
    def repair(self):
        pass


class Printers(OfficeEquipment):
    equipment_type = 'Printers'
    working_points = 5

    def __init__(self, name, color='white', technology='jet'):
        super().__init__(name, color)
        self.name = name
        self.color = color
        self.technology = technology
        self.work_limit = Printers.working_points

    def work(self):
        if not self.broken_status:
            print(f'{self.name}: Bz-bz-bz...')
            self.work_limit -= 1
            if self.work_limit <= 0:
                self.broken_status = True
        else:
            print(f'Printer {self.name} does not work!')

    def repair(self):
        self.work_limit = Printers.working_points
        self.broken_status = False


class Scanners(OfficeEquipment):
    equipment_type = 'Scanners'
    working_points = 3

    def __init__(self, name, color='black', resolution='600dpi'):
        super().__init__(self, name)
        self.name = name
        self.color = color
        self.resolution = resolution
        self.work_limit = Scanners.working_points

    def work(self):
        if not self.broken_status:
            print(f'{self.name}: U-u-u...')
            self.work_limit -= 1
            if self.work_limit <= 0:
                self.broken_status = True
        else:
            print(f'Scanner {self.name} does not work!')

    def repair(self):
        self.work_limit = Scanners.working_points
        self.broken_status = False


class Copiers(OfficeEquipment):
    equipment_type = 'Copiers'
    working_points = 7

    def __init__(self, name, color='black', copy_seed='1000spm'):
        super().__init__(self, name)
        self.name = name
        self.color = color
        self.resolution = copy_seed
        self.work_limit = Copiers.working_points

    def work(self):

        if not self.broken_status:
            print(f'{self.name}: Ubz-ubz-ubz...')
            self.work_limit -= 1
            if self.work_limit <= 0:
                self.broken_status = True
        else:
            print(f'Scanner {self.name} does not work!')

    def repair(self):
        self.work_limit = Copiers.working_points
        self.broken_status = False


depot_1 = Depot('depot_1')

printer_1 = Printers('printer_1')
printer_2 = Printers('printer_2')
printer_3 = Printers('printer_3')
printer_4 = Printers('printer_4', 'black')
printer_5 = Printers('printer_5', 'white', 'laser')

for n in range(0, 5):
    printer_1.work()
print('')
for n in range(0, 3):
    printer_3.work()
print('')
scanner_1 = Scanners('scanner_1')
scanner_2 = Scanners('scanner_2')
scanner_3 = Scanners('scanner_3')
scanner_4 = Scanners('scanner_4')
scanner_5 = Scanners('scanner_5')

for n in range(0, 5):
    scanner_2.work()
print('')
for n in range(0, 2):
    scanner_3.work()
print('')
copier_1 = Copiers('copier_1')
copier_2 = Copiers('copier_2')
copier_3 = Copiers('copier_3')
copier_4 = Copiers('copier_4')
copier_5 = Copiers('copier_5')

for n in range(0, 5):
    copier_2.work()
print('')
for n in range(0, 3):
    copier_3.work()
print('')
my_list = [printer_1, printer_2, printer_3, printer_4]
my_list.extend([scanner_1, scanner_2, scanner_3, scanner_4])
my_list.extend([copier_1, copier_2, copier_3, copier_4])

depot_1.register_new_equipment(my_list)

Depot.count_all_equipment()
print('Check 1')

print(depot_1)

depot_1.register_new_equipment([printer_5, scanner_5])
depot_1.register_new_equipment(copier_5)
print('Check 2')
print(depot_1)

depot_1.release_equipment([printer_1, printer_2, printer_3])
depot_1.release_equipment([scanner_1, scanner_2, scanner_3])
depot_1.release_equipment([copier_1, copier_2, copier_3])
print('Check 3')
print(depot_1)

depot_1.run_equipment_on_duty(3)
print('Check 4')
print(depot_1)

depot_1.store_equipment([printer_1, scanner_1, copier_1])
print('Check 5')
print(depot_1)

depot_1.repair_stored_equipment()
print('Check 6')
print(depot_1)

depot_1.remove_equipment([printer_2, scanner_1])
depot_1.remove_equipment(copier_5)
print('Check 7')
print(depot_1)

depot_1.remove_equipment([scanner_1, scanner_2, scanner_3, scanner_4, scanner_5])
print('Check 8')
print(depot_1)
