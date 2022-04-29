from bmi.record import Record
from services.bmi_calculator import *


# N/B fixtures are not meant to bea called directly
def create_record() -> Record:
    return Record(50, 150, 1, 'M', "2000-03-21", 20)


def test_bmi_service_score():
    record = create_record()
    score = bmi_score(record.height, record.weight)
    assert score > 0
