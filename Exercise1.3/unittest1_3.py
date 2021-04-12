import unittest
from script1_3 import validator

class TestCase(unittest.TestCase):

    # Used passwords
    passwords = ['Wg&0gP56YzR','pLT(g5Jy7','i!T^q*&%w12','%YytSU&0*e9lQy','#R8M5%9W03(','^Vw9L3& p6i7!gDW1yp&*W7y Je7q8iXx5M9x^ @&^M7D yV7ZA0DG']

    # Size validations
    def test1_lenValidation(self):
        result = validator(self.passwords[1],['LEN','>',9])
        self.assertEqual(False,result)

    def test2_lenValidation(self):
        result = validator(self.passwords[5],['LEN','>',9])
        self.assertEqual(True,result)

    def test3_lenValidation(self):
        result = validator(self.passwords[3],['LEN','<',30])
        self.assertEqual(True,result)

    def test4_lenValidation(self):
        result = validator(self.passwords[5],['LEN','<',30])
        self.assertEqual(False,result)

    def test5_lenValidation(self):
        result = validator(self.passwords[1],['LEN','==',9])
        self.assertEqual(True,result)

    def test6_lenValidation(self):
        result = validator(self.passwords[2],['LEN','==',9])
        self.assertEqual(False,result)
    
    # Letter validation
    def test1_letValidation(self):
        result = validator(self.passwords[1],['LETTERS','>',10])
        self.assertEqual(False,result)

    def test2_letValidation(self):
        result = validator(self.passwords[5],['LETTERS','>',10])
        self.assertEqual(True,result)

    def test3_letValidation(self):
        result = validator(self.passwords[0],['LETTERS','<',7])
        self.assertEqual(False,result)

    def test4_letValidation(self):
        result = validator(self.passwords[4],['LETTERS','<',7])
        self.assertEqual(True,result)

    def test5_letValidation(self):
        result = validator(self.passwords[2],['LETTERS','==',9])
        self.assertEqual(False,result)

    def test6_letValidation(self):
        result = validator(self.passwords[3],['LETTERS','==',9])
        self.assertEqual(True,result)

    # Number validation
    def test1_numbValidation(self):
        result = validator(self.passwords[1],['NUMBERS','>',5])
        self.assertEqual(False,result)

    def test2_numbValidation(self):
        result = validator(self.passwords[5],['NUMBERS','>',9])
        self.assertEqual(True,result)

    def test3_numbValidation(self):
        result = validator(self.passwords[0],['NUMBERS','<',3])
        self.assertEqual(False,result)

    def test4_numbValidation(self):
        result = validator(self.passwords[1],['NUMBERS','<',3])
        self.assertEqual(True,result)

    def test5_numbValidation(self):
        result = validator(self.passwords[0],['NUMBERS','==',3])
        self.assertEqual(True,result)

    def test6_numbValidation(self):
        result = validator(self.passwords[4],['NUMBERS','==',5])
        self.assertEqual(True,result)

    # Special Characters validation
    def test1_speValidation(self):
        result = validator(self.passwords[1],['SPECIALS','>',3])
        self.assertEqual(False,result)
    
    def test2_speValidation(self):
        result = validator(self.passwords[2],['SPECIALS','>',3])
        self.assertEqual(True,result)

    def test3_speValidation(self):
        result = validator(self.passwords[3],['SPECIALS','<',2])
        self.assertEqual(False,result)

    def test4_speValidation(self):
        result = validator(self.passwords[2],['SPECIALS','<',6])
        self.assertEqual(True,result)
    
    def test5_speValidation(self):
        result = validator(self.passwords[5],['SPECIALS','==',3])
        self.assertEqual(False,result)

    def test6_speValidation(self):
        result = validator(self.passwords[0],['SPECIALS','==',1])
        self.assertEqual(True,result)

    # Wrong parameter validation
    # List empty
    def test1_wrongValidation(self):
        result = validator(self.passwords[0],[])
        self.assertEqual(False,result)
    # Firt requirement wrong
    def test2_wrongValidation(self):
        result = validator(self.passwords[0],['SPECIAL','==',1])
        self.assertEqual(False,result)
    # Second requirement wrong
    def test3_wrongValidation(self):
        result = validator(self.passwords[0],['SPECIALS','=',1])
        self.assertEqual(False,result)
    # Third requirement wrong
    def test4_wrongValidation(self):
        result = validator(self.passwords[0],['SPECIALS','==','dois'])
        self.assertEqual(False,result)
    # Password Empty
    def test5_wrongValidation(self):
        result = validator('',['SPECIALS','==',1])
        self.assertEqual(False,result)

if __name__ == '__main__':
    unittest.main()

    
    