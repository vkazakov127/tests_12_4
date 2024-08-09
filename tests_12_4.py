# -*- coding: utf-8 -*-
# tests_12_4.py
import unittest
import rt_with_exceptions as r_
import logging


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []
        # Настройка логирования
        logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                            format='%(asctime)s | %(levelname)s | %(message)s')

    def setUp(self):
        self.runner1 = r_.Runner('Усэйн', 10)
        self.runner2 = r_.Runner('Андрей', 9)
        self.runner3 = r_.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print('-------- Все результаты соревнований -------')
        for result1 in cls.all_results:
            one_result_dict = {}  # Буфер, для вывода как словарь
            for key, value in result1.items():
                value1 = str(value)  # Извлекаем "name"
                value1 = f'{value1:6}'  # Форматирование строки
                one_result_dict[key] = value1
            print(one_result_dict)

    def test_tour1(self):
        # Андрей и Ник
        tour1 = r_.Tournament(90, self.runner2, self.runner3)
        result1 = tour1.start()
        self.__class__.all_results.append(result1)  # Сохраняем в общий список
        last_index = list(result1.keys())[-1]  # Индекс последнего бегуна
        last_name = result1.get(last_index)  # Имя последнего бегуна
        # --------- Собственно, тест
        self.assertEqual(last_name, self.runner3.name)  # Тест

    def test_tour2(self):
        # Усэйн и Ник
        tour1 = r_.Tournament(90, self.runner1, self.runner3)
        result1 = tour1.start()
        self.__class__.all_results.append(result1)  # Сохраняем в общий список
        last_index = list(result1.keys())[-1]  # Индекс последнего бегуна
        last_name = result1.get(last_index)  # Имя последнего бегуна
        # --------- Собственно, тест
        self.assertEqual(last_name, self.runner3.name)  # Тест

    def test_tour3(self):
        # Усэйн, Андрей и Ник
        tour1 = r_.Tournament(90, self.runner1, self.runner2, self.runner3)
        result1 = tour1.start()
        self.__class__.all_results.append(result1)  # Сохраняем в общий список
        last_index = list(result1.keys())[-1]  # Индекс последнего бегуна
        last_name = result1.get(last_index)  # Имя последнего бегуна
        # --------- Собственно, тест
        self.assertEqual(last_name, self.runner3.name)  # Тест


class RunnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding = 'utf-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')

    def test_run(self):
        try:
            runner_test = r_.Runner('somebody', -7)
            runner_test.run()
            distance_test = runner_test.distance
            # Собственно, тест
            self.assertEqual(distance_test, 14)
            logging.info(f'"test_run" выполнен успешно')
        except:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)
            distance_test = None
            # Собственно, тест
            self.assertEqual(distance_test, 14)

    def test_walk(self):
        try:
            runner_test = r_.Runner(282, 7)
            runner_test.walk()
            distance_test = runner_test.distance
            # Собственно, тест
            self.assertEqual(distance_test, 7)
            logging.info(f'"test_walk" выполнен успешно')
        except:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)
            distance_test = None
            # Собственно, тест
            self.assertEqual(distance_test, 7)
