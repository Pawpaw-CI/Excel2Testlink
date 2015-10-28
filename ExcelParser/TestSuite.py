'''
Created on 21 de oct. de 2015

@author: cgimenop
'''

class TestSuite:
    '''
    classdocs
    '''
      
    
    def __init__(self, title, cases = []):
        '''
        Constructor
        '''
        
        self.title = title
        self.cases = cases
        
        
    def addCase(self, new_case):
        self.cases.append(new_case)    