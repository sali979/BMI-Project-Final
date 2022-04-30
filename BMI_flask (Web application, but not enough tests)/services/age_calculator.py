from datetime import date


def calculate_age(born):
    born = reformat_date(born)

    today = date.today()
    age = int(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))
    print("Age: ", age)

    return age


def reformat_date(dob):
    dob = dob.split('-')
    year = int(dob[0])
    month = int(dob[1])
    day = int(dob[2])

    date_obj = date(year, month, day)
    return date_obj
