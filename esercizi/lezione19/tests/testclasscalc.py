import unittest

from  esercizi.lezione11.classcalc import Calculations

class testCalc(unittest.TestCase):

    def test_sum(self):

        calc_1 = Calculations(a=2, b=3)
        result = calc_1.get_sum()
        self.assertEqual(result, 5, msg=f'Error Test Failed the goal was 5 the function returned {result}')
    
    

if __name__ == "__main__":
    
    unittest.main()