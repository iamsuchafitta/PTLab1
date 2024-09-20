# -*- coding: utf-8 -*-
import pytest
from src.CalcSecondQuartile import CalcSecondQuartile
from src.CalcRating import CalcRating
from src.Types import DataType, RatingsType


class TestCalcSecondQuartile:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [("математика", 80),
                 ("русский язык", 76),
                 ("программирование", 100)],
            "Петров Игорь Владимирович":
                [("математика", 61),
                 ("русский язык", 80),
                 ("программирование", 78),
                 ("литература", 97)],
            "Иванов Сергей Александрович":
                [("математика", 55),
                 ("русский язык", 60),
                 ("программирование", 70)],
            "Сидоров Николай Михайлович":
                [("математика", 40),
                 ("русский язык", 50),
                 ("программирование", 45)]
        }

        rating_scores: RatingsType = {
            "Абрамов Петр Сергеевич": 85.3333,
            "Петров Игорь Владимирович": 79.0000,
            "Иванов Сергей Александрович": 61.6667,
            "Сидоров Николай Михайлович": 45.0000
        }

        second_quartile_students = {
            "Петров Игорь Владимирович": 79.0000,
            "Иванов Сергей Александрович": 61.6667
        }

        return data, rating_scores, second_quartile_students

    def test_init_calc_second_quartile(self,
                                       input_data:
                                       tuple[DataType, RatingsType]) -> None:
        calc_quartile = CalcSecondQuartile(input_data[0])
        assert input_data[0] == calc_quartile.data

    def test_students_in_second_quartile(self,
                                         input_data:
                                         tuple[DataType, RatingsType]) -> None:
        data, rating_scores, expected_students = input_data

        # Рассчитываем рейтинги
        ratings = CalcRating(data).calc()

        # Получаем студентов во втором квартиле
        second_quartile_students = (CalcSecondQuartile(data).
                                    students_in_second_quartile(ratings))

        # Проверяем, что ключи (имена студентов) совпадают
        assert (set(second_quartile_students.keys()) ==
                set(expected_students.keys()))

        # Проверяем значения с учетом возможной погрешности
        for student in expected_students:
            assert abs(second_quartile_students[student] -
                       expected_students[student]) < 1e-4

    def test_empty_data(self):
        data: DataType = {}
        calc_quartile = CalcSecondQuartile(data)
        assert calc_quartile.students_in_second_quartile({}) == {}

    def test_single_student(self):
        data: DataType = {
            "Сидоров Николай Михайлович": [("математика", 70)]
        }
        calc_quartile = CalcSecondQuartile(data)
        ratings = {"Сидоров Николай Михайлович": 70}
        assert calc_quartile.students_in_second_quartile(ratings) == {
            "Сидоров Николай Михайлович": 70
        }

    def test_even_number_of_students(self):
        data: DataType = {
            "Студент 1": [("математика", 80)],
            "Студент 2": [("математика", 70)],
            "Студент 3": [("математика", 60)],
            "Студент 4": [("математика", 50)]
        }
        calc_quartile = CalcSecondQuartile(data)
        ratings = {
            "Студент 1": 80,
            "Студент 2": 70,
            "Студент 3": 60,
            "Студент 4": 50
        }
        expected = {
            "Студент 2": 70,
            "Студент 3": 60
        }
        assert calc_quartile.students_in_second_quartile(ratings) == expected

    def test_odd_number_of_students(self):
        data: DataType = {
            "Студент 1": [("математика", 90)],
            "Студент 2": [("математика", 80)],
            "Студент 3": [("математика", 70)],
            "Студент 4": [("математика", 60)],
            "Студент 5": [("математика", 50)]
        }
        calc_quartile = CalcSecondQuartile(data)
        ratings = {
            "Студент 1": 90,
            "Студент 2": 80,
            "Студент 3": 70,
            "Студент 4": 60,
            "Студент 5": 50
        }
        expected = {
            "Студент 2": 80,
            "Студент 3": 70,
            "Студент 4": 60
        }
        assert calc_quartile.students_in_second_quartile(ratings) == expected

    def test_all_students_same_rating(self):
        data: DataType = {
            "Студент 1": [("математика", 70)],
            "Студент 2": [("математика", 70)],
            "Студент 3": [("математика", 70)],
            "Студент 4": [("математика", 70)]
        }
        calc_quartile = CalcSecondQuartile(data)
        ratings = {
            "Студент 1": 70,
            "Студент 2": 70,
            "Студент 3": 70,
            "Студент 4": 70
        }
        expected = ratings  # Все студенты должны быть во втором квартиле
        assert calc_quartile.students_in_second_quartile(ratings) == expected

    def test_boundary_values(self):
        data: DataType = {
            "Студент 1": [("математика", 100)],
            # Верхняя граница второго квартиля
            "Студент 2": [("математика", 75)],
            "Студент 3": [("математика", 50)],
            # Нижняя граница второго квартиля
            "Студент 4": [("математика", 25)],
            "Студент 5": [("математика", 0)]
        }
        calc_quartile = CalcSecondQuartile(data)
        ratings = {
            "Студент 1": 100,
            "Студент 2": 75,
            "Студент 3": 50,
            "Студент 4": 25,
            "Студент 5": 0
        }
        expected = {
            "Студент 2": 75,
            "Студент 3": 50,
            "Студент 4": 25
        }
        assert calc_quartile.students_in_second_quartile(ratings) == expected
