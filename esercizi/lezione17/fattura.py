from dottore import Dottore
from paziente import Paziente
class Fattura:
    def __init__(self, patient: list=[], doctor: list= []):
        self.patient = patient
        self.doctor = doctor
        for doctor in self.doctor:
            if doctor.isValidDoctor()== True:
                self.fatture = len(self.patient)
                self.salary=0
            else:
                self.patient= None
                self.doctor=None
                self.fatture=None
                self.salary=None
                print("non è possibile creare la classe fattura perchè il dottore non è valido")
                break
    
    

    


paziente1=Paziente('marco','dettomarco', 'fsoifhr3')
dottore1= Dottore('angelo', 'aldino','ihoerfho', 98696)
dottore1.SetAge(78)
fattura1 = Fattura([paziente1], [dottore1])