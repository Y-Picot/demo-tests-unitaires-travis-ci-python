import unittest
import bibliotheque

class UneClasseDeTest(unittest.TestCase):
        
    def setUp(self):
        print("Avant le test")
        self.a = 1
        self.b = 2    
        self.c = 50 
        self.d = 0

    def tearDown(self):
        print("Après le test")
        a = None
        b = None 
        c = None
        d = None
        
    def test_addition(self):
        self.assertEqual(3,bibliotheque.addition(self.a,self.b))
        self.assertNotEqual(5,bibliotheque.addition(self.a,self.b))        

    def test_soustraction(self):
        self.assertEqual(-1,bibliotheque.soustraction(self.a,self.b))
        self.assertNotEqual(4,bibliotheque.soustraction(self.a,self.b))
    
    def test_multiplication(self):
        self.assertEqual(2,bibliotheque.multiplication(self.a,self.b))
        self.assertNotEqual(4,bibliotheque.multiplication(self.a,self.b))
        
    
    def test_division(self):
        self.assertEqual(0.5,bibliotheque.division(self.a,self.b))
        self.assertNotEqual(4,bibliotheque.division(self.a,self.b))
        self.assertEqual(0.0,bibliotheque.division(self.a,self.d))
        
    def test_carree(self):
        self.assertEqual(4,bibliotheque.carree(self.b))
        self.assertNotEqual(1,bibliotheque.carree(self.b))
   
    def test_racineCarree(self):
        self.assertEqual(7.07,bibliotheque.racineCarree(self.c))
        self.assertNotEqual(1,bibliotheque.racineCarree(self.c))
    
    def test_cosinus(self):
        self.assertEqual(0.54,bibliotheque.cosinus(self.a))
        self.assertNotEqual(1,bibliotheque.cosinus(self.a))          
            
if __name__ == '__main__':
    unittest.main()