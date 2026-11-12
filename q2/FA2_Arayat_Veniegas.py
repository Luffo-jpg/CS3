class Patient:
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = float(bill_amount)

    def get_name(self):
        return self._name

    def get_bill_amount(self):
        return self._bill_amount

    def set_name(self, name):
        self._name = name

    def set_bill_amount(self, bill_amount):
        self._bill_amount = float(bill_amount)

    def calculate_bill(self):
        return self._bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


def display_billing_info(patient_object):
    print(f"Patient Name:  {patient_object.get_name()}")
    print(f"Original Bill: ₱{patient_object.get_bill_amount():,.2f}")
    print(f"Final Bill:    ₱{patient_object.calculate_bill():,.2f}")
    print("-" * 30)


if __name__ == "__main__":
    print("Hospital Billing System")
    print("------------------------")

    regular_patient = Patient("Juan Dela Cruz", 15000.00)
    senior_patient = SeniorPatient("Maria Santos", 15000.00)
    philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000.00)

    display_billing_info(regular_patient)
    display_billing_info(senior_patient)
    display_billing_info(philhealth_patient)
