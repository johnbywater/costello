from datetime import date
from typing import Dict
from uuid import UUID

from eventsourcing.application.command import CommandProcess
from eventsourcing.domain.model.command import Command

class SystemCommand(Command):
    __subclassevents__ = True


class OpenCase(SystemCommand):
    pass


class CloseCase(SystemCommand):
    def __init__(self, *, case_id, **kwargs):
        super(CloseCase, self).__init__(**kwargs)
        self.case_id = case_id


class RecordContactEvent(SystemCommand):
    def __init__(self, *, case_id, details, date, **kwargs):
        super(RecordContactEvent, self).__init__(**kwargs)
        self.case_id = case_id
        self.details = details
        self.date = date


class Commands(CommandProcess):
    def open_case(self) -> UUID:
        cmd = OpenCase.__create__()
        self.save(cmd)
        return cmd.id

    def close_case(self, case_id) -> None:
        cmd = CloseCase.__create__(case_id=case_id)
        self.save(cmd)

    def record_contact_event(self, case_id, details: Dict, date: date) -> None:
        cmd = RecordContactEvent.__create__(case_id=case_id, details=details, date=date)
        self.save(cmd)
