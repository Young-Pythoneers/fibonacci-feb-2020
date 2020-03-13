import os
import sqlite3

import pytest

import fibonaci
import tests
from fibonaci.build_database import create_new_database
from fibonaci.fib_api import create_app
from fibonaci.models import Fibonacci, FibSchema
from tests.config_for_tests import db


@pytest.fixture
def app():
    return create_app()


def test_app(client):
    rv = client.get("/")
    assert rv.status_code == 200


def test_for_index(client):
    rv = client.get("api/fibonacci/for-index?n=20")
    assert rv.status_code == 200
    assert rv.json == 6765


def test_up_to_including_index(client):
    rv = client.get("/api/fibonacci/up-to-including-index?n=8")
    assert rv.status_code == 200
    assert rv.json == [0, 1, 1, 2, 3, 5, 8, 13, 21]


def test_up_to_value(client):
    rv = client.get("/api/fibonacci/up-to-value?n=20")
    assert rv.status_code == 200
    assert rv.json == [0, 1, 1, 2, 3, 5, 8, 13]


def test_config_import():
    from tests.config_for_tests import db
    assert True


def test_monkeypatch(monkeypatch):
    monkeypatch.setattr(fibonaci, "config", tests.config_for_tests)
    assert True


def test_database_creation(monkeypatch):
    monkeypatch.setattr(fibonaci, "config", tests.config_for_tests)
    database_name = "fibonacci_database_test.db"
    create_new_database(database_name=database_name)
    # os.remove('../fibonaci/'+ database_name)
    assert True


def test_database_insertion(monkeypatch):
    monkeypatch.setattr(fibonaci, "config", tests.config_for_tests)
    database_name = "fibonacci_database_test.db"
    to_be_inserted_value = "1234"
    to_be_inserted_index = 987
    create_new_database(database_name=database_name)

    fib_value = Fibonacci(an_index=to_be_inserted_index, a_value=to_be_inserted_value)
    db.session.add(fib_value)
    db.session.commit()

    conn = sqlite3.connect(database_name)
    cur = conn.cursor()
    cur.execute(
        f"SELECT a_value FROM fibonacci where an_index is {to_be_inserted_index}"
    )
    query_result = cur.fetchall()
    to_be_returned_value = query_result[0][0]
    conn.close()
    # os.remove(database_name)
    assert to_be_returned_value == to_be_inserted_value


def test_database_integration():
    conn = sqlite3.connect("../fibonaci/fibonacci_database.db")
    cur = conn.cursor()
    cur.execute(f"SELECT a_value FROM fibonacci where an_index is {20}")
    record = cur.fetchall()
    conn.close()
    assert record[0][0] == "6765"
