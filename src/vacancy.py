import json


class Vacancy():
    """Класс для создание экземпляра класса для работы с вакансиями"""
    def __init__(self, id, name, url, area, salary_from, salary_to, requirements, employer_id):
        self.id = id
        self.name = name
        self.url = url
        self.area = area
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirements = requirements
        self.employer_id = employer_id

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.url}, {self.employer})"

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f'Наименование вакансии: {self.name}\nРаботодатель: {self.employer}\nСсылка на вакансию:' \
               f' {self.url}\nОписание вакансии: {self.requirements}\nМесто работы: {self.area}\nЗарплата:' \
               f' {self.salary_to}\n'

    def __gt__(self, other):
        return self.salary_to > other.salary_to

    def dict_vacancy(self):
        vacancy = []
        vacancy.append(self.id)
        vacancy.append(self.name)
        vacancy.append(self.url)
        vacancy.append(self.area)
        vacancy.append(self.salary_from)
        vacancy.append(self.salary_to)
        vacancy.append(self.requirements)
        vacancy.append(self.employer_id)

        return vacancy


