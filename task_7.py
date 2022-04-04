# 7. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

progress_km = int(input('Enter first day result: '))
target_km = int(input('Enter your target: '))
days = 1

if progress_km >= target_km:
    print('You are already doing it!')

else:
    while progress_km < target_km:
        days += 1
        progress_km = progress_km + progress_km*0.1
        # print(progress_km)
    print(f'It will take you {days} days!')
