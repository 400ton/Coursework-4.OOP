from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """
    Абстрактный класс для работы API сервиса с вакансиями
    """

    @abstractmethod
    def get_vacancies(self, search_query):
        pass


class AbstractVacancy(ABC):
    """
    Абстрактный класс который обязывает реализовать методы
    для добавления вакансий в файл, получения данных из файла
    по указанным критериям и удаления информации о вакансиях
    """

    @abstractmethod
    def add_data_to_dict(self, vacancy):
        pass

    @abstractmethod
    def get_data_from_dict(self, keys):
        pass

    @abstractmethod
    def del_data_dict(self):
        pass
