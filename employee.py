class Employee:
    def __init__(self, first_name, last_name, annual_salary=5000):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise):
        self.annual_salary += salary_raise
        return self.annual_salary
