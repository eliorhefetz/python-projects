class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def size(self):
        return len(self.items)


class PriorityQueue(Queue):
    def __init__(self):
        super().__init__()

    def enqueue(self, patient):
        if self.is_empty():
            self.items.append(patient)
            return

        for index in range(self.size()):
            if self.items[index].severity < patient.severity:
                self.items.insert(index, patient)
                return

        self.items.append(patient)


class Patient:
    def __init__(self, patient_id, patient_name, illness_description, severity):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.illness_description = illness_description
        self.severity = severity

    def updatePriority(self, new_severity):
        self.severity = new_severity

    def __repr__(self):
        return (
            f"Patient ID: {self.patient_id}, "
            f"Name: {self.patient_name}, "
            f"Illness: {self.illness_description}, "
            f"Severity: {self.severity}"
        )


class Doctor:
    def __init__(self, doctor_id, doctor_name):
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.patients_queue = PriorityQueue()

    def addPatient(self, patient):
        self.patients_queue.enqueue(patient)

    def treatPatient(self):
        return self.patients_queue.dequeue()

    def __repr__(self):
        return (
            f"Doctor ID: {self.doctor_id}, "
            f"Name: {self.doctor_name}, "
            f"Patients in Queue: {self.patients_queue.size()}"
        )


class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.doctors_list = []
        self.patients_list = []

    def addDoctor(self, doctor):
        self.doctors_list.append(doctor)

    def addPatient(self, patient):
        self.patients_list.append(patient)

    def assignPatientToDoctor(self, patient_id, doctor_id):
        selected_patient = None
        selected_doctor = None

        for patient in self.patients_list:
            if patient.patient_id == patient_id:
                selected_patient = patient
                break

        for doctor in self.doctors_list:
            if doctor.doctor_id == doctor_id:
                selected_doctor = doctor
                break

        if selected_patient is None or selected_doctor is None:
            return False

        selected_doctor.addPatient(selected_patient)
        self.patients_list.remove(selected_patient)
        return True

    def treatNextPatient(self, doctor_id):
        for doctor in self.doctors_list:
            if doctor.doctor_id == doctor_id:
                return doctor.treatPatient()
        return None

    def patientStatistics(self):
        statistics = {}

        for patient in self.patients_list:
            if patient.severity not in statistics:
                statistics[patient.severity] = []
            statistics[patient.severity].append(patient.patient_name)

        for doctor in self.doctors_list:
            for patient in doctor.patients_queue.items:
                if patient.severity not in statistics:
                    statistics[patient.severity] = []
                statistics[patient.severity].append(patient.patient_name)

        return statistics

    def patientByPriority(self, severity):
        result = []

        for patient in self.patients_list:
            if patient.severity == severity:
                result.append(patient.patient_name)

        for doctor in self.doctors_list:
            for patient in doctor.patients_queue.items:
                if patient.severity == severity:
                    result.append(patient.patient_name)

        return result

    def allDoctors(self):
        sorted_doctors = sorted(
            self.doctors_list,
            key=lambda doctor: doctor.patients_queue.size(),
            reverse=True
        )

        result = []
        for doctor in sorted_doctors:
            result.append(doctor.doctor_name)

        return result

    def __repr__(self):
        return (
            f"Hospital Name: {self.hospital_name}, "
            f"Doctors: {len(self.doctors_list)}, "
            f"Waiting Patients: {len(self.patients_list)}"
        )


def print_header():
    print("\n" + "=" * 60)
    print("              HOSPITAL MANAGEMENT SYSTEM")
    print("=" * 60)


def print_menu():
    print("\nChoose an option:")
    print("1. Add Doctor")
    print("2. Add Patient")
    print("3. Assign Patient To Doctor")
    print("4. Treat Next Patient")
    print("5. Update Patient Priority")
    print("6. Show Patient Statistics")
    print("7. Show Patients By Priority")
    print("8. Show All Doctors")
    print("9. Exit")


def main():
    print_header()
    hospital_name = input("Enter hospital name: ").strip()
    hospital = Hospital(hospital_name)

    while True:
        print_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            try:
                doctor_id = int(input("Enter doctor ID: "))
                doctor_name = input("Enter doctor name: ").strip()
                doctor = Doctor(doctor_id, doctor_name)
                hospital.addDoctor(doctor)
                print("Doctor added successfully.")
            except ValueError:
                print("Invalid input.")

        elif choice == "2":
            try:
                patient_id = int(input("Enter patient ID: "))
                patient_name = input("Enter patient name: ").strip()
                illness_description = input("Enter illness description: ").strip()
                severity = int(input("Enter illness severity: "))
                patient = Patient(patient_id, patient_name, illness_description, severity)
                hospital.addPatient(patient)
                print("Patient added successfully.")
            except ValueError:
                print("Invalid input.")

        elif choice == "3":
            try:
                patient_id = int(input("Enter patient ID: "))
                doctor_id = int(input("Enter doctor ID: "))
                if hospital.assignPatientToDoctor(patient_id, doctor_id):
                    print("Patient assigned successfully.")
                else:
                    print("Patient or doctor not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            try:
                doctor_id = int(input("Enter doctor ID: "))
                treated_patient = hospital.treatNextPatient(doctor_id)
                if treated_patient is None:
                    print("Doctor not found or queue is empty.")
                else:
                    print("Treated patient:")
                    print(treated_patient)
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            try:
                patient_id = int(input("Enter patient ID: "))
                new_severity = int(input("Enter new severity: "))
                updated = False

                for patient in hospital.patients_list:
                    if patient.patient_id == patient_id:
                        patient.updatePriority(new_severity)
                        updated = True
                        break

                if not updated:
                    for doctor in hospital.doctors_list:
                        for index in range(len(doctor.patients_queue.items)):
                            if doctor.patients_queue.items[index].patient_id == patient_id:
                                patient = doctor.patients_queue.items.pop(index)
                                patient.updatePriority(new_severity)
                                doctor.addPatient(patient)
                                updated = True
                                break
                        if updated:
                            break

                if updated:
                    print("Patient priority updated successfully.")
                else:
                    print("Patient not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "6":
            statistics = hospital.patientStatistics()
            if len(statistics) == 0:
                print("No patients found.")
            else:
                print("\nPatient Statistics:")
                for severity in sorted(statistics.keys(), reverse=True):
                    print(f"Severity {severity}: {statistics[severity]}")

        elif choice == "7":
            try:
                severity = int(input("Enter severity level: "))
                patients = hospital.patientByPriority(severity)
                if len(patients) == 0:
                    print("No patients found with this severity.")
                else:
                    print(patients)
            except ValueError:
                print("Invalid input.")

        elif choice == "8":
            doctors = hospital.allDoctors()
            if len(doctors) == 0:
                print("No doctors found.")
            else:
                print(doctors)

        elif choice == "9":
            print("Exiting system...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
