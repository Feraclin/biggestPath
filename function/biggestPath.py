from re import fullmatch
from typing import List


class LengthPathOutOfRange(ValueError): pass


class DuplicateName(ValueError): pass


class BiggestPath:
    MAX_LENGTH_PATH: int = 255

    @classmethod
    def __call__(cls, dct: dict) -> str:
        return '/' + cls.find_path(dct).rstrip('/')

    @staticmethod
    def name_check(name: str) -> bool:
        '''Проверяем имя каталог на соотвесвие требованию имена директорий/файлов
        должны состоят только из букв английского алфавита и цифр'''
        name_pattern = r'^[a-zA-Z\d]*$'
        return bool(fullmatch(name_pattern, name))

    @staticmethod
    def check_duplicate_name(lst: List[str]) -> bool:
        '''Проверяем уникальность имен файлов в каталоге'''
        return len(lst) != len(set(lst))

    @staticmethod
    def check_length(name: str) -> bool:
        '''Проверяем длину пути менее 255 символов'''
        return len(name) > __class__.MAX_LENGTH_PATH

    @classmethod
    def find_path(cls, dct: dict) -> str:
        '''Ищем самый длинный путь'''
        out = ''
        for k, v in dct.items():
            match v:
                case dict() if cls.name_check(k):
                    if len(tmp_out := f'{k}{"/"}{cls.find_path(v)}') > len(out):
                        out = tmp_out
                        if cls.check_length(out):
                            raise LengthPathOutOfRange
                case list() if cls.name_check(k):
                    if cls.check_duplicate_name(v):
                        raise DuplicateName
                    else:
                        out += f'{k}{"/"}{max(v)}'
        return out
