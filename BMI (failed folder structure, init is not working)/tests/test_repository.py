# pylint: disable=protected-access
from datetime import date
import domain.health_record
import repository


def test_repository_can_save_a_health_record(session):
    record = health_record.HealthRecord('test', 50, 150, "F", "01/01/1980", 10.2)

    repo = repository.SqlAlchemyRepository(session)
    repo.add(record)
    session.commit()

    rows = session.execute(
        'SELECT username, height, weight, gender, date_of_birth, bmi FROM "health_records"'
    )
    assert list(rows) == [('test', 50.0, 150.0, "F", "01/01/1980", 10.2)]


def insert_user_record(session):
    session.execute(
        "INSERT INTO user_records (username, category, bmi)"
        ' VALUES ("test1", "healthy", 26)'
    )
    [[user_id]] = session.execute(
        "SELECT id FROM user_records WHERE username=:username AND category=:category",
        dict(username="test1", category="healthy"),
    )
    return user_id


def insert_record(session, healthrecord_id):
    session.execute(
        "INSERT INTO health_records (username, height, weight, gender, date_of_birth, bmi)"
        ' VALUES (:healthrecord_id, 50, 150, "F", "01/01/1980", 10.2)',
        dict(healthrecord_id=healthrecord_id),
    )
    [[healthrecord_id]] = session.execute(
        'SELECT id from domain.health_records WHERE username=:healthrecord_id AND category="healthy"',
        dict(healthrecord_id=healthrecord_id),
    )
    return healthrecord_id


def insert_allocation(session, user_id, healthrecord_id):
    session.execute(
        "INSERT INTO allocations (user_id, healthrecord_id)"
        " VALUES (:user_id, :healthrecord_id)",
        dict(user_id=user_id, healthrecord_id=healthrecord_id),
    )


# def test_repository_can_retrieve_health_record_with_allocations(session):
#     user_id = insert_user_record(session)
#     hrecord_id = insert_record(session, "test1")
#     insert_record(session, "test2")
#     insert_allocation(session, user_id, hrecord_id)

#     repo = repository.SqlRepository(session)
#     retrieved = repo.get("test1")

#     expected = health_record.HealthRecord("test1", 50, 150, "F", "01/01/1980", 10.2)
#     assert retrieved == expected  # Batch.__eq__ only compares username
#     assert retrieved.username == expected.username
#     assert retrieved.bmi == expected.bmi
#     assert retrieved._allocations == {
#         health_record.UserRecord("test1", "healthy", 10.2),
#    }


def get_allocations(session, batchid):
    rows = list(
        session.execute(
            "SELECT username"
            " FROM allocations"
            " JOIN user_records ON allocations.user_id = user_records.id"
            " JOIN health_records ON allocations.healthrecord_id = health_records.id"
            " WHERE health_records.username = :batchid",
            dict(batchid=batchid),
        )
    )
    return {row[0] for row in rows}


# def test_updating_health_record(session):
#     test1 = health_record.UserRecord("test1", "healthy", "27")
#     test2 = health_record.UserRecord("test2", "underweight", "17")
#     record = health_record.HealthRecord("test1", 170, 65, "M", "01/01/1990", 27)
#     record.allocate(test1)

#     repo = repository.SqlAlchemyRepository(session)
#     repo.add(record)
#     session.commit()

#     record.allocate(test2)
#     repo.add(record)
#     session.commit()

#     assert get_allocations(session, "test1") == {"test1", "test2"}
