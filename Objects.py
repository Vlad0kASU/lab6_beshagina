# -*-coding utf-8-*-
from dataclasses import dataclass
from typing import List

from Note import Note
from strategy import ConsoleIOConcreteStrategy, FileIOConcreteStrategy
from Creature import input_check


@dataclass
class Objects:
    __notes: List[Note]

    def __init__(self):
        self.__notes = []

        self.commands = {
            1: self.add_note,
            2: self.edit_note,
            3: self.delete_note,
            4: self.show_notes,
            5: self.save_notes,
            6: self.load_notes,
            7: self.clear_notes
        }

        self.strategy = ConsoleIOConcreteStrategy

    def run_command(self, command):
        self.commands[command]()

    def change_strategy(self, strategy):
        self.strategy = strategy

    def show_notes(self):
        self.strategy = ConsoleIOConcreteStrategy()

        self.strategy.write(self.__notes)

    def add_note(self):
        self.strategy = ConsoleIOConcreteStrategy()

        self.__notes.append(self.strategy.read())

    def edit_note(self):
        self.show_notes()

        while True:
            index = int(input('Выберите запись: ',))

            if input_check(index, "int", 0, len(self.__notes) - 1):
                try:
                    note = self.__notes[index]

                    note.set_note()

                    print('Запись отредактирована')
                except IndexError:
                    print('Такой записи не существует')

                break
            else:
                self.show_notes()

    def delete_note(self):
        self.show_notes()

        while True:
            index = input('Выберите запись: ', )

            if input_check(index, "int", 0, len(self.__notes) - 1):
                try:
                    index = int(index)

                    self.__notes.pop(index)

                    print('Запись удалена')
                except Exception:
                    print('Такой записи не существует')

                break
            else:
                self.show_notes()

    def save_notes(self):
        self.strategy = FileIOConcreteStrategy()
        self.strategy.write(self.__notes)

        print('Файл успешно сохранен!')

    def load_notes(self):
        self.strategy = FileIOConcreteStrategy()
        self.__notes = self.strategy.read()

        print('Файл успешно загружен!')

    def clear_notes(self):
        self.__notes = []

        print('Все записи удалены!')
