import domain.health_record
from datetime import date


def test_UserRecord_mapper_can_load_records(session):
    session.execute(
        "INSERT INTO user_records (username, category, bmi) VALUES "
        '("test1", "obese", 32),'
        '("test1", "obese", 31),'
        '("test2", "underweight", 17)'
    )
    expected = [
        health_record.UserRecord("test1", "obese", 32),
        health_record.UserRecord("test1", "obese", 31),
        health_record.UserRecord("test2", "underweight", 17),
    ]
    assert session.query(health_record.UserRecord).all() == expected


def test_UserRecord_mapper_can_save_user_records(session):
    new_urec = health_record.UserRecord("test1", "obese", 32)
    session.add(new_urec)
    session.commit()

    rows = list(session.execute('SELECT username, category, bmi FROM "user_records"'))
    assert rows == [("test1", "obese", 32)]


def test_retrieving_health_records(session):
    session.execute(
        "INSERT INTO health_records (username, height, weight, gender, date_of_birth, bmi)"
        ' VALUES ("test1", 50.0, 150.0, "F", "01/01/1980", 10.2)'
    )
    session.execute(
        "INSERT INTO health_records (username, height, weight, gender, date_of_birth, bmi)"
        ' VALUES ("test2", 70.0, 170.0, "F", "02/02/1982", 12.2)'
    )
    expected = [
        health_record.HealthRecord("test1", 50.0, 150.0, "F", "01/01/1980", 10.2),
        health_record.HealthRecord("test2", 70.0, 170.0, "F", "02/02/1982", 12.2),
    ]

    assert session.query(health_record.HealthRecord).all() == expected


def test_saving_health_records(session):
    hrecord = health_record.HealthRecord("test1", 50.0, 150.0, "F", "01/01/1980", 10.2)
    session.add(hrecord)
    session.commit()
    rows = session.execute(
        'SELECT username, height, weight, gender, date_of_birth, bmi FROM "health_records"'
    )
    assert list(rows) == [("test1", 50.0, 150.0, "F", "01/01/1980", 10.2)]


# def test_saving_allocations(session):
#     hrecord = health_record.HealthRecord(("test1", 50.0, 150.0, "F", "01/01/1980", 10.2))
#     urecord = health_record.HealthRecord("test2", 70.0, 170.0, "F", "02/02/1982", 12.2)
#     # hrecord.allocate(urecord)
#     session.add(hrecord)
#     session.commit()
#     rows = list(session.execute('SELECT healthrecord_id FROM "allocations"'))
#     assert rows == [(hrecord.id, urecord.id)]


def test_retrieving_allocations(session):
    session.execute(
        'INSERT INTO user_records (username, category, bmi) VALUES ("test1", "obese", 32)'
    )
    [[userec]] = session.execute(
        "SELECT id FROM user_records WHERE username=:username AND bmi=:bmi",
        dict(username="test1", bmi=32),
    )
    session.execute(
        "INSERT INTO health_records (username, height, weight, gender, date_of_birth, bmi)"
        ' VALUES ("test1", 50.0, 150.0, "F", "01/01/1980", 32)'
    )
    [[hearec]] = session.execute(
        "SELECT id from domain.health_records WHERE username=:username AND bmi=:bmi",
        dict(username="test1", bmi=32),
    )
    session.execute(
        "INSERT INTO allocations (user_id, healthrecord_id) VALUES (:userec, :hearec)",
        dict(userec=userec, hearec=hearec),
    )

    hrecord = session.query(health_record.HealthRecord).one()

    assert hrecord._allocations == {health_record.UserRecord("test1", "obese", 32)}
