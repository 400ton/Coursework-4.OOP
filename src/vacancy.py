class Vacancy:
    def __init__(self, name, description, salary, _url):
        self.name = name
        self.description = description
        self.salary = salary
        self._url = _url

    def is_salary(self):
        if self.salary is None:
            return "Зарплата не указана"
        else:
            return self.salary

    def __lt__(self, other):
        if self.salary < other.salary:
            pass

    def __eq__(self, other):
        pass

    @staticmethod
    def from_dict(data):
        """
        Преобразование набора данных из JSON в список объектов
        :param data:
        :return:
        """
        vacancy = []
        for value in data:
            name = value['name']
            url = value['alternate_url']
            area = value['area']
            salary = value['salary']
            snippet = value["snippet"]
            experience = value['experience']
            vacancy.append(dict(name=name, url=url, area=area, salary=salary, snippet=snippet, experience=experience))
        return vacancy
