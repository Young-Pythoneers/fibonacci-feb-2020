import pytest
#from mock import patch

from fibonaci.fib_api import app

def decode_byte(byte):
    conversion1 = ((byte).decode("ASCII")).replace('\n', '')
    conversion2 =  conversion1.replace(" ","")
    return conversion2


@pytest.fixture
def client():
    with app.app.test_client() as client:
        yield client


def test_app(client):
    rv = client.get("/")
    assert rv.status_code == 200



def test_for_index(client):
    rv = client.get("api/fibonacci/for_index?n=20")
    assert rv.status_code == 200

def test_for_index_answer(client):
    rv = client.get("api/fibonacci/for_index?n=20")
    assert int(rv.data) == 6765



def test_up_to_including_index(client):
    rv = client.get("/api/fibonacci/up-to-including-index?n=20")
    assert rv.status_code == 200

def test_up_to_including_index_answer(client):
    rv = client.get("api/fibonacci/up-to-including-index?n=8")
    rv2 = decode_byte(rv.data)
    assert rv2 == '[0,1,1,2,3,5,8,13,21]'



def test_up_to_value(client):
    rv = client.get("/api/fibonacci/up-to-value?n=20")
    assert rv.status_code == 200

def test_up_to_value_answer(client):
    rv = client.get("/api/fibonacci/up-to-value?n=20")
    rv2 = decode_byte(rv.data)
    assert rv2 == '[0,1,1,2,3,5,8,13]'



#@patch('urllib.urlopen')
#def test_foo(urlopen_mock):
#    urlopen_mock.return_value = MyUrlOpenMock()