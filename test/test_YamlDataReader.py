# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.YamlDataReader import YamlDataReader

class TestYamlDataReader:

    @pytest.fixture()
    def yaml_file_and_data_content(self) -> tuple[str, DataType]:
        text = """
- Иванов Иван Иванович:
      математика: 80
      программирование: 90
      литература: 76
- Петров Петр Петрович:
      математика: 100
      социология: 90
      химия: 61
"""

        data = {
            "Иванов Иван Иванович": [
                ("математика", 80),
                ("программирование", 90),
                ("литература", 76)
            ],
            "Петров Петр Петрович": [
                ("математика", 100),
                ("социология", 90),
                ("химия", 61)
            ]
        }
        return text, data

    @pytest.fixture()
    def yaml_filepath_and_data(self, yaml_file_and_data_content: tuple[str, DataType],
                               tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.yaml")
        p.write_text(yaml_file_and_data_content[0], encoding='utf-8')
        return str(p), yaml_file_and_data_content[1]

    def test_read(self, yaml_filepath_and_data: tuple[str, DataType]) -> None:
        file_content = YamlDataReader().read(yaml_filepath_and_data[0])
        assert file_content == yaml_filepath_and_data[1]

