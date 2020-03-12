import pytest
import sqlite3

from fibonaci.fib_api import create_app


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


def test_database():
    conn = sqlite3.connect('../fibonaci/fibonacci_database.db')
    cur = conn.cursor()
    cur.execute(f'SELECT a_value FROM fibonacci where an_index is {20}')
    record = cur.fetchall()
    conn.close()
    assert record[0][0] == '6765'
