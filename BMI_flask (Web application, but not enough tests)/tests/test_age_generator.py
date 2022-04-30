from bmi.record import Record


def create_record() -> Record:
    return Record(50, 150, 1, 'M', "2000-03-20", 20)


def test_age():
    record = create_record()
    assert record.age > 0
