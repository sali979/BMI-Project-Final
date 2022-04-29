from datetime import date, datetime
import abc
import domain.health_record
import orm

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, record: domain.health_record.HealthRecord):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, username) -> domain.health_record.HealthRecord:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, record):
        self.session.add(record)

    def get(self, username):
        return self.session.query(domain.health_record.HealthRecord).filter_by(username=username).one()

    def list(self):
        return self.session.query(domain.health_record.HealthRecord).all()
