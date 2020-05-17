from datetime import date, datetime
from unittest import TestCase
from uuid import uuid4

from costello.domainmodel.suspected_case import SuspectedCase


class TestSuspectedCase(TestCase):
    def test_open_and_close(self):
        # Open case.
        person_id = uuid4()
        case = SuspectedCase.open(case_id=uuid4(), person_id=person_id, details={})
        self.assertEqual(case.person_id, person_id)
        self.assertTrue(case.is_open)

        # Close case.
        case.close()
        self.assertFalse(case.is_open)

    def test_record_test_result(self):
        person_id = uuid4()
        case = SuspectedCase.open(case_id=uuid4(), person_id=person_id, details={})

        # Positive test.
        case.record_test_result(type="PCR", date=date(2020, 4, 1), result="positive")
        self.assertEqual(len(case.test_results), 1)
        self.assertEqual(case.test_results[0]["type"], "PCR")
        self.assertEqual(case.test_results[0]["date"], date(2020, 4, 1))
        self.assertEqual(case.test_results[0]["result"], "positive")

        # Negative test.
        case.record_test_result(type="PCR", date=date(2020, 4, 8), result="negative")
        self.assertEqual(len(case.test_results), 2)
        self.assertEqual(case.test_results[1]["type"], "PCR")
        self.assertEqual(case.test_results[1]["date"], date(2020, 4, 8))
        self.assertEqual(case.test_results[1]["result"], "negative")

    def test_record_symptoms(self):
        person_id = uuid4()
        case = SuspectedCase.open(case_id=uuid4(), person_id=person_id, details={})

        # Record cough.
        case.record_symptoms(details={"cough": True}, date=date(2020, 4, 1))
        self.assertEqual(len(case.symptoms), 1)

        # Record cough and temperature.
        case.record_symptoms(
            details={"cough": True, "temperature": True}, date=date(2020, 4, 2)
        )
        self.assertEqual(len(case.symptoms), 2)

    def test_record_contact_event(self):
        person_id = uuid4()
        case = SuspectedCase.open(case_id=uuid4(), person_id=person_id, details={})

        # Record contact event.
        case.record_contact_event(
            details={"telephone_number": "0123456789"},
            date=datetime(2020, 4, 1, 10, 30, 0),
        )

    def test_record_use_of_shared_space(self):
        person_id = uuid4()
        case = SuspectedCase.open(case_id=uuid4(), person_id=person_id, details={})

        # Went on a bus.
        shared_space_id = uuid4()
        case.record_use_of_shared_space(
            details={"shared_space_id": shared_space_id},
            date=datetime(2020, 4, 1, 10, 30, 0),
        )
        self.assertEqual(len(case.uses_of_shared_space), 1)
