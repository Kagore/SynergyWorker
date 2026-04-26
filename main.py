from worker import WORKER
from datetime import datetime

def main():
    print("=== Университет Синергия - Отдел Кадров (Python) ===")
    
    # Защита от ввода неверного типа данных
    try:
        n = int(input("Введите количество сотрудников для добавления в базу: "))
    except ValueError:
        print("Ошибка: необходимо ввести целое число.")
        return

    # Использование динамического массива (стандартный список list в Python)
    synergy_workers = []

    # Ввод данных
    for i in range(n):
        print(f"\nСотрудник № {i + 1}:")
        name = input("Фамилия и инициалы (например, Иванов И.И.): ")
        pos = input("Должность (например, Куратор, Преподаватель): ")
        try:
            sal = float(input("Зарплата (руб.): "))
            year = int(input("Год поступления на работу (например, 2018): "))
        except ValueError:
            print("Ошибка ввода чисел! Пропускаем этого сотрудника, данные некорректны.")
            continue
            
        # Создание объекта и добавление в динамический массив
        new_worker = WORKER(full_name=name, position=pos, salary=sal, year=year)
        synergy_workers.append(new_worker)

    # Фильтрация по стажу
    try:
        experience_threshold = int(input("\nВведите требуемый стаж работы (полных лет) для фильтрации: "))
    except ValueError:
        print("Ошибка: необходимо ввести целое число.")
        return

    current_year = datetime.now().year
    found = False

    print(f"\n--- Сотрудники со стажем более {experience_threshold} лет ---")
    for w in synergy_workers:
        experience = current_year - w.get_year()
        if experience > experience_threshold:
            print(f"- {w.get_full_name()} (Стаж: {experience} лет)")
            found = True

    # Если таких работников нет
    if not found:
        print("Сотрудников с таким стажем в организации нет.")

if __name__ == "__main__":
    main()