# Multi-level and hiercirecal inheritances

class Address:
    __address:str = ""
    def sumAddress(self,address):
        self.__address = address
    def getAddress(self):
        return self.__address
class Employee(Address):
    __firstName:str =""
    __lastName:str = ""
    __surname:str = ""
    def setname(self,fname:str,lname:str,sname:str):
        self.__firstName = fname
        self.__lastName = lname
        self.__surname = sname
    def __nameformat(self):
        return f'{self.__surname} {self.__firstName} {self.__lastName}'
    def getfullName(self):
        return self.__nameformat()
class permanentEmployee(Employee):
    __sal:int = 45000
    def salcal(self):
        return 12*self.__sal
class contractEmployee(Employee):
    __hr_pay:int = 5000
    def salcal(self,hrs:int):
        return f'salcal for {hrs} hrs.(self.__hr_pay*hrs)'
emp = permanentEmployee()
emp.setname(fname="Sai",sname="G",lname="Sundhar")
emp.sumAddress("kurnool")
print(emp.getfullName())
print(emp.getAddress())
print(emp.salcal())

cemp = contractEmployee()
cemp.setname(fname="Sai",sname="G",lname="Sundhar")
cemp.sumAddress("kurnool")
print(cemp.getfullName())
print(cemp.getAddress())
print(cemp.salcal(20))


#multiple inheritance
class SAI:
    def printdata(self):
        print(5000)
class aa:
    def printdata(self):
        print(1000)
class ClassA(aa,SAI):
    pass
a = ClassA()
a.printdata()

# hydrid inheritances
class ClassA:
    def printdata(self):
        print("sai")
class ClassB(ClassA):
     def printdata(self):
        print("SUNDHAR")
class ClassC(ClassA):
    def printdata(self):
        print("DHANUNJAI")
class ClassD(ClassB,ClassC):
    pass
a = ClassD()
a.printdata()
