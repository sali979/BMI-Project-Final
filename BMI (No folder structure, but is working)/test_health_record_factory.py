from health_record import HealthRecord, HealthRecordFactory

def test_can_create_valid_health_record():
    # arrange
    hr = HealthRecordFactory.make_health_record('test', 50, 150, "F", "01/01/1980", 10.2)
    # act 
    # assert
    assert isinstance(hr, HealthRecord)
