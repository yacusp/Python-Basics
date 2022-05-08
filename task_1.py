# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Date:
    @staticmethod
    def validate(date_tuple):
        long_months = (1, 3, 5, 7, 8, 10, 12)
        short_months = (2, 4, 6, 9, 11)

        if date_tuple[1] > 12:
            print('Invalid value! There is only 12 months!')
            return False

        elif date_tuple[1] < 1:
            print('Month value could not be less than 1!')
            return False

        if date_tuple[0] > 31:
            print('Day value could not be more than 31!')
            return False
        elif date_tuple[0] > 30 and date_tuple[1] in short_months:
            print(f'There is no 31-th in month: {date_tuple[1]}')
            return False
        elif date_tuple[0] == 30 and date_tuple[1] == 2:
            print(f'There is no 30-th of February!')
            return False
        elif date_tuple[0] == 29 and date_tuple[1] == 2 and date_tuple[2] % 4 != 0:
            print(f'It cannot be 29-th February not in leap year!')
            return False

        return True

    @classmethod
    def make_date_int(cls, string_input):
        rus_dict = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
                    'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}
        eng_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'augusta': 8,
                    'september': 9, 'october': 10, 'november': 11, 'december': 12}

        string_input = string_input.lower()
        string_input = string_input.replace('.', ' ')
        string_input = string_input.replace(',', ' ')
        string_input = string_input.replace('-', ' ')
        string_input = string_input.replace('/', ' ')
        date_str_list = string_input.split()

        day = 0
        month = 0
        year = 0

        try:
            day = int(date_str_list[0])
        except ValueError:
            print('Invalid day input')
            return None
        try:
            month = int(date_str_list[1])
        except ValueError:
            try:
                month = rus_dict[date_str_list[1]]
            except KeyError:
                try:
                    month = eng_dict[date_str_list[1]]
                except KeyError:
                    print('Invalid month input')
                    return None
        try:
            year = int(date_str_list[2])
        except ValueError:
            print('Invalid year input')
            return None

        # return tuple((day, month, year))

        final_tuple = tuple((day, month, year))

        if Date.validate(final_tuple):
            return final_tuple
        else:
            print('Date is not valid!')
            return None

    def __init__(self, string_date):
        self.int_date_tuple = Date.make_date_int(string_date)

    def __str__(self):
        if self.int_date_tuple is None:
            return str('There is no valid date!')
        else:
            return str(f'{self.int_date_tuple[0]:02}.{self.int_date_tuple[1]:02}.{self.int_date_tuple[2]:04} ')


date_1 = Date('26.11.1984')
print(date_1)

date_2 = Date('16 Июня 2011')
print(date_2)

date_3 = Date('04/May/1978')
print(date_3)

date_4 = Date('32 Марта 2012')
print(date_4)

date_5 = Date('01 Никогдабря 2027')
print(date_5)

print(Date.validate((26, 11, 1984)))

print(Date.validate((32, 11, 1984)))

print(Date.validate((29, 2, 2000)))

print(Date.validate((29, 2, 2001)))
