class Note:
    title: str = ''
    description: str = ''

    def set_note(self):
        print('Создаем запись ...')

        self.title = input('Заголовок: ',)
        self.description = input('Описание: ',)

    def print_note(self):
        print(self.__str__())

    def __str__(self):
        return '\n Заголовок: {0} \n Описание: {1} \n'.format(self.title, self.description)