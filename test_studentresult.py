
from studentresult import calculate_result

def test_total():
    total, average, percentage = calculate_result(80, 90, 70)
    assert total == 240

def test_average():
    total, average, percentage = calculate_result(80, 90, 70)
    assert average == 80

def test_percentage():
    total, average, percentage = calculate_result(80, 90, 70)
    assert percentage == 80
