class Payroll:
    def __init__(self,desc,date,charge,id):
        self.__description = desc
        self.__Date = date
        self.__Charge = charge
        self.__employee_id = id
    
    def Deduction_description(self):
        return self.__description
    
    def Deduction_date(self):
        return self.__Date
    
    def Deduction_charge(self):
        return self.__Charge
    
    def Deduction_employee_id(self):
        return self.__employee_id
