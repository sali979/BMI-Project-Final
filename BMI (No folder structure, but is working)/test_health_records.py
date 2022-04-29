from datetime import date
from health_record import HealthRecord, UserRecord


def test_allocating_to_a_records_with_bmi():
    record = HealthRecord("test2", 70.0, 170.0, "F", "02/02/1982", 12.2)
    urecord = UserRecord("test1", "obese", 32)

    record.allocate(urecord)

    assert record.available_bmiscore == 12.2


def make_hrecord_and_urecord(username, hrec_bmi, urec_bmi):
    return (
        HealthRecord("test2", 70.0, 170.0, "F", "02/02/1982", 12.2),
        UserRecord("test1", "obese", 32),
    )


# def test_can_allocate_if_available_greater_than_required():
#     large_batch, small_line = make_hrecord_and_urecord("test1", "obese", 32)
#     assert large_batch.can_allocate(small_line)


# def test_cannot_allocate_if_available_smaller_than_required():
#     small_batch, large_line = make_hrecord_and_urecord("test1", "obese", 32)
#     assert small_batch.can_allocate(large_line) is False


# def test_can_allocate_if_available_equal_to_required():
#     record, urecord = make_hrecord_and_urecord("test1", "obese", 32)
#     assert record.can_allocate(urecord)


def test_cannot_allocate_if_bmi_do_not_match():
    record = HealthRecord("test2", 70.0, 170.0, "F", "02/02/1982", 12.2)
    different_sku_line = UserRecord("test1", "obese", 32)
    assert record.can_allocate(different_sku_line) is False


def test_allocation_is_idempotent():
    record, urecord = make_hrecord_and_urecord("test1", "obese", 12.2)
    record.allocate(urecord)
    record.allocate(urecord)
    assert record.available_bmiscore == 12.2


def test_deallocate():
    record, urecord = make_hrecord_and_urecord("test1", "obese", 12.2)
    record.allocate(urecord)
    record.deallocate(urecord)
    assert record.available_bmiscore == 12.2


def test_can_only_deallocate_allocated_lines():
    record, unallocated_line = make_hrecord_and_urecord("test1", "obese", 12.2)
    record.deallocate(unallocated_line)
    assert record.available_bmiscore == 12.2
