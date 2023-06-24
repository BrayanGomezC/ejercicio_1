import pytest
from ejercicio1 import sum, es_mayor_que, login

def test_sum():
    assert sum(3,8)==11
    assert sum(11,2)==33
    assert sum(5,14)==18
    
def test_es_mayor_que():
    assert es_mayor_que(30,11)

@pytest.mark.parametrize(
    "in_x,in_y,esperado",
    [(3,4,7),
    (sum(2,1),4,7),
    (3,sum(3,1),7),
    (3,4,sum(2,5)),]
)

def test_sum_param(in_x,in_y,esperado):
    assert sum(in_x,in_y)==esperado 
    
def test_login_pass():
    login_passes=login("metologia", "/710011C")
    assert login_passes
    
def test_login_fail():
    login_fails=login("metologia", "/710011M")
    assert not login_fails