from datetime import date
from typing import Dict
from uuid import UUID

from eventsourcing.application.decorators import applicationpolicy
from eventsourcing.application.process import ProcessApplication
from eventsourcing.exceptions import RepositoryKeyError

from costello.domainmodel.suspected_case import SuspectedCase
from costello.system.commands import CloseCase, OpenCase


class Application(ProcessApplication):
    def open_case(self, *, case_id: UUID, person_id: UUID = None, details: Dict=None) -> UUID:
        case = SuspectedCase.open(case_id=case_id, person_id=person_id, details=details)
        self.save(case)
        return case.id

    def is_case_open(self, case_id: UUID) -> bool:
        try:
            case = self.get_case(case_id)
        except RepositoryKeyError:
            return False
        else:
            return case.is_open

    def get_case(self, case_id: UUID) -> SuspectedCase:
        repository = self.repository
        return self._get_case(repository, case_id)

    def _get_case(self, repository, case_id) -> SuspectedCase:
        case = repository[case_id]
        assert isinstance(case, SuspectedCase)
        return case

    def close_case(self, case_id):
        case = self.get_case(case_id)
        case.close()
        self.save(case)

    def record_symptoms(self, case_id: UUID, symptoms: Dict, date: date):
        case = self.get_case(case_id)
        case.record_symptoms(details=symptoms, date=date)

    def record_contact_event(self, case_id, details: Dict, date: date) -> UUID:
        case = self.get_case(case_id)
        return case.record_contact_event(details=details, date=date)

    @applicationpolicy
    def policy(self, repository, event):
        pass

    @policy.register(OpenCase.Created)
    def _(self, repository, event):
        self.open_case(
            case_id=event.originator_id,

        )

    @policy.register(CloseCase.Created)
    def _(self, repository, event):
        self.close_case(
            case_id=event.case_id,
        )
