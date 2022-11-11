class ValueNotInArrayError(Exception):
    def __str__(self):
        return 'Значение слишком мало или слишком велико'
    pass

class ChoiseError(Exception):
    def __str__(self):
        return 'Выбрана некорректная команда, файлы экстренно сохранены в файл'
    pass

class ValueNotInt(Exception):
    def __str__(self):
        return 'Значение не int'
    pass

