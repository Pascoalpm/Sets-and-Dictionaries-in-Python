#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Список студентов
    students = []

    print("Система управления студентами")
    print("Введите команду (add, list, select, help, exit)")

    # Организовать бесконечный цикл запроса команд
    while True:
        # Запросить команду из терминала
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о студенте
            name = input("Фамилия и инициалы? ")
            group = input("Номер группы? ")

            # Успеваемость (5 элементов)
            print("Успеваемость (5 оценок через пробел, например: 5 4 3 2 4):")
            grades_input = input("Оценки: ")
            grades_list = grades_input.split()

            grades = []
            for i in range(5):
                if i < len(grades_list):
                    try:
                        grade = int(grades_list[i])
                        grades.append(grade)
                    except ValueError:
                        grades.append(0)
                else:
                    grades.append(0)

            # Создать словарь
            student = {
                'name': name,
                'group': group,
                'grades': grades
            }

            # Добавить словарь в список
            students.append(student)

            # Упорядочить по алфавиту
            if len(students) > 1:
                students.sort(key=lambda item: item.get('name', ''))

            print(f"Студент {name} добавлен.")

        elif command == 'list':
            print("\nСписок студентов:")
            print("-" * 40)

            for idx, student in enumerate(students, 1):
                print(f"{idx}. {student.get('name', '')} - {student.get('group', '')}")
                print(f"   Оценки: {student.get('grades', [])}")

            if not students:
                print("Студентов нет")

            print("-" * 40)

        elif command == 'select':
            print("\nСтуденты с оценкой 2:")
            print("-" * 40)

            count = 0
            for student in students:
                if 2 in student.get('grades', []):
                    count += 1
                    print(f"{count}. {student.get('name', '')} ({student.get('group', '')})")

            if count == 0:
                print("Студентов с оценкой 2 не найдено.")

            print("-" * 40)

        elif command == 'help':
            print("\nСписок команд:")
            print("add - добавить студента")
            print("list - вывести список студентов")
            print("select - запросить студентов с оценкой 2")
            print("help - отобразить справку")
            print("exit - завершить работу с программой")

        else:
            print(f"Неизвестная команда '{command}'", file=sys.stderr)
            print("Введите 'help' для списка команд")