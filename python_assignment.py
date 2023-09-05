class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

def search_by_age(employees, operator, age):
    result = []
    if operator == '<':
        result = [emp for emp in employees if emp.age < age]
    elif operator == '>':
        result = [emp for emp in employees if emp.age > age]
    elif operator == '<=':
        result = [emp for emp in employees if emp.age <= age]
    elif operator == '>=':
        result = [emp for emp in employees if emp.age >= age]
    
    return result

def search_by_salary(employees, operator, salary):
    result = []
    if operator == '<':
        result = [emp for emp in employees if emp.salary < salary]
    elif operator == '>':
        result = [emp for emp in employees if emp.salary > salary]
    elif operator == '<=':
        result = [emp for emp in employees if emp.salary <= salary]
    elif operator == '>=':
        result = [emp for emp in employees if emp.salary >= salary]
    
    return result

def search_by_employee_id(employees, emp_id):
    result = [emp for emp in employees if emp.emp_id == emp_id]
    return result

def print_employee_data(employees):
    if not employees:
        print("No matching records found.")
    else:
        print("Employee ID\tName\tAge\tSalary")
        for emp in employees:
            print(f"{emp.emp_id}\t\t{emp.name}\t{emp.age}\t{emp.salary}")

if __name__ == "__main__":
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    while True:
        print("\nOptions:")
        print("1. Search by Age")
        print("2. Search by Salary")
        print("3. Search by Employee ID")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            operator = input("Enter operator (<, >, <=, >=): ")
            age = int(input("Enter age: "))
            result = search_by_age(employees, operator, age)
            print_employee_data(result)
        elif choice == '2':
            operator = input("Enter operator (<, >, <=, >=): ")
            salary = int(input("Enter salary: "))
            result = search_by_salary(employees, operator, salary)
            print_employee_data(result)
        elif choice == '3':
            emp_id = input("Enter Employee ID: ")
            result = search_by_employee_id(employees, emp_id)
            print_employee_data(result)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
