class User:
    default_language = "English"  

    def __init__(self, name, age, country):
        self.name = name 
        self.age = age  
        self.country = country 


user1 = User("Ali", 25, "AZE")
user2 = User("NUR", 30, "Turkish")


class Book:
    default_discount = 0.1
    max_stock = 100


discount = Book.default_discount

max_stock = Book.max_stock

class WebServer:
    default_port = 80

WebServer.default_port = 443


class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
     

    def calculate_pay(self):
   
        pass


class HourlyEmployee(Employee):
    def __init__(self, employee_id, name, hourly_rate, hours_worked):
        super().__init__(employee_id, name, 0)  
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        self.salary = self.hourly_rate * self.hours_worked
        return self.salary


class SalariedEmployee(Employee):
    def __init__(self, employee_id, name, salary):
        super().__init__(employee_id, name, salary)


class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_payroll(self):
        for employee in self.employees:
            employee.calculate_pay()
            print(f"{employee.name}'s salary: ${employee.salary}")


payroll_system = PayrollSystem()


hourly_employee = HourlyEmployee("1", "Ali Hilal", 15, 40)
salaried_employee = SalariedEmployee("2", "Kenan Xasi", 3000)

payroll_system.add_employee(hourly_employee)
payroll_system.add_employee(salaried_employee)


payroll_system.calculate_payroll()


print("------------------------")
print("Task1 : ")

print("User 1:")
print("Name:", user1.name)
print("Age:", user1.age)
print("Country:", user1.country)
print("Default Language:", User.default_language)
print()
print("User 2:")
print("Name:", user2.name)
print("Age:", user2.age)
print("Country:", user2.country)
print("Default Language:", User.default_language)

print("------------------------------------------")
print("Task2 : ")

print("Discount:", discount)
print("Max Stock:", max_stock)

print("------------------------------------------")
print("Task3 : ")

print("Updated default_port : ", WebServer.default_port)












