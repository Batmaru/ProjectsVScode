from dottore import Dottore
from paziente import Paziente
class Fattura:
    def __init__(self, doctor: Dottore, patient: list[Paziente]=[]):
        self.patient = patient
        self.doctor = doctor

        if doctor.isValidDoctor()== True:
            self.fatture = len(self.patient)
            self.salary=0
        else:
            self.patient= None
            self.doctor=None
            self.fatture=None
            self.salary=None
            print("non è possibile creare la classe fattura perchè il dottore non è valido")


    def getsalary(self):
        self.salary=self.doctor.getParcel() * len(self.patient)
        return self.salary
    
    def getFatture(self):
        return len(self.patient)
    
    def addPatient(self, newpatient: Paziente):
        if newpatient not in self.patient:
            self.patient.append(newpatient)
            self.salary = self.getsalary()
            self.fatture = self.getFatture()
        else:
            print("il paziente è già presente nella lista")

    def removePatient(self, idCode: str):
        for paziente in self.patient:
            if paziente.getIdCode() == idCode:
                self.patient.remove(paziente)
                self.salary= self.getsalary()
                self.fatture = self.getFatture()


dottore = Dottore('Angelo', 'Verdi', 'Cardiochirurgo', 200.0)
dottore.SetAge(45)
paziente1 = Paziente('Marco', 'Bianchi', 'ABC123')
paziente2 = Paziente('Luca', 'Rossi', 'DEF456')
fattura = Fattura(dottore, [paziente1])
print(fattura)

fattura.addPatient(paziente2)
print(fattura)


            
    
    

    


