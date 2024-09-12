# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import yaml


class YAMLDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)

        for item in yaml_data:
            for name, subjects in item.items():
                self.students[name] = [(subject, score)
                                       for subject, score in subjects.items()]

        return self.students
