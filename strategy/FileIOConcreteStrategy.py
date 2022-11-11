# -*-coding utf-8-*-
import pickle
import os

from strategy.IOStrategy import IOStrategy


class FileIOConcreteStrategy(IOStrategy):
    def read(self):
        with open(f'dumps{os.sep}notes.dumps', 'rb') as file:
            try:
                return pickle.load(file)['data']
            except IOError:
                print('Файл не найден')

                return []

    def write(self, notes):
        with open(f'dumps{os.sep}notes.dumps', 'wb') as file:
            try:
                pickle.dump({'data': notes}, file)
            except IOError:
                print('Файла не найден')
