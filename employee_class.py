'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 10 Assignment 2
'''



class Employee:
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_gross_salary(self):
        return self.hourly_rate * self.hours_worked
    
    def calculate_salary_after_tax(self, tax_rate):
       try:
           tax_rate = float(tax_rate)
           if tax_rate < 0 or tax_rate >1:
               raise ValueError("Tax rate must be between 0 and 1.")
           
           gross_salary = self.calculate_gross_salary()
           tax_amount = gross_salary * tax_rate
           net_salary = gross_salary - tax_amount
           return net_salary
       except ValueError as error:
           print(f"Error calculating salary: {error}")
           return None
    
    def display_infor(self):
        return (
            f"Employee Name: {self.name}, Hourly Rate: ${self.hourly_rate:.2f}, "
            f"Hours Worked: {self.hours_worked}"
        )
    def create_employee(name, hourly_rate, hours_worked):
        try:
            hourly_rate = float(hourly_rate)
            hours_worked = float(hours_worked)
            
            if hourly_rate < 0 or hours_worked < 0:
                raise ValueError("Hourly rate and hours worked must be non-negative.")
            
            return Employee(name, hourly_rate, hours_worked)
        except ValueError as error:
            print(f"Could not create employee: {error}")
            return None
        
    def run_demo():
        try:
           employee = create_employee("Rayaan", 28.50, 40)
           if employee is None:
               return
           
           print(employee.display_info())
           gross = employee.calculate_gross_salary()
           net = employee.calculate_salary_after_tax(0.20)

           print(f"Gross Salary: ${gross:.2f}")
           if net is not None:
               print(f"Salary after tax: ${net:.2f}")

           print("\nTesting validation with tax rate 1.5...")
           employee.calculate_salary_after_tax(1.5)
                                               
        except Exception as error:
            print(f"Unexpected error in employee demo: {error}")

if __name__ == "__main__":
    run_demo()
