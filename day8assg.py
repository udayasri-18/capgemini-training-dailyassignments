from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"Work of the employee {self.name} is Manager"

    def get_salary(self):
        return self.salary

class Developer(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self) -> str:
        return f"Work of the employee {self.name} is Developer"

    def get_salary(self):
        return self.salary

class Department:
    def __init__(self):
        self.employees = []

    def hire(self, employee: Employee):
        self.employees.append(employee)

    def fire(self, employee: Employee):
        self.employees.remove(employee)

    def get_total_salary(self):
        return sum(employee.get_salary() for employee in self.employees)

    def show_employee_details(self):
        for employee in self.employees:
            print(f"Name: {employee.name}, Role: {employee.work()}, Salary: {employee.get_salary()}")

# Testing the implementation
manager = Manager("John Doe", 75000)
developer = Developer("Jane Smith", 60000)

department = Department()
department.hire(manager)
department.hire(developer)

department.show_employee_details()
print(f"Total Salary Expense: {department.get_total_salary()}")

# Fire an employee and show updated details
department.fire(developer)
print("\nAfter firing an employee:")
department.show_employee_details()
print(f"Total Salary Expense: {department.get_total_salary()}")