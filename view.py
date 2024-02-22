from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from itertools import product


class View:
    def __init__(self):
        print('Начинаем работу...')


    def set_controller(self, controller):
        self.controller = controller


    def set_entity_names(self, entity_names):
        self.entity_names = entity_names


    def ask_question(self, question):
        user_answer = prompt(question)
        return user_answer


    def show_error(self, message):
        print('Ошибка!', message)


    def prompt_loop(self):
        crud_verbs = ['добавить', 'найти', 'изменить', 'удалить']
        possible_actions = [': '.join(t) for t in list(product(crud_verbs, self.entity_names))]

        while True:
            user_input = prompt('> ', completer=WordCompleter(possible_actions, ignore_case=True))

            if user_input.split(': ')[0] == 'добавить':
                self.controller.create(user_input.split(': ')[1])
            elif user_input.split(': ')[0] == 'найти':
                self.controller.read(user_input.split(': ')[1])
            elif user_input.split(': ')[0] == 'изменить':
                self.controller.update(user_input.split(': ')[1])
            elif user_input.split(': ')[0] == 'удалить':
                self.controller.delete(user_input.split(': ')[1])
            else:
                print('Неизвестная команда.')
