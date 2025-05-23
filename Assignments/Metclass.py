class Admin_office:
    def __init__(self,cabins):
        self.cabins = cabins
        self.sofa = 4
        self.tables = 5
    def open(self):
        print("Admin office is opened")
    def available(self):
        print(f"{self.cabins} seater cabins is available in admin office")
    def close(self):
        print("Admin office is closed")
    
class Python_class:
     def __init__(self):
         self.chairs = 30
         self.AC = 2
     def start(self):
         print("pythonclass is started")
     def stop(self):
         print("pythonclass is stopped")

class Datascience_class:
    def __init__(self):
         self.chairs = 30
         self.AC = 2

    def start(self):
         print("datascience class is started")
    def stop(self):
         print("datascience class is stopped")  
    
class MET :
    def __init__(self,admin_office,python_class,datascience_class):
        self.admin_office = admin_office
        self.python_class = python_class
        self.datascience_class = datascience_class

admin_office = Admin_office(5)
python_class = Python_class()
datascience_class = Datascience_class()
MET = MET(admin_office,python_class,datascience_class)

MET.admin_office.open()
MET.python_class.start()
MET.datascience_class.start()


        