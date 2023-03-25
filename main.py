class Employee:

    def __init__(self, organisation, position, double_experience, name, gender, age, double_salary):
        self.__organisation = organisation  # Место работы
        self._position = position  # Должность
        self._double_experience = double_experience  # Стаж
        self._name = name  # имя
        self._gender = gender  # пол
        self._age = age  # Возраст
        self._double_salary = double_salary  # Заработная плата

    # ______________________________________________________________________________________________________________________
    def __str__(self):
        return f'Сотрудник компании: {self.__organisation}\nДолжность: {self._position}\nСтаж работы:' \
               f'{self._double_experience}\nИмя: {self._name}\n' \
               f'Пол: {self._gender}\nВозраст: {self._age}\nЗарплата: {self._double_salary}тыс/руб\n'

    def print_info(self):  # Получение информации о месте работы, занимаемой должности, стаже работы, заработной платы
        print("Организация: {}".format(self.__organisation))
        print("Занимаемая должность: {}".format(self._position))
        print("Стаж: {}".format(self._double_experience))
        print("Заработная плата: {}".format(self._double_salary))

    def new_position(self):
        worker._position = str(input("Новая занимаемая должность: ").format(self._position))
        return self._position

    def double_salary(self):
        worker._double_salary = worker._double_salary + int(input("Начисление зарплаты: ").format(self._double_salary))
        return self._double_salary

    # ______________________________________________________________________________________________________________________
    @staticmethod
    def number_of_staff():
        print('Количество сотрудников:', len(mylist))

    def append(self):
        return self.number_of_staff()

    @property
    def gender(self):
        return self._gender

    @property
    def name(self):
        return self._name


# _____________________________________________________________________________________________________________________

mylist = tuple

worker = Employee(input("Введите название компании: "), str(input("Введите название должности: ")),
                  int(input("Введите стаж работы: ")), str(input("Введите имя сотрудника: ")),
                  str(input("Введите пол сотрудника:")), int(input("Введите возраст сотрудника:")),
                  int(input("Зарплата сотрудника: ")))

print("\nПолучить Информацию:\n"
      "____________________________\n"
      "Вывести список всех сотрудников---> 0\n"
      "Место работы, занимаемая должность, стаж работы, заработная плата---> 1 \n"
      "Изменение должности---> 2\n"
      "Начисление заработной платы---> 3\n"
      "Вывод личных данных---> 4\n"
      "операция сравнения объектов---> 5\n,"
      "____________________________")

while True:
    func_programing = int(input("Выберите пункт действия: "))
    if func_programing != 0 and func_programing != 1 and func_programing != 2 and func_programing != 3 \
            and func_programing != 4 and func_programing != 5:
        print("Защита от детей, повторите ввод")
        continue
        
    if worker == Employee:
        worker.append()
        
    if func_programing == 0:
        print(mylist)

    if func_programing == 1:
        print(worker.print_info())

    if func_programing == 2:
        print(worker.new_position())

    if func_programing == 3:
        print(worker.double_salary())

    if func_programing == 4:
        print(worker.name)
        print(worker.gender)
