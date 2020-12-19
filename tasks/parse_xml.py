
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
import xml.dom.minidom

def parse_xml(xmlFile):
    """
    parse the xml
    """
    doc = xml.dom.minidom.parse("test.xml")
    #get the list of xml tags which is start with sentence
    tags = doc.getElementsByTagName("sentence id")
    sentences={}
    for tag in tags:
        sentences[sentence_id] = tag.getattribute("name")
