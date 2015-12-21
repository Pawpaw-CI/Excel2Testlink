'''
Created on 29 de oct. de 2015

@author: cgimenop
'''
import unittest
from  TLCase import * 


class TLCaseUnitTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        
        pass

    def test_importance(self): 
        case = TLCase()
        self.assertEqual(case.importance_value("l"), case.IMPORTANCE_LOW, "Low priority wrong parsed")
        self.assertEqual(case.importance_value("m"), case.IMPORTANCE_MEDIUM, "Medium priority wrong parsed")
        self.assertEqual(case.importance_value("h"), case.IMPORTANCE_HIGH, "High priority wrong parsed") 
        self.assertEqual(case.importance_value(""), case.IMPORTANCE_MEDIUM, "Empty priority case not treated")
        self.assertEqual(case.importance_value(None), case.IMPORTANCE_MEDIUM, "Empty priority case not treated")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testImportance']
    unittest.main()