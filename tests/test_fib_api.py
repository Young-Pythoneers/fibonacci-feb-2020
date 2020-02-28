import pytest
from flask import url_for

from fibonaci.fib_api import app


@pytest.fixture
def client():
    with app.app.test_client() as client:
        yield client


def test_app(client):
    rv = client.get("/")
    assert rv.status_code == 200


def test_single_value(client):
    rv = client.get("/api/single_value?n=20")
    assert rv.status_code == 200


def test_mul_values(client):
    rv = client.get("/api/mul_values?n=20")
    assert rv.status_code == 200


def test_mul_values_max(client):
    rv = client.get("/api/mul_values_max?n=20")
    assert rv.status_code == 200
