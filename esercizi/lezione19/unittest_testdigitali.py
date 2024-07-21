import unittest
from testidigitali import Documento, Email, File

'''I test devono includere:
Verifica dei metodi getText() e setText() nella classe Documento.
Verifica del metodo isInText() nella classe Documento.
Verifica del metodo getText() nella classe Email.
Verifica del metodo writeToFile() nella classe Email.
Verifica del metodo isInText() nella classe Email.
Verifica del metodo getText() nella classe File.
Verifica del metodo isInText() nella classe File.'''

class Testdigitali(unittest.TestCase):
    def setUp(self):
        self.documento = Documento()
        self.email = Email()
    
    def test_setText(self):
        self.documento.setText('questa è una email')
        self.assertEqual(self.documento.getText(), 'questa è una email')
        self.assertEqual(self.email.getText(),)
    
    def test_is_in_text(self):
        self.documento.isInText()
        self.assertTrue(self.documento('una'))
        
    
    
    



