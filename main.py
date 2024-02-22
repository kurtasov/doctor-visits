from view import View
from controller import Controller


class App():
    def __init__(self):
        self.view = View()
        self.controller = Controller(self.view)
        self.view.set_controller(self.controller)


if __name__ == "__main__":
    app = App()
    app.view.prompt_loop()
