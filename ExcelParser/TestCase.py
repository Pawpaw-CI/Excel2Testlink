'''
Created on 21 de oct. de 2015

@author: cgimenop
'''

class TestCase:
    
    CODE = 0;
    TITLE = 1
    SUMMARY = 2
    IMPORTANCE = 3
    PRECONDITIONS = 4
    STEPS = 5
    EXPECTED_RESULT = 6
    EXTRA_DETAILS = 7 #UNUSED
    EXECUTION_TYPE = 8
    E2E = 9 #UNUSED
    REGRESSION = 10 #UNUSED
    LINKED_STORIES = 11
    STATE = 12 #UNUSED
    COMMENTS = 13 #UNUSED
    
    EXECUTION_TYPE_MANUAL = "1"
    EXECUTION_TYPE_AUTO = "2"
    
    EXCEL_IMPORTANCE_LOW = "L"
    EXCEL_IMPORTANCE_MEDIUM = "M"
    EXCEL_IMPORTANCE_HIGH = "H"
    
    IMPORTANCE_LOW = 1
    IMPORTANCE_MEDIUM = 2
    IMPORTANCE_HIGH = 3
    
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        
        self.title = params[self.TITLE].value
        
        #FIXME: Which is the best way to concat strings?
        self.summary = params[self.CODE].value + "</br>"
        self.summary += params[self.TITLE].value + "</br>"
        
        self.summary += "Covers: " + params[self.LINKED_STORIES].value+"</br>"
        
        self.importance = self.importance_value(params[self.IMPORTANCE].value)
        self.preconditions = params[self.PRECONDITIONS].value.replace("\n", "</br>")
        
        #TODO: This will need further work
        self.steps = params[self.STEPS].value.replace("\n", "</br>")
        
        self.expected_result = str(params[self.EXPECTED_RESULT].value)+"</br>"+str(params[self.EXTRA_DETAILS].value)
        self.expected_result = self.expected_result.replace("\n", "</br>")
        
        if (params[self.EXECUTION_TYPE].value == "yes"):
            self.execution_type = self.EXECUTION_TYPE_AUTO  
        else:
            self.execution_type = self.EXECUTION_TYPE_MANUAL  
        
    def importance_value(self, value):
        if (value == None):
            return self.IMPORTANCE_MEDIUM
        switcher = {
            "L": self.IMPORTANCE_LOW,
            "M": self.IMPORTANCE_MEDIUM,
            "H": self.IMPORTANCE_HIGH,
            }
        return switcher.get(value.upper(), self.IMPORTANCE_MEDIUM)
    
    
        
        
        