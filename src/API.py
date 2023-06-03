from abc import ABC, abstractmethod
from src.vacancy import Vacancy
import requests
import json


class API(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def get_employers_vacancies(self):
        pass


class HeadHunterAPI(API):
    """класс для подключения к API Head  Hunter и получения информации от 10 работодателей по 500 вакансиям на каждого"""
    def __init__(self, area):
        self.name = "Head hunter"
        self.area = area
        self.url = 'https://api.hh.ru/'
        self.emp_id = [1740, 3529, 2180, 976931, 15478, 4181, 39305, 3776, 80, 84585]

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}')"

    def __str__(self):
        return f"{self.name}"

    def get_vacancies(self, employee_id, page=0, text=""):
        """Парсинг 500 вакансий с сайта Head Hunter"""
        vacancies_data = []

        for page_num in range(5): #5
            params = {
                #'text': text,
                'area': self.area,
                'page': page_num,
                'per_page': '100' #100
            }

            reguest = self.get_json_from_hh(params, "vacancies"+"?employer_id="+str(employee_id))
            parsed = json.loads(reguest.content)
            reguest.close()

            if parsed.get('items'):
                for item in parsed.get('items'):
                    if item:

                        new_vacancy = Vacancy(
                            id=int(item['id']),
                            name=item['name'],
                            url=item['alternate_url'],
                            area=item["area"]['name'],
                            salary_to=item['salary']['to'] if item['salary'] is not None else 0,
                            salary_from=item['salary']['from'] if item['salary'] is not None else 0,
                            requirements=item['snippet']['requirement'],
                            employer_id=int(item['employer']['id'])
                        )

                        new_vacancy_dict = new_vacancy.dict_vacancy()
                        vacancies_data.append(new_vacancy_dict)
        return vacancies_data

    def get_employers_vacancies(self):
        """Парсинг работодателей и вакансий с сайта Head Hunter"""
        data_total = []

        for i in self.emp_id:
            req = self.get_json_from_hh(query='employers/' + str(i))
            data = req.content.decode()
            req.close()
            jsObj = json.loads(data)

            try:
                employers = [int(jsObj['id']), jsObj['name'], jsObj['site_url'], jsObj['vacancies_url'], jsObj['area']['id'], jsObj['description']]
            except:
                print("Ошибка заполнения данных о работодателе")

            vacancies = self.get_vacancies(employee_id=i)
            data_total.append(
                {
                    'employers': employers,
                    'vacancies': vacancies
                }
            )

        return data_total

    def get_json_from_hh(self, params={}, query=""):
        """Отправляем GET запрос"""
        try:
            response = requests.get(self.url+query, params)
            return response
        except ConnectionError:
            print("Connection error")
        except requests.HTTPError:
            print('HTTP error')
        except TimeoutError:
            print('Timeout error')
        return {}