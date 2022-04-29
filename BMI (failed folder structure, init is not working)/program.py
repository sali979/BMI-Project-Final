from domain.health_record import HealthRecord, HealthRecordFactory

def main():
    hr = HealthRecordFactory.make_health_record("test999" 175, 60, "M", "03/03/1990, 27.3")
    print(hr)

if __name__ == "__main__":
    main()