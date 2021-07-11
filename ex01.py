# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
try:
    script_name, hours, salary_per_hour, bonus = argv
    try:
        print(f'Salary: {float(hours) * float(salary_per_hour) + float(bonus)}')
    except ValueError:
        print('Bad argument format')
except ValueError:
    print('Bad arguments count')

