class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def promote(self, new_position, salary_increase):
        self.position = new_position
        self.salary += salary_increase

    def display_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary:,.2f}")

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]

    def get_total_salary(self):
        return sum(emp.salary for emp in self.employees)

    def display_department_info(self):
        print(f"Department: {self.name}")
        print("Employees:")
        for employee in self.employees:
            print(f" - {employee.name}, {employee.position}")

# Örnek kullanım
if __name__ == "__main__":
    # İki çalışan oluşturalım
    emp1 = Employee(101, "John Doe", "Software Engineer", 75000)
    emp2 = Employee(102, "Jane Smith", "Product Manager", 90000)

    # Departman oluşturalım ve çalışanları ekleyelim
    department_it = Department("IT Department")
    department_it.add_employee(emp1)
    department_it.add_employee(emp2)

    # Departman bilgilerini gösterelim
    department_it.display_department_info()
    total_salary = department_it.get_total_salary()
    print(f"\nTotal Department Salary: ${total_salary:,.2f}\n")

    # Çalışanları terfi ettirelim
    emp1.promote("Senior Software Engineer", 9000)
    emp2.promote("Senior Product Manager", 12000)

    # Departman bilgilerini güncelleyelim
    department_it.display_department_info()
    total_salary = department_it.get_total_salary()
    print(f"\nTotal Department Salary: ${total_salary:,.2f}\n")
