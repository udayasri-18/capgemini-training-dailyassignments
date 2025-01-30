class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed successfully.")
                return
        print("Book not found.")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                print(f"Book Found: {book.title} by {book.author}")
                return
        print("Book not found.")

    def display_books(self):
        if self.books:
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Copies: {book.copies}")
        else:
            print("No books available.")


# Create Library instance
library = Library()

# Adding Books
book1 = Book("Python Programming", "John Doe", "123456", 5)
book2 = Book("Machine Learning", "Jane Doe", "789012", 3)

library.add_book(book1)
library.add_book(book2)

print("\nDisplaying Books:")
library.display_books()

print("\nSearching for a Book:")
library.find_book("789012")  # Direct call without checking return value

print("\nRemoving a Book:")
library.remove_book("123456")

print("\nDisplaying Books After Removal:")
library.display_books()


class Employee:
    employees = []  # Store all employees

    def __init__(self, name, age, salary, department, role, skills=None):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department
        self.role = role  
        self.skills = skills if skills else [] 
        Employee.employees.append(self)  

    @classmethod
    def find_manager(cls, department):
        for emp in cls.employees:
            if emp.department == department and emp.role == "Manager":
                return emp.name
        return "No manager found."

    @classmethod
    def count_employees(cls, department=None, skill=None):
        sum=0
        for emp in cls.employees:
            if department and emp.department == department:
                sum+=1
            elif skill and emp.role == "Engineer" and skill in emp.skills:
                sum+=1
        return sum

    @classmethod
    def employees_per_department(cls):
        dept_count = {}
        for emp in cls.employees:
            dept_count[emp.department] = dept_count.get(emp.department, 0) + 1
        return dept_count

n=int(input("Enter number of departments"))
for _ in range(n):  
    dept = input("\nEnter department name: ")

    # Manager
    print(f"Enter Manager details for {dept}:")
    Employee(input("Name: "), int(input("Age: ")), float(input("Salary: ")), dept, "Manager")

    # Engineers
    for i in range(3):
        print(f"Enter Engineer {i+1} details for {dept}:")
        Employee(input("Name: "), int(input("Age: ")), float(input("Salary: ")), dept, "Engineer", input("Skills: ").split(","))

# Functionality
print("\nManager of department:", Employee.find_manager(input("Enter department to find manager: ")))
print("Employees in department are:", Employee.count_employees(department=input("Enter department to find no of employees: ")))
print("Engineers with skill :", Employee.count_employees(skill=input("Enter skill: ")))

print("\nTotal employees per department:")
for dept, count in Employee.employees_per_department().items():
    print(f"{dept}: {count}")

print("\nTotal employees in company:", Employee.count_employees())
