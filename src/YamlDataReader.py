# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import yaml

#Students:  {'Иванов Иван Иванович': [('математика', 80), ('программирование', 90), ('литература', 76)],
#            'Петров Петр Петрович': [('математика', 100), ('социология', 90), ('химия', 61)]}

class YamlDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)

        for student in yaml_data:
            for name, subjects in student.items():
                self.students[name] = [(subject, score) for subject, score in subjects.items()]

        return self.students
