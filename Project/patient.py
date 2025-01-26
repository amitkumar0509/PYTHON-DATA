patient_list = []

class Patient:
    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.doctor_assigned = None

    def assign_doctor(self, doctor):
        self.doctor_assigned = doctor

    def get_details(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Disease: {self.disease}, Doctor: {self.doctor_assigned.name if self.doctor_assigned else 'None'}"

    def __str__(self):
        return self.get_details()


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def get_details(self):
        return f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}"

    def __str__(self):
        return self.get_details()


def add_patient(patient_id, name, age, disease, doctor=None):
    new_patient = Patient(patient_id, name, age, disease)
    if doctor:
        new_patient.assign_doctor(doctor) 
    patient_list.append(new_patient)  
    print(f"Patient {name} added successfully!")


def display_all_patients():
    print("\n--- List of Patients ---")
    if not patient_list:
        print("No patients in the system.")
    else:
        for patient in patient_list:
            print(patient)
class Billing:
    def __init__(self,patient,bedcharges):
        self.patient = patient
        self.medicinecost = []
        self.consultant_fee = 200
        self.bedcharges = bedcharges
        self.calculate_totalbill = 0

    def add_medicine(self, name, cost):
        self.medicinecost.append((name, cost))
    def calculate_total(self):
        self.total_bill = sum(cost for _, cost in self.medicinecost) + self.consultant_fee + self.bedcharges
        return self.total_bill
    def print_bill(self):
        print("\n--- Patient Bill ---")
        print(f"Patient Name: {self.patient.name}")
        print(f"Patient ID: {self.patient.patient_id}")
        print(f"Doctor Assigned: {self.patient.doctor_assigned.name if self.patient.doctor_assigned else 'No doctor assigned'}")
        print("\nMedicines:")
        for medicine, cost in self.medicinecost :
            print(f"  - {medicine}: ₹{cost}")
        print(f"\nConsultation Fee: ₹{self.consultant_fee}")
        print(f"Total Bill: ₹{self.calculate_total()}")
        print("--------------------")
doctor1 = Doctor(11,"Priya","Optometrist")
doctor2 = Doctor(1,"Neeraj Chopra ","Cardiologist")
doctor3 = Doctor(23,"Dev Aggarwal","Dermatologist")  
doctor4 = Doctor(112,"Nisha","Gastroenterologist")      
add_patient(101, "Amit", 40, "Skin",doctor3)
add_patient(102, "Raj", 35, "Heart",doctor2)
add_patient(103, "Neha", 29, "corneadefect",doctor1)
patient1 = Patient(105, "Sita devi", 45, "Heart Disease")
patient1.assign_doctor(doctor2)
patient_list.append(patient1)
billing1 = Billing(patient1,15000)
billing2 = Billing(patient_list[1],17000)
billing1.add_medicine("Aspirin", 20)
billing1.add_medicine("Beta Blocker", 50)
billing2.add_medicine("intracanazole",2356)
billing2.add_medicine("Glucose",600)
billing1.print_bill()
billing2.print_bill()
display_all_patients()
print("\nDetails of first patient:")
print(patient_list[1].get_details())

