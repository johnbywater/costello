from datetime import datetime
from unittest.case import TestCase

from eventsourcing.system.runner import SingleThreadedRunner

from costello.application import Application
from costello.system.definition import CostelloSystem
from costello.system.notifications import Notifications
from costello.system.commands import Commands


class TestBankAccountSystem(TestCase):
    def setUp(self) -> None:
        # Run the system with single threaded runner.
        self.runner = SingleThreadedRunner(CostelloSystem(infrastructure_class=None))
        self.runner.start()
        self.commands: Commands = self.runner.get(Commands)
        self.app: Application = self.runner.get(Application)
        self.notifications: Notifications = self.runner.get(Notifications)

    def tearDown(self) -> None:
        del self.notifications
        del self.app
        del self.commands
        self.runner.close()
        del self.runner

    def test_open_and_close_case(self):
        # Open case.
        case_id = self.commands.open_case()

        # Check case is open.
        self.assertTrue(self.app.is_case_open(case_id))

        # Close case.
        self.commands.close_case(case_id=case_id)

        # Check case is closed.
        self.assertFalse(self.app.is_case_open(case_id))

        # Record contact event.
        self.commands.record_contact_event(
            case_id=case_id,
            details={"telephone_number": "0123456789"},
            date=datetime(2020, 4, 1, 10, 30, 0),
        )
