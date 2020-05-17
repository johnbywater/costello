from datetime import date
from unittest.case import TestCase
from uuid import uuid4

from eventsourcing.application.popo import PopoApplication

from costello.application import Application


class TestApplication(TestCase):
    def setUp(self) -> None:
        self.app = Application.mixin(PopoApplication)()

    def test_open_and_close_case(self):
        # Register suspected case of infection.
        person_id = uuid4()
        case_id = self.app.open_case(
            case_id=uuid4(), person_id=person_id, details={"telephone_number": "0123456789"}
        )

        # Check case is open.
        self.assertTrue(self.app.is_case_open(case_id))

        # Close case.
        self.app.close_case(case_id)

        # Check case is closed.
        self.assertFalse(self.app.is_case_open(case_id))

    def test_record_symptoms(self):
        # Register suspected case of infection.
        person_id = uuid4()
        case_id = self.app.open_case(
            case_id=uuid4(), person_id=person_id, details={"telephone_number": "0123456789"}
        )

        # Record details.
        self.app.record_symptoms(
            case_id, symptoms={"cough": True}, date=date(2020, 4, 1)
        )

    def test_record_contact_event(self):
        # Register suspected case of infection.
        person_id = uuid4()
        case_id = self.app.open_case(case_id=uuid4(), person_id=person_id, details={})

        # Record contact event.
        contact_event_id = self.app.record_contact_event(
            case_id, details={"telephone_number": "0123456789"}, date=date(2020, 3, 20)
        )
