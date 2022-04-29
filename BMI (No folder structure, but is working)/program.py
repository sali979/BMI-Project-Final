from bmi.health_record import HealthRecord, HealthRecordFactory

def main():
    hr = HealthRecordFactory.make_health_record(15, 15, "F", "01/01/1980")
    print(hr)

if __name__ == "__main__":
    main()