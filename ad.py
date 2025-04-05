import re

def is_valid_date(date_str):
    # Проверяем формат с помощью регулярного выражения
    if not re.fullmatch(r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})$', date_str):
        return False

    day, month, year = map(int, date_str.split('.'))
    
    # Проверка количества дней в месяце
    if month == 2:  # Февраль
        if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
            max_days = 29  # Високосный год
        else:
            max_days = 28  # Не високосный
    elif month in [4, 6, 9, 11]:
        max_days = 30  # Апрель, июнь, сентябрь, ноябрь
    else:
        max_days = 31  # Остальные месяцы
    
    return 1 <= day <= max_days
