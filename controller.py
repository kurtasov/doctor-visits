import models
from datetime import datetime
import queryhelper


patient_data = [
    {"last_name":"Кулишенко","first_name":"Леонид","patronymic":"Александрович","gender":"M","date_of_birth":"1952-06-25"},
    {"last_name":"Некрасов","first_name":"Рафаил","patronymic":"Александрович","gender":"M","date_of_birth":"1935-09-29"},
    {"last_name":"Пономаренко","first_name":"Ян","patronymic":"Александрович","gender":"M","date_of_birth":"1942-02-12"},
    {"last_name":"Шумейко","first_name":"Шамиль","patronymic":"Александрович","gender":"M","date_of_birth":"1946-04-11"},
    {"last_name":"Колобова","first_name":"Клементина","patronymic":"Александровна","gender":"F","date_of_birth":"1944-05-03"},
    {"last_name":"Рыбакова","first_name":"Устинья","patronymic":"Александровна","gender":"F","date_of_birth":"1929-08-17"},
    {"last_name":"Чикольба","first_name":"Эльмира","patronymic":"Александровна","gender":"F","date_of_birth":"1938-07-07"},
    {"last_name":"Тимошенко","first_name":"Тарас","patronymic":"Алексеевич","gender":"M","date_of_birth":"1970-03-17"},
    {"last_name":"Зиновьева","first_name":"Флорентина","patronymic":"Алексеевна","gender":"F","date_of_birth":"1928-08-07"},
    {"last_name":"Козлова","first_name":"Зинаида","patronymic":"Алексеевна","gender":"F","date_of_birth":"1983-08-31"},
    {"last_name":"Пономаренко","first_name":"Зинаида","patronymic":"Алексеевна","gender":"F","date_of_birth":"1942-02-12"},
    {"last_name":"Мельников","first_name":"Йозеф","patronymic":"Анатолиевич","gender":"M","date_of_birth":"1949-02-05"},
    {"last_name":"Овчаренко","first_name":"Григорий","patronymic":"Анатолиевич","gender":"M","date_of_birth":"1953-11-10"},
    {"last_name":"Терентьева","first_name":"Нина","patronymic":"Анатолиевна","gender":"F","date_of_birth":"1926-10-19"},
    {"last_name":"Чикольба","first_name":"Янита","patronymic":"Анатолиевна","gender":"F","date_of_birth":"1938-07-07"},
    {"last_name":"Коломоец","first_name":"Арсений","patronymic":"Андреевич","gender":"M","date_of_birth":"1944-05-03"},
    {"last_name":"Рожков","first_name":"Йоханес","patronymic":"Андреевич","gender":"M","date_of_birth":"1936-09-08"},
    {"last_name":"Шаров","first_name":"Александр","patronymic":"Андреевич","gender":"M","date_of_birth":"1957-02-08"},
    {"last_name":"Зайцева","first_name":"Глафира","patronymic":"Андреевна","gender":"F","date_of_birth":"1937-11-28"},
    {"last_name":"Ильина","first_name":"Алёна","patronymic":"Андреевна","gender":"F","date_of_birth":"1952-06-25"}
];

doctor_data = [
    {"last_name":"Иванов","first_name":"Иван","patronymic":"Иванович","fee_per_visit":2500.0},
    {"last_name":"Виноградова","first_name":"Инесса","patronymic":"Валерьевна","fee_per_visit":3500.0},
    {"last_name":"Горобчук","first_name":"Гертруда","patronymic":"Артёмовна","fee_per_visit":2400.0},
    {"last_name":"Борисова","first_name":"Ульяна","patronymic":"Львовна","fee_per_visit":2500.0},
    {"last_name":"Ерёменко","first_name":"Чилита","patronymic":"Сергеевна","fee_per_visit":2700.0},
    {"last_name":"Медведев","first_name":"Матвей","patronymic":"Григорьевич","fee_per_visit":8000.0},
    {"last_name":"Соболев","first_name":"Жерар","patronymic":"Вадимович","fee_per_visit":8500.0},
    {"last_name":"Чикольба","first_name":"Бронислава","patronymic":"Анатолиевна","fee_per_visit":9000.0},
    {"last_name":"Фокина","first_name":"Устинья","patronymic":"Львовна","fee_per_visit":1500.0},
    {"last_name":"Фомичёва","first_name":"Жанна","patronymic":"Борисовна","fee_per_visit":4500.0},
    {"last_name":"Фролова","first_name":"Ольга","patronymic":"Евгеньевна","fee_per_visit":5000.0},
    {"last_name":"Игнатьев","first_name":"Денис","patronymic":"Богданович","fee_per_visit":3000.0},
    {"last_name":"Дементьев","first_name":"Цицерон","patronymic":"Романович","fee_per_visit":5000.0},
    {"last_name":"Дзюба","first_name":"Доминика","patronymic":"Львовна","fee_per_visit":6000.0}
];


class Controller:
    def __init__(self, view):
        self.view = view
        self.entity_names = models.get_entity_names()
        self.view.set_entity_names(self.entity_names)

        try:
            models.db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
            models.db.generate_mapping(create_tables=True)
            models.populate_sample_data(models.Patient, patient_data)
            models.populate_sample_data(models.Doctor, doctor_data)
        except Exception as e:
            self.view.show_error(e)


    def create(self, entity):
        self.view.show_error(f'Добавление для сущности {entity} не реализовано!')


    def read(self, entity):
        if entity == 'Patient':
            birth_date = self.view.ask_question("Введите дату рождения: ")
            queryhelper.lookup_patient(birth_date)
            return

        if entity == 'Doctor':
            last_name = self.view.ask_question("Введите фамилию: ")
            queryhelper.lookup_doctor(last_name)
            return

        self.view.show_error(f'Чтение для сущности {entity} не реализовано!')


    def update(self, entity):
        self.view.show_error(f'Изменение для сущности {entity} не реализовано!')


    def delete(self, entity):
        self.view.show_error(f'Удаление для сущности {entity} не реализовано!')
