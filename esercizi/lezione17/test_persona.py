import unittest
from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura


class TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona = Persona('Gabriele', 'Rossi')
    
    def test_initialization(self):
        self.assertEqual(self.persona.GetName(), 'Gabriele')
        self.assertEqual(self.persona.GetLastName(), 'Rossi')
        self.assertEqual(self.persona.GetAge(), 0)
    
    def test_setName(self):
        self.persona.SetName('Luca')
        self.assertEqual(self.persona.GetName(), 'Luca')
    
    def test_setLastName(self):
        self.persona.SetLastName('Bianchi')
        self.assertEqual(self.persona.GetLastName(), 'Bianchi')
    
    def test_setAge(self):
        self.persona.SetAge(25)
        self.assertEqual(self.persona.GetAge(), 25)


class TestDottore(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore('Angelo', 'Verdi', 'Cardiochirurgo', 200.0)
    
    def test_initialization(self):
        self.assertEqual(self.dottore.GetName(), 'Angelo')
        self.assertEqual(self.dottore.GetLastName(), 'Verdi')
        self.assertEqual(self.dottore.getspecialization(), 'Cardiochirurgo')
        self.assertEqual(self.dottore.getParcel(), 200.0)
    
    def test_isValidDoctor(self):
        self.dottore.SetAge(45)
        self.assertTrue(self.dottore.isValidDoctor())
        self.dottore.SetAge(25)
        self.assertFalse(self.dottore.isValidDoctor())

class TestPaziente(unittest.TestCase):
    def setUp(self):
        self.paziente = Paziente('Marco', 'Bianchi', 'ABC123')
    
    def test_initialization(self):
        self.assertEqual(self.paziente.GetName(), 'Marco')
        self.assertEqual(self.paziente.GetLastName(), 'Bianchi')
        self.assertEqual(self.paziente.getIdCode(), 'ABC123')

class TestFattura(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore('Angelo', 'Verdi', 'Cardiochirurgo', 200.0)
        self.dottore.SetAge(45)
        self.paziente1 = Paziente('Marco', 'Bianchi', 'ABC123')
        self.paziente2 = Paziente('Luca', 'Rossi', 'DEF456')
        self.fattura = Fattura(self.dottore, [self.paziente1])
    
    def test_initialization(self):
        self.assertIsInstance(self.fattura.doctor, Dottore)
        self.assertEqual(len(self.fattura.patient), 1)
        self.assertEqual(self.fattura.getsalary(), 200.0)

    def test_getSalary(self):
        self.assertEqual(self.fattura.getsalary(), 200.0)
        self.fattura.addPatient(self.paziente2)
        self.assertEqual(self.fattura.getsalary(), 400.0)

    def test_getFatture(self):
        self.assertEqual(self.fattura.getFatture(), 1)
        self.fattura.addPatient(self.paziente2)
        self.assertEqual(self.fattura.getFatture(), 2)

    def test_addPatient(self):
        self.fattura.addPatient(self.paziente2)
        self.assertIn(self.paziente2, self.fattura.patient)
        self.assertEqual(len(self.fattura.patient), 2)

    def test_removePatient(self):
        self.fattura.removePatient('ABC123')
        self.assertNotIn(self.paziente1, self.fattura.patient)
        self.assertEqual(len(self.fattura.patient), 0)

if __name__ == '__main__':
    unittest.main()
