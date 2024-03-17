import requests
from src.classes_template import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    """
    Класс для работы с API запросами c сайта hh.ru
    """

    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query):
        """
        Функция возвращает данные с сайта по введенному ключу
        :param search_query:
        :return: json object
        """
        params = {"per_page": 100, "text": search_query, "page": 10}
        response = requests.get(self.__base_url, params=params)
        return response.json()["items"]
