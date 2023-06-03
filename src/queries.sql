-- """ получает список всех компаний и количество вакансий у каждой компании"""
select employees.name, count(*)
from employees left join vacancies using(employee_id)
group by employees.name

--"""получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
select employees.name, vacancies.name, salary_to, salary_from, vacancies.url
from vacancies  left join employees using(employee_id)

--получает среднюю зарплату по вакансиям.
select (avg(salary_to) + avg(salary_from))/2
from vacancies
where salary_to !=0 or salary_from !=0

--получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
select name, salary_to, salary_from
from vacancies
group by name, salary_to, salary_from
having (select (avg(salary_to) + avg(salary_from))/2  from vacancies  where salary_to !=0 or salary_from !=0)  < salary_to
or (select (avg(salary_to) + avg(salary_from))/2  from vacancies  where salary_to !=0 or salary_from !=0) < salary_from


--"""получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”"""
select name, requirements
from vacancies
where name like {keyword} or requirements like {keyword}
