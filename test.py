from main import Employee


worker1 = Employee('positive technology', 'Ведущий инженер', '20', 'Анастасия', 'Женский', '30 лет', int(40000))
worker2 = Employee('positive technology', 'Ведущий инженер', '30', 'Влад', 'Мужской', '20 лет', int(50000))
worker3 = Employee('positive technology', 'Начальник отдела', '20', 'Петя', 'Мужской', '50 лет', int(150000))

mylist = [worker1, worker2, worker3]

# test_list
number_worker = Employee  # Так как статический метод, то определяем к какому классу относится данная функция
number_worker.number_of_staff()  # Выводим в консоль значения с 'mylist'

print(worker1)

worker2._double_salary += 50000
print(worker2)

worker3._position = 'УБОРЩИК'

print(worker3)

print('Вывод личных данных:', worker1.print_info())

worker2.__str__()

print(mylist)



