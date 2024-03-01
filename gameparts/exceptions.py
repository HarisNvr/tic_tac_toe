# gameparts/exceptions.py

class FieldIndexError(IndexError):

    def __str__(self):
        return 'Введено значение за границами игрового поля'

# Вот оно - новое исключение, унаследованное от базового класса Exception.
class CellOccupiedError(Exception):

    def __str__(self):
        return 'Попытка изменить занятую ячейку'