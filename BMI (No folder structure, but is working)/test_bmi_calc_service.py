import pytest
from health_record import HealthRecord, HealthRecordFactory
from bmi_calc import bmi_score

@pytest.fixture
def health_rec() -> HealthRecord:
    return HealthRecordFactory.make_health_record('test', 50, 150, "F", "01/01/1980", 40.4)

def test_bmi_service_bmi_score():
    # arrange
    hr = HealthRecordFactory.make_health_record('test', 15, 15, "F", "01/01/1980", 10.2)
    print(hr)
    # act
    score = bmi_score(hr.height, hr.weight)

    # assert
    assert score > 0

def test_bmi_service_bmi_score():
    # arrange
    hr2 = HealthRecordFactory.make_health_record('test1', 50, 150, "M", "02/02/1982", 20)
    print(hr2)
    # act
    score = bmi_score(hr2.height, hr2.weight)

    # assert
    assert score > 0