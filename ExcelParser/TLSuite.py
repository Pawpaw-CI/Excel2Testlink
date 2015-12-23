'''
Created on 21 de oct. de 2015

@author: cgimenop
'''

from xml.dom import minidom


class TLSuite:
    '''
    classdocs
    '''
      
    
    def __init__(self, title, cases = [], requirements = dict()):
        '''
        Constructor
        '''
        
        self.title = title
        self.cases = cases
        self.requirements = requirements
        
        
    def add_tlcase(self, new_case):
        self.cases.append(new_case)
        case_requirements = new_case.get_requirements()
        for requirement_index in case_requirements:
            if requirement_index not in self.requirements:
                self.requirements[requirement_index] = case_requirements[requirement_index]
            
        
    def to_xml(self):
        xml_doc = minidom.Document()
        
        xml_test_suite = xml_doc.createElement("testsuite")
        xml_test_suite.setAttribute("name", self.title)
        xml_doc.appendChild(xml_test_suite)
    
        for case in self.cases:
            xml_test_case = case.to_xml()
        
            xml_test_suite.appendChild(xml_test_case)
        
        return xml_doc
        
    def get_requirements(self):
        return self.requirements 
                        
    def xml_requirements(self, req_doc_id = None):
        if (req_doc_id is None):
            print ("Invalid empty requirements id")
            raise
        
        xml_doc = minidom.Document()
        requirement_specification = xml_doc.createElement("requirement-specification")
        req_spec = xml_doc.createElement("req_spec")
        req_spec.setAttribute("title", req_doc_id)
        req_spec.setAttribute("doc_id", req_doc_id)
        
        for requirement in self.requirements:
            case_requirement = self.requirements[requirement]
            
            docid = xml_doc.createElement("docid")
            docid_cdata = xml_doc.createCDATASection(requirement)
            docid.appendChild(docid_cdata)
            case_requirement.appendChild(docid)
            
            requirement_description = xml_doc.createElement("description")
            description_cdata = xml_doc.createCDATASection(requirement)
            requirement_description.appendChild(description_cdata)
            case_requirement.appendChild(requirement_description)
            
            req_spec.appendChild(case_requirement)
 
        requirement_specification.appendChild(req_spec)
        return requirement_specification
        