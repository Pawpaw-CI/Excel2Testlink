'''
Created on 21 de oct. de 2015

@author: cgimenop
@updated Oct 29th 2015
'''

from xml.dom import minidom


class TLSuite:
    '''
    classdocs
    '''
      
    
    def __init__(self, title, cases = []):
        '''
        Constructor
        '''
        
        self.title = title
        self.cases = cases
        
        
    def add_tlcase(self, new_case):
        self.cases.append(new_case)    
        
    def to_xml(self):
        xml_doc = minidom.Document()
        
        xml_test_suite = xml_doc.createElement("testsuite")
        xml_test_suite.setAttribute("name", self.title)
        xml_doc.appendChild(xml_test_suite)
    
        for case in self.cases:
            xml_test_case = case.to_xml()
        
            xml_test_suite.appendChild(xml_test_case)
        
        return xml_doc.toprettyxml(indent="\t")
        
        