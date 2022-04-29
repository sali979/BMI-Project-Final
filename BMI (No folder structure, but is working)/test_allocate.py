from datetime import date, timedelta
import pytest
from health_record import allocate, UserRecord, HealthRecord, NoBMIScore
from bmi_calc import bmi_category, bmi_score, bmi_evaluation

# today = date.today()
# tomorrow = today + timedelta(days=1)
# later = tomorrow + timedelta(days=10)

def test_correctly_evaluate_healthy():
    healthy = HealthRecord("test", 170, 65, "M", "01/01/1990", 20.14)
    testrecord = HealthRecord("t", 180, 70, "M", "01/01/1991", 10)

    allocate(testrecord, [healthy])

    assert healthy.available_bmiscore == 20.14

def test_correctly_evaluate_extremely_underweight():
    extremely_underweight = HealthRecord("test", 170, 30, "M", "01/01/1990", 9.59)
    testrecord = HealthRecord("t", 180, 70, "M", "01/01/1991", 10)

    allocate(testrecord, [extremely_underweight])

    assert extremely_underweight.available_bmiscore == 9.59

def test_correctly_evaluate_underweight():
    underweight = HealthRecord("test", 170, 55, "M", "01/01/1990", 17.58)
    testrecord = HealthRecord("t", 180, 70, "M", "01/01/1991", 10)

    allocate(testrecord, [underweight])

    assert underweight.available_bmiscore == 17.58

def test_correctly_evaluate_overweight():
    overweight = HealthRecord("test", 170, 85, "M", "01/01/1990", 27.17)
    testrecord = HealthRecord("t", 180, 70, "M", "01/01/1991", 10)

    allocate(testrecord, [overweight])

    assert overweight.available_bmiscore == 27.17

def test_correctly_evaluate_obese():
    obese = HealthRecord("test", 170, 95, "M", "01/01/1990", 30.37)
    testrecord = HealthRecord("t", 180, 70, "M", "01/01/1991", 10)

    allocate(testrecord, [obese])

    assert obese.available_bmiscore == 30.37


# def test_prefers_current_stock_batches_to_shipments():
#     in_stock_batch = Batch("in-stock-batch", "RETRO-CLOCK", 100, eta=None)
#     shipment_batch = Batch("shipment-batch", "RETRO-CLOCK", 100, eta=tomorrow)
#     urecord = UserRecord("oref", "RETRO-CLOCK", 10)

#     allocate(urecord, [in_stock_batch, shipment_batch])

#     assert in_stock_batch.available_quantity == 90
#     assert shipment_batch.available_quantity == 100


# def test_prefers_earlier_batches():
#     earliest = Batch("speedy-batch", "MINIMALIST-SPOON", 100, eta=today)
#     medium = Batch("normal-batch", "MINIMALIST-SPOON", 100, eta=tomorrow)
#     latest = Batch("slow-batch", "MINIMALIST-SPOON", 100, eta=later)
#     urecord = UserRecord("order1", "MINIMALIST-SPOON", 10)

#     allocate(urecord, [medium, earliest, latest])

#     assert earliest.available_quantity == 90
#     assert medium.available_quantity == 100
#     assert latest.available_quantity == 100


# def test_returns_allocated_batch_ref():
#     in_stock_batch = Batch("in-stock-batch-ref", "HIGHBROW-POSTER", 100, eta=None)
#     shipment_batch = Batch("shipment-batch-ref", "HIGHBROW-POSTER", 100, eta=tomorrow)
#     urecord = UserRecord("oref", "HIGHBROW-POSTER", 10)
#     allocation = allocate(urecord, [in_stock_batch, shipment_batch])
#     assert allocation == in_stock_batch.reference


# def test_raises_out_of_stock_exception_if_cannot_allocate():
#     batch = Batch("batch1", "SMALL-FORK", 10, eta=today)
#     allocate(UserRecord("order1", "SMALL-FORK", 10), [batch])

#     with pytest.raises(OutOfStock, match="SMALL-FORK"):
#         allocate(UserRecord("order2", "SMALL-FORK", 1), [batch])
