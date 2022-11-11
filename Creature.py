from Note import Note
from Exceptions import ValueNotInArrayError, ValueNotInt

class Creature(Note):
    price: int = ''

    def set_note(self):
        print('Создаем существо ...')

        self.title = input('Название: ',)
        self.description = input('Описание: ',)

        while True:
            price = input('Цена: ',)

            if input_check(price, "int", 0, 1000000):
                self.price = price

                break

    def print_note(self):
        print(self.__str__())

    def __str__(self):
        return '\n Заголовок: {0} \n Описание: {1} \n Цена: {2}$ \n'.format(self.title, self.description, self.price)


def input_check(value, type='int', min_value=0, max_value=100):
    """
    Проверка введенного значения на тип int
    """
    if type == 'int':
        try:
            if int(value) >= min_value or int(value) <= max_value:
                return True
            print(f"{value} не входит в интервал от {min_value} до {max_value}")
            raise ValueNotInArrayError
        except:
            return False
    else:
        raise ValueNotInt