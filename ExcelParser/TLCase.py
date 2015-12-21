'''
Created on 21 de oct. de 2015

@author: cgimenop
@updated Oct 29th 2015
'''

from xml.dom import minidom

class TLCase:
    
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
    
    IMPORTANCE_LOW = "1"
    IMPORTANCE_MEDIUM = "2"
    IMPORTANCE_HIGH = "3"
    
    '''
    classdocs
    '''
    
    
    def __init__(self, params = []):
        '''
        Constructor
        '''
        if (len(params) == 0):
            return
        
        self.title = params[self.TITLE].value
        
        
        self.summary = "</br>".join([params[self.CODE].value, params[self.TITLE].value, "Covers: ", params[self.LINKED_STORIES].value])
                
        self.importance = self.importance_value(params[self.IMPORTANCE].value)
        
        self.preconditions = params[self.PRECONDITIONS].value.replace("\n", "</br>")
        
        #TODO: This will need further work to split the excel cell in multiple steps
        self.steps = params[self.STEPS].value.replace("\n", "</br>")
        
        self.expected_result = "</br>".join([str(params[self.EXPECTED_RESULT].value), str(params[self.EXTRA_DETAILS].value)])
        self.expected_result = self.expected_result.replace("\n", "</br>")
        
        if (params[self.EXECUTION_TYPE].value == "yes"):
            self.execution_type = self.EXECUTION_TYPE_AUTO  
        else:
            self.execution_type = self.EXECUTION_TYPE_MANUAL  
        
    def importance_value(self, value):
        if (value == None):
            return self.IMPORTANCE_MEDIUM
        switcher = {
            self.EXCEL_IMPORTANCE_LOW: self.IMPORTANCE_LOW,
            self.EXCEL_IMPORTANCE_MEDIUM: self.IMPORTANCE_MEDIUM,
            self.EXCEL_IMPORTANCE_HIGH: self.IMPORTANCE_HIGH,
            }
        return switcher.get(value.upper(), self.IMPORTANCE_MEDIUM)
    
    def to_xml(self):
        xml_doc = minidom.Document()
        xml_test_case = xml_doc.createElement("testcase")
        xml_test_case.setAttribute("name", self.title)
        
        summary = xml_doc.createElement("summary")
        cdata = xml_doc.createCDATASection(self.summary)
        summary.appendChild(cdata)
        xml_test_case.appendChild(summary)
        
        preconditions = xml_doc.createElement("preconditions")
        cdata = xml_doc.createCDATASection(self.preconditions)
        preconditions.appendChild(cdata)
        xml_test_case.appendChild(preconditions)
        
        steps = xml_doc.createElement("steps")
        xml_test_case.appendChild(steps)
        
        step = xml_doc.createElement("step")
        steps.appendChild(step)
        
        actions = xml_doc.createElement("actions")
        step.appendChild(actions)
        cdata = xml_doc.createCDATASection(self.steps)
        actions.appendChild(cdata)
        
        expected_results = xml_doc.createElement("expectedresults")
        step.appendChild(expected_results)
        cdata = xml_doc.createCDATASection(self.expected_result)
        expected_results.appendChild(cdata)
        
        #TODO: When test description is correctly splited into steps this will have to change accordingly
        step_number = xml_doc.createElement("step_number")
        step.appendChild(step_number)
        cdata = xml_doc.createCDATASection("1")
        step_number.appendChild(cdata)
        
        
        execution_type = xml_doc.createElement("execution_type")
        cdata = xml_doc.createCDATASection(self.execution_type)
        execution_type.appendChild(cdata)
        xml_test_case.appendChild(execution_type)
        
        
        importance = xml_doc.createElement("importance")
        cdata = xml_doc.createCDATASection(self.importance)
        importance.appendChild(cdata)
        xml_test_case.appendChild(importance)
        
        return xml_test_case
    
        
        
        