'''
Created on 29 de oct. de 2015

@author: cgimenop
'''
import unittest
from  TLCase import TLCase 


class TLCaseUnitTest(unittest.TestCase):


    def setUp(self):
        
        pass


    def tearDown(self):
        
        pass

    def test_importance(self): 
        case = TLCase()
        
        self.assertEqual(case.importance_value(TLCase.EXCEL_IMPORTANCE_LOW.lower()), case.IMPORTANCE_LOW, "Low lower case priority wrong parsed")
        self.assertEqual(case.importance_value(TLCase.EXCEL_IMPORTANCE_MEDIUM.lower()), case.IMPORTANCE_MEDIUM, "Medium lower case priority wrong parsed")
        self.assertEqual(case.importance_value(TLCase.EXCEL_IMPORTANCE_HIGH.lower()), case.IMPORTANCE_HIGH, "High lower case priority wrong parsed") 
        self.assertEqual(case.importance_value(TLCase.EXCEL_IMPORTANCE_LOW), case.IMPORTANCE_LOW, "Low upper case priority wrong parsed")
        self.assertEqual(case.importance_value(TLCase.EXCEL_IMPORTANCE_MEDIUM), case.IMPORTANCE_MEDIUM, "Medium upper case priority wrong parsed")
        self.assertEqual(case.importance_value(TLCase.EXCEL_IMPORTANCE_HIGH), case.IMPORTANCE_HIGH, "High upper case priority wrong parsed")
        #TODO: Add random character check 
        self.assertEqual(case.importance_value(""), case.IMPORTANCE_MEDIUM, "Empty priority case not treated")
        self.assertEqual(case.importance_value(None), case.IMPORTANCE_MEDIUM, "None priority case not treated")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testImportance']
    unittest.main()