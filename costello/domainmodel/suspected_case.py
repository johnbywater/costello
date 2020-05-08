from datetime import date
from typing import Any

from eventsourcing.domain.model.aggregate import BaseAggregateRoot


class SuspectedCase(BaseAggregateRoot):
    __subclassevents__ = True

    def __init__(self, *, person_id, **kwargs: Any):
        super().__init__(**kwargs)
        self.symptoms = []
        self.person_id = person_id
        self.test_results = []
        self.is_closed = False

    @classmethod
    def open(cls, *, person_id) -> "SuspectedCase":
        return cls.__create__(person_id=person_id)

    def close(self):
        self.__trigger_event__(SuspectedCase.Closed)

    class Closed(BaseAggregateRoot.Event):
        def mutate(self, obj: "SuspectedCase") -> None:
            obj.is_closed = True

    def record_test_result(self, *, type: str, date: date, result: str):
        self.__trigger_event__(SuspectedCase.TestResultRecorded, type=type, date=date, result=result)

    class TestResultRecorded(BaseAggregateRoot.Event):
        @property
        def type(self):
            return self.__dict__['type']

        @property
        def date(self):
            return self.__dict__['date']

        @property
        def result(self):
            return self.__dict__['result']

        def mutate(self, obj: "SuspectedCase") -> None:
            obj.test_results.append({
                "type": self.type,
                "date": self.date,
                "result": self.result,
            })

    @property
    def has_been_tested(self):
        return bool(len(self.test_results))

    def record_symptoms(self, symptoms: tuple, date: date):
        self.__trigger_event__(SuspectedCase.SymptomsRecorded, symptoms=symptoms, date=date)

    class SymptomsRecorded(BaseAggregateRoot.Event):
        @property
        def symptoms(self):
            return self.__dict__['symptoms']

        @property
        def date(self):
            return self.__dict__['date']

        def mutate(self, obj: "SuspectedCase"):
            obj.symptoms.append({
                "symptoms": self.symptoms,
                "date": self.date
            })
