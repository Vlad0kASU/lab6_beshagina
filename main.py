from Objects import Objects
from Menu import Menu
from Exceptions import ChoiseError

def main():
    objects = Objects()

    menu_options = [
        'Добавить объект выбранного типа',
        'Редактировать',
        'Удалить объект',
        'Вывести на экран весь список',
        'Сохранить в файл',
        'Загрузить из файла',
        'Очистить список объектов',
        'Выход']

    menu = Menu('Меню:', menu_options)

    while True:
        command = menu.show_menu()

        if command == len(menu_options):
            break
        elif command < len(menu_options):
            objects.run_command(command)
        else:
            objects.save_notes()
            raise ChoiseError


if __name__ == '__main__':
    main()

