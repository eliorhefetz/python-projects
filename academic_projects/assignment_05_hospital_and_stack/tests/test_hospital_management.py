import unittest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from hospital_management import Patient, Doctor, Hospital


class TestHospitalManagement(unittest.TestCase):
    def test_assign_and_treat_highest_priority(self):
        hospital = Hospital("General")
        doctor = Doctor(1, "Dr. Levi")
        patient_1 = Patient(1, "Noa", "Flu", 2)
        patient_2 = Patient(2, "Dan", "Injury", 5)

        hospital.addDoctor(doctor)
        hospital.addPatient(patient_1)
        hospital.addPatient(patient_2)

        self.assertTrue(hospital.assignPatientToDoctor(1, 1))
        self.assertTrue(hospital.assignPatientToDoctor(2, 1))

        treated = hospital.treatNextPatient(1)
        self.assertEqual(treated.patient_name, "Dan")

    def test_patient_statistics(self):
        hospital = Hospital("General")
        patient_1 = Patient(1, "Noa", "Flu", 2)
        patient_2 = Patient(2, "Dan", "Injury", 5)

        hospital.addPatient(patient_1)
        hospital.addPatient(patient_2)

        statistics = hospital.patientStatistics()

        self.assertEqual(statistics[2], ["Noa"])
        self.assertEqual(statistics[5], ["Dan"])


if __name__ == "__main__":
    unittest.main()
