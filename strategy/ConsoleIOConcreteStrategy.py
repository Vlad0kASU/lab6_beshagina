# -*-coding utf-8-*-
from Creature import Creature
from Note import Note
from strategy.IOStrategy import IOStrategy
from Menu import Menu


class ConsoleIOConcreteStrategy(IOStrategy):
    def __init__(self):
        self.note_types = [
            {'title': 'Запись', 'class': Note},
            {'title': 'Существо', 'class': Creature}
        ]

    def read(self):
        menu = Menu('Выберите тип: ', list([str(item['title']) for item in self.note_types]))

        note = self.note_types[menu.show_menu() - 1]['class']()
        note.set_note()

        return note

    def write(self, notes):
        for i, item in enumerate(notes):
            print('\n Запись №{}: '.format(i))

            item.print_note()