
from result import calculate_result

def test_total():
    assert calculate_result(80, 90, 70) == 240

def test_average():
    assert calculate_result(80, 90, 70) == 80

def test_percentage():
    assert calculate_result(80, 90, 70)== 80
