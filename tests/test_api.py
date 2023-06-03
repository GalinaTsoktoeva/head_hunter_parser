def test_head_hunter(api_head_hunter):
    assert api_head_hunter.name == "Head hunter"
    assert api_head_hunter.area == 1

def test_get_employers_vacancies(api_head_hunter):
    data = api_head_hunter.get_employers_vacancies()
    assert len(data) == 10

def test_get_vacancies(api_head_hunter, employee_id=1740):
    vacancy = api_head_hunter.get_vacancies(employee_id=1740)
    assert len(vacancy) == 500


    #api_head_hunter.get_vacancies("Python")
    #emp = api_head_hunter.get_employers()
    #print(*emp)
    #db = config()
    #db_manager.create_database('hh', db)
    #print(emp)
    #print(emp)
    #dict_res = db_manager.get_vacancies_with_keyword('linux')
    #print(dict_res)
    #db_manager.insert_employers_db(emp)
    #vac = api_head_hunter.get_vacancies(employee_id=1740)
    #db_manager.insert_vacancies_db(emp[0]['vacancies'])
    #print(vac)
