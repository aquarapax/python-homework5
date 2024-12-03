# -----Задача №1 Создать программу, которая работает со списком-----

def is_number(value): # Функция для проверки, является ли значение числом.
    try:
        float(value)  # Попробуем преобразовать значение в float
        return True   # Если успешно, возвращаем True
    except ValueError:
        return False  # Если возникает ошибка, возвращаем False

def func(): # функция проверки и сортировки
    user_input = input("Введите элементы через пробел: ") # ввод списка пользователем
    elements = user_input.split()  # Преобразование введенной строки в список
    # Проверяем, содержит ли список хотя бы одно положительное число с использованием any
    # используем функцию is_number для отсеивания нечисловых значений
    has_positive = any(float(x) > 0 for x in elements if is_number(x))
    if has_positive:
        print("Список содержит хотя бы одно положительное число.")
    else:
        print("В списке нет положительных чисел.")

    # Проверяем на наличие в списке нечисловых элементов с помощью all
    all_numbers = all(is_number(x) for x in elements)
    if all_numbers:
        print("Все элементы списка являются числами.")
    else:
        print("В списке есть нечисловые элементы.")

    numeric_elements = (float(x) for x in elements if is_number(x)) # создаем генератор, не числовые элементы отсеиваем с помощью is_number
    sorted_numbers = sorted(numeric_elements)# Сортируем  c помощью sorted
    print("Отсортированный список чисел:", sorted_numbers)

func() # вызываем функцию

# -----Задача №2 Написать класс CyclicIterator-----
class CyclicIterator:
    def __init__(self, iterable): # инициализация класса
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iterable:  # Проверяем, является ли итерируемый объект пустым
            raise StopIteration  # Если пусто, вызываем исключение
        value = self.iterable[self.index]  # Получаем текущий элемент
        self.index = (self.index + 1) % len(self.iterable)  # присваиваем индекс для следующего вызова next, при достижении len, index сбрасывается на 0
        return value  # Возвращаем текущий элемент

# Проберка класса CyclicIterator
items  = range(5) # range для тестирования
cyclic_iterator = CyclicIterator(items)

for i in range(12):  # 12 итераций для демонстрации цикличности
    print(f'{i} - {next(cyclic_iterator)}')
    
# ----- Задача №3 Задайте функцию-генератор для генерации паролей -----

import random # random для случайного выбора символов
from string import ascii_lowercase, ascii_uppercase # Строки с наборами ascii для источника симоволов пароля
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*" # Формируем строку с символами для пароля

def password_generator(length=12): # Добавим параметр для регулирования длинны пароля, по умолчанию 12
  
    while True:  # Бесконечный цикл, чтобы генерировать пароли "бесконечно"
        password = '' # Переменная для хранения пароля
        for i in range(length): # Цикл от 0 до length-1
            t = random.choice(chars) # Выбираем случайный символ из chars
            password = password + t # Склеиваем символ с паролем
        yield password  # Возвращаем сгенерированный пароль с помощью yield

# Создаем экземпляр генератора
gen = password_generator()

# Генерируем и выводим 5 паролей
for i in range(5):
    print(next(gen)) # Используем next для получения следующего сгенерированного значения

# ----- Задача №4 Создать класс Movie -----

from datetime import datetime, timedelta

class Movie:
    def __init__(self, title, schedule_periods):
        self.title = title
        self.schedule_periods = schedule_periods

    def schedule(self): # Генератор который возвращает даты показа фильмов
        for start_date, end_date in self.schedule_periods: # Цикл по периуду
            current_date = start_date # Начинаем с первой даты
            while current_date <= end_date: # Цикл до тех пор пока не достигнем end_date
                yield current_date # возвращаем дату
                current_date += timedelta(days=1) # увеличиваем дату на один день

# Создаем экземпляр фильма с названием и расписанием
movie = Movie("Елки inf", [
    (datetime(2024, 12, 31), datetime(2025, 1, 3)),
    (datetime(2025, 1, 5), datetime(2025, 1, 7)),
    (datetime(2025, 2, 1), datetime(2025, 2, 1))
])

# Проверяем работу генератора
print(f"Расписание показа фильма '{movie.title}':")
for showing_date in movie.schedule():
    print(showing_date)