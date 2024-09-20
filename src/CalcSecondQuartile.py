# -*- coding: utf-8 -*-
from Types import DataType
import numpy as np


class CalcSecondQuartile:
    def __init__(self, data: DataType):
        self.data = data

    def students_in_second_quartile(self, ratings):
        # Если нет рейтингов, то возвращаем пустой словарь
        if not ratings:
            return {}

        # Преобразуем значения рейтингов в список
        rating_values = list(ratings.values())

        # Получаем второй квартиль
        q1, q3 = np.percentile(rating_values, [25, 75])

        second_quartile_students = {}
        # Ищем студентов, чьи рейтинги попадают во второй квартиль
        for student, rating in ratings.items():
            if q1 <= rating <= q3:
                second_quartile_students[student] = rating

        return second_quartile_students
