# -*- coding: utf-8 -*-
"""РК №1. Вариант запросов А, предметная область 26 (Студенческая группа - Учебный курс)."""

from operator import itemgetter

class Student:
    """Студент (Связь: много)."""
    def __init__(self, id, fio, score, course_id):
        self.id = id
        self.fio = fio
        self.score = score      # Количественный признак (средний балл)
        self.course_id = course_id

class Course:
    """Учебный курс (Связь: один)."""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class StudentCourse:
    """Связь многие-ко-многим: Студент - Курс."""
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id

# Тестовые данные
courses = [
    Course(1, 'Базовый курс программирования'),
    Course(2, 'Математический анализ'),
    Course(3, 'Физика'),
    Course(11, 'Продвинутый курс Python'),
    Course(22, 'Дискретная математика'),
    Course(33, 'Квантовая физика')
]

students = [
    Student(1, 'Артамонов', 4.5, 1),
    Student(2, 'Петров', 3.8, 2),
    Student(3, 'Иваненко', 5.0, 3),
    Student(4, 'Иванов', 4.2, 3),
    Student(5, 'Иванин', 3.5, 3)
]

students_courses = [
    StudentCourse(1, 1), StudentCourse(1, 11),
    StudentCourse(2, 2), StudentCourse(2, 22),
    StudentCourse(3, 3), StudentCourse(3, 33),
    StudentCourse(4, 3), StudentCourse(4, 33),
    StudentCourse(5, 3), StudentCourse(5, 33)
]

def main():
    # Соединение данных один-ко-многим
    one_to_many = [(s.fio, s.score, c.name)
                   for c in courses
                   for s in students
                   if s.course_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, sc.course_id, sc.student_id)
                         for c in courses
                         for sc in students_courses
                         if c.id == sc.course_id]

    many_to_many = [(s.fio, s.score, course_name)
                    for course_name, course_id, student_id in many_to_many_temp
                    for s in students if s.id == student_id]

    print('Задание А1')
    # Сортировка по названию курса (индекс 2)
    res_11 = sorted(one_to_many, key=itemgetter(2))
    for item in res_11:
        print(item)

    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все курсы
    for c in courses:
        c_students = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(c_students) > 0:
            c_scores = [score for _, score, _ in c_students]
            c_scores_sum = sum(c_scores) # Суммарный балл
            res_12_unsorted.append((c.name, c_scores_sum))

    # Сортировка по суммарному баллу (по убыванию)
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    for item in res_12:
        print(item)

    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все курсы
    for c in courses:
        if 'курс' in c.name.lower():
            c_students = list(filter(lambda i: i[2] == c.name, many_to_many))
            c_students_names = [x for x, _, _ in c_students]
            res_13[c.name] = c_students_names

    for key, value in res_13.items():
        print(f"'{key}': {value}")

if __name__ == '__main__':
    main()
