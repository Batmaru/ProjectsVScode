'''### Test con UnitTest

Utilizzando il modulo unittest, definire i seguenti test per le classi Documento, Email e File.
 
I test devono includere:

    Verifica dei metodi getText() e setText() nella classe Documento.
    Verifica del metodo isInText() nella classe Documento.
    Verifica del metodo getText() nella classe Email.
    Verifica del metodo writeToFile() nella classe Email.
    Verifica del metodo isInText() nella classe Email.
    Verifica del metodo getText() nella classe File.
    Verifica del metodo isInText() nella classe File.'''

import unittest
from testidigitali  import Documento, Email, File

class TestDDigitali(unittest.TestCase):

    def setUp(self):
        self.doc = Documento()
        self.email = Email()
        self.file = File('documento.txt')

    def test_documento_text(self):
        self.assertEqual(self.doc.getText(), "")
        self.doc.setText("test")
        self.assertEqual(self.doc.getText(), "test")
        
    def test_documento_isintext(self):
        self.doc.setText('test in py')
        self.assertTrue(self.doc.isInText('test'))
        self.assertFalse(self.doc.isInText('python'))

    def test_email_gettext(self):
        self.assertEqual(self.email.getText(), f"Da:  A: \nTitolo: \nMessaggio: ")
        self.email.setText("test")
        self.assertEqual(self.email.getText(), "Da:  A: \nTitolo: \nMessaggio: test")

    def test_email_write(self):
        self.email.setMittente('marwan@gmail.com')
        self.email.setDestinatario('gabriele@gmail.com')
        self.email.setTitolo('brawlstars')
        self.email.setText('Questo è il contenuto del file')
        self.email.writetofile('test_email.txt')
        content=None
        with open('test_email.txt', 'r') as file:
            content = file.read()
        expected_text = ("Da: marwan@gmail.com A: gabriele@gmail.com\n"
                         "Titolo: brawlstars\n"
                         "Messaggio: Questo è il contenuto del file")
        self.assertEqual(content, expected_text)

    def test_email_isintest(self):
        self.email.setText('test in py')
        self.assertTrue(self.email.isInText('test'))

    def test_file_gettest(self):
        testo=(f'Percorso: documento.txt\nContenuto: frsrdjihfbgaiufhur')
        self.assertEqual(self.file.getText(), testo)