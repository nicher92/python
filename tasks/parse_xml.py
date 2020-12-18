
"""
write a function called parse_xml() which loads and parses data/21728182.xml. The data contains NER labeled sentences.

The output of the parse_xml() should be a two dicts structured in the following way:

sentences = {
            sentence_id:"sentence",
            ...
            }

ners = {
            sentence_id:[
                         ((char_start, char_end),  NER_TYPE),
                        ...
                        
                        ]
            ...
        
        }

NOTE! NER_TYPE is the label not the drug text/name
"""
from xml import etree
def parse_xml(xmlFile):
    """
    parse the xml
    """
    with open(xmlFile) as fobj:
        xml = fobj.read()
    root = etree.fromstring(xml)
    for appt in root.getchildren():
        for elem in appt.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = elem.text
            print(elem.tag + "=>" + text)
#if __name__ == "__main__":
    #parse_xml("/ Users/ Akhav/ Documents/ GitHub/ python/ data/ test.xml")
