from datetime import datetime

class WORKER:

    def __init__(self, full_name="", position="", salary=0.0, year=None):
        self.__full_name = full_name
        self.__position = position
        self.__salary = salary
        self.__year = year if year is not None else datetime.now().year

    def __del__(self):
        pass

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def set_position(self, position):
        self.__position = position

    def set_salary(self, salary):
        self.__salary = salary

    def set_year(self, year):
        self.__year = year

    def get_full_name(self):
        return self.__full_name

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__salary

    def get_year(self):
        return self.__year

    def display(self):
        print(f"ФИО: {self.__full_name} | Должность: {self.__position} | Зарплата: {self.__salary} руб. | Год поступления: {self.__year}")