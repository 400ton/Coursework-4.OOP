from src.head_hunterAPI import HeadHunterAPI
from src.vacancy import Vacancy
from src.json_saving import JSONManager


# Функция для взаимодействия с пользователем
def user_interaction():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ").lower()
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().split()
    # salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    # # Получение вакансий с hh.ru в формате JSON по запросу
    hh_vacancies = hh_api.get_vacancies(search_query)

    # # Сохранение информации о вакансиях в файл
    json_saving = JSONManager('data/data.json')
    json_saving.add_vacancy(hh_vacancies)
    #
    # # Преобразование набора данных из JSON в список объектов
    data = json_saving.open_file()
    vacancy = Vacancy.from_dict(data)
    print(len(vacancy))
    for value in vacancy:
        print(f"{value}\n")

    # filtered_vacancies = filter_vacancies(hh_vacancies, filter_words)
    #
    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)

    # Очистка файла
    json_saving.delete_vacancy()


if __name__ == "__main__":
    user_interaction()
