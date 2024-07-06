class Job:
    def __init__(self, name, salary, hours_worked):
        self.name = name
        self.salary = salary
        self.hours_worked = hours_worked

    def print_information(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Hours worked: ", self.hours_worked)

    
class Doctor(Job):
    def __init__(self, name, salary, hours_worked, specialty, years_of_experience):
        super().__init__(name, salary, hours_worked)
        self.specialty = specialty
        self.years_of_experience = years_of_experience

    def print_information(self):
        super().print_information()
        print("Speciality: ", self.specialty)
        print("Years of Experience: ", self.years_of_experience)

class Teacher(Job):
    def __init__(self, name, salary, hours_worked, subject, position):
        super().__init__(name, salary, hours_worked)
        self.subject = subject
        self.position = position
    
    def print_information(self):
        super().print_information()
        print("Subject: ", self.subject)
        print("Position: ", self.position)

lawyer = Job("Hercule Poirot", 2000, 7)
teacher = Teacher("Alan Turing", 560, 12, "Informatics", "Junior Teacher")
doctor = Doctor("John Smith", 890, 14, "Pediatrician", 15)

# Print information
print("================================")
print("The lawyer about information...")
print("================================")
lawyer.print_information()
print("================================")
print("The teacher about information...")
print("================================")
teacher.print_information()
print("================================")
print("The doctor about information...")
print("================================")
doctor.print_information()