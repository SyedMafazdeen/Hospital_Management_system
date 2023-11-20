class Doctor:
    def __init__(self, doctorId, doctorName, specialization, consultationFee):
        self.doctorId = doctorId
        self.doctorName = doctorName
        self.specialization = specialization
        self.consultationFee = consultationFee

class Hospital:
    def __init__(self, doctorDB):
        self.doctorDB = doctorDB

    def searchByDoctorName(self, doctorName):
        matching_doctors = []
        for doctor in self.doctorDB.values():
            if doctor.doctorName == doctorName:
                matching_doctors.append(doctor)
        if matching_doctors:
            return matching_doctors
        else:
            return None

    def calculateConsultationFeeBySpecialization(self, specialization):
        total_fee = 0
        for doctor in self.doctorDB.values():
            if doctor.specialization == specialization:
                total_fee += doctor.consultationFee
        return total_fee


# Main program
if __name__ == "__main__":
    num_doctors = int(input())
    doctors_dict = {}
    for _ in range(num_doctors):
        doctorId = int(input())
        doctorName = input()
        specialization = input()
        consultationFee = float(input())
        doctor = Doctor(doctorId, doctorName, specialization, consultationFee)
        doctors_dict[doctorId] = doctor

    hospital = Hospital(doctors_dict)

    doctor_name_to_search = input()
    matching_doctors = hospital.searchByDoctorName(doctor_name_to_search)
    if matching_doctors:
        for doctor in matching_doctors:
            print(doctor.doctorId)
            print(doctor.doctorName)
            print(doctor.specialization)
            print(doctor.consultationFee)

    else:
        print("No Doctor Exists with the given DoctorName")

    specialization_to_calculate = input()
    total_fee = hospital.calculateConsultationFeeBySpecialization(specialization_to_calculate)
    print(total_fee)
