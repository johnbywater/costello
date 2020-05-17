from unittest.case import TestCase

from costello.domainmodel.disease import Disease


class TestDiseaseModel(TestCase):
    def test_register_disease(self):
        disease = Disease.__create__(name="COVID-19")
        disease.set_earliest_infectiousness_onset(days=1)
        disease.set_latest_symptom_onset(days=14)
