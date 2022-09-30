import EmployeeClass as e 
import PayrollDeductionClass as p



my_employee = e.Employees('Jimmy Smith',58475,"Information Systems",'Developer',6800)
deduction1 = p.Payroll('food court', '8/14/2022',22.50,39119)
deduction2 = p.Payroll('gift contribution', '8/12/2022', 25.00, 58475)
deduction3= p.Payroll('food court', '8/17/2022', 15.25, 21547)
deduction4= p.Payroll('vending machine', '8/22/2022', 3.00, 58475)
deduction5= p.Payroll('vending machine', '8/5/2022', 2.75, 58475)

print("*** Employee Pay ***")
print("Name:",my_employee.Name())
print("ID number:", my_employee.EmployeeID())
print("Department:", my_employee.Department())
print("Gross Pay: $",float(my_employee.Salary()))
print("Net Pay: $",my_employee.Salary()-deduction2.Deduction_charge()-deduction4.Deduction_charge()-deduction5.Deduction_charge())
print(deduction1)