# Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.

def user_data_print(name, sname, year, city, mail, phone):
    print(f'Name: {name} {sname}, year of birth: {year}, city: {city}, e-mail: {mail}, phone number: {phone}')


user_name = input('Enter your name: ')
user_sname = input('Enter your surname: ')
user_year = input('Enter your year of birth: ')
user_city = input('Enter city: ')
user_mail = input('Enter your e-mail: ')
user_phone = input('Enter your phone number: ')

user_data_print(name=user_name, sname=user_sname, year=user_year, city=user_city, mail=user_mail, phone=user_phone)
