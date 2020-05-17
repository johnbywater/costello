from datetime import date, datetime
from typing import Any, Dict
from uuid import UUID, uuid4

from eventsourcing.domain.model.aggregate import BaseAggregateRoot


class SuspectedCase(BaseAggregateRoot):
    __subclassevents__ = True

    class Event(BaseAggregateRoot.Event):
        pass

    def __init__(self, *, person_id, details, **kwargs: Any):
        super().__init__(**kwargs)
        self.person_id = person_id
        self.details = details
        self.contact_events = []
        self.uses_of_shared_space = []
        self.symptoms = []
        self.test_results = []
        self.is_open = True

    @classmethod
    def open(cls, *, case_id, person_id, details) -> "SuspectedCase":
        return cls.__create__(
            event_class=cls.Opened,
            originator_id=case_id,
            person_id=person_id,
            details=details,
        )

    class Opened(BaseAggregateRoot.Created):
        pass

    def close(self):
        self.__trigger_event__(SuspectedCase.Closed)

    class Closed(Event):
        def mutate(self, obj: "SuspectedCase") -> None:
            obj.is_open = False

    def record_test_result(self, *, type: str, date: date, result: str):
        self.__trigger_event__(
            SuspectedCase.TestResultRecorded, type=type, date=date, result=result
        )

    class TestResultRecorded(BaseAggregateRoot.Event):
        @property
        def type(self):
            return self.__dict__["type"]

        @property
        def date(self):
            return self.__dict__["date"]

        @property
        def result(self):
            return self.__dict__["result"]

        def mutate(self, obj: "SuspectedCase") -> None:
            obj.test_results.append(
                {"type": self.type, "date": self.date, "result": self.result,}
            )

    @property
    def has_been_tested(self):
        return bool(len(self.test_results))

    def record_symptoms(self, details: Dict, date: date):
        self.__trigger_event__(
            SuspectedCase.SymptomsRecorded, details=details, date=date
        )

    class SymptomsRecorded(Event):
        @property
        def details(self):
            return self.__dict__["details"]

        @property
        def date(self):
            return self.__dict__["date"]

        def mutate(self, obj: "SuspectedCase"):
            obj.symptoms.append({"details": self.details, "date": self.date})

    def record_use_of_shared_space(self, details: Dict, date: date):
        self.__trigger_event__(
            SuspectedCase.UseOfSharedSpaceRecorded, details=details, date=date
        )

    class UseOfSharedSpaceRecorded(Event):
        @property
        def details(self):
            return self.__dict__["details"]

        @property
        def date(self):
            return self.__dict__["date"]

        def mutate(self, obj: "SuspectedCase") -> None:
            obj.uses_of_shared_space.append(
                {"details": self.details, "date": self.date,}
            )

    def record_contact_event(self, details: Dict, date: date) -> UUID:
        contact_event_id = uuid4()
        self.__trigger_event__(
            self.PersonContacted, details=details, date=date, contact_event_id=contact_event_id
        )
        return contact_event_id

    class PersonContacted(Event):
        @property
        def details(self):
            return self.__dict__["details"]

        @property
        def contact_event_id(self):
            return self.__dict__["contact_event_id"]

        def mutate(self, obj: "SuspectedCase"):
            obj.contact_events.append(
                {"details": self.details, "contact_event_id": self.contact_event_id,}
            )
