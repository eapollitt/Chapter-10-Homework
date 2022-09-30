class Employees: 
    def __init__(self,n,id,dep,j,sal):
         self.name = n
         self.__employee_id = id
         self.__department = dep
         self.__job = j
         self.__salary = sal

    def Name(self):
        return self.name 

    def EmployeeID(self):
        return self.__employee_id

    def Department(self):
        return self.__department 
    
    def Job(self):
        return self.__job 

    def Salary(self):
        return self.__salary 