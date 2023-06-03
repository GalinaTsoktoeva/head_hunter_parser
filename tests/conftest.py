import pytest
from src.API import HeadHunterAPI
from src.DBManager import DBManager

@pytest.fixture()
def api_head_hunter():
    api = HeadHunterAPI(1)
    return api

@pytest.fixture()
def db_manager():
    return DBManager()