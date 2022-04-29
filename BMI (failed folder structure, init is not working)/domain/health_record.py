from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
from typing import Type, Optional, List, Set
#from service.bmi_calc import bmi_category, bmi_evaluation, bmi_score

class NoBMIScore(Exception):
    pass


def allocate(urecord: UserRecord, hrecords: List[HealthRecord]) -> str:
    pass
    # try:
    #     record = next(b for b in sorted(hrecords) if b.can_allocate(urecord))
    #     record.allocate(urecord)
    #     return record.username
    # except StopIteration:
    #     raise NoBMIScore(f"No BMI for user {urecord.username}")


@dataclass(unsafe_hash=True)
class UserRecord:
    username: str
    category: str
    bmi: float

class HealthRecordFactory:

    def make_health_record(username: str, height: float, weight: float, gender, date_of_birth: date, bmi: float):
        #userid is user's id number
        if username is None:
            raise ValueError("Must include a username")
        # height in inches
        if height <= 0:
            raise TypeError
        # weight in pounds:
        if weight <= 0:
            raise TypeError
        # M or F
        allowed_genders = ['M','F']
        if gender not in allowed_genders:
            raise TypeError
        # any valid date string that can be parsed by python's datetime library - MM/DD/YYYY
        if datetime.strptime(date_of_birth, "%m/%d/%Y") is None:
            raise TypeError
        # bmi score
        if bmi <= 0:
            raise TypeError

        return HealthRecord(username, height, weight, gender, date_of_birth, bmi)


class HealthRecord:
    
    def __init__(self, username: str, height: float, weight: float, gender, date_of_birth: date, bmi: float):
        self.username = username  # username is a string
        self.height = height  # height in inches
        self.weight = weight  # weight in pounds:
        self.gender = gender  # M or F
        self.date_of_birth = date_of_birth # expecting a python date
        self.bmi = bmi # bmi score
        self._allocations = set()

    def __str__(self) -> str:
        return f"h: {self.height} inches and w: {self.weight} pounds"

    def __hash__(self):
        return hash(self.username)

    def __eq__(self, other):
        if not isinstance(other, HealthRecord):
            return False
        return other.username == self.username

    def __gt__(self, other):
        if self.date_of_birth is None:
            return False
        if other.date_of_birth is None:
            return True
        return self.date_of_birth > other.date_of_birth

    def allocate(self, urecord: UserRecord):
        if self.can_allocate(urecord):
            self._allocations.add(urecord)

    def deallocate(self, urecord: UserRecord):
        if urecord in self._allocations:
            self._allocations.remove(urecord)

    @property
    def allocated_bmiscore(self) -> float:
        return sum(urecord.bmi_score for urecord in self._allocations)

    @property
    def available_bmiscore(self) -> float:
        return self.bmi - self.allocated_bmiscore

    def can_allocate(self, urecord: UserRecord) -> bool:
        return self.bmi == urecord.bmi and self.available_bmiscore >= urecord.category