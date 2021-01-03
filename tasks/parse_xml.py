
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

from xml.dom.minidom import parse
import xml.dom.minidom
# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("21728182.xml")
collection = DOMTree.documentElement

# Get all the sentence_id in the collection
sentences = collection.getElementsByTagName("sentence")

# Print detail of each sentence_id.
for sentence in sentences:
   print ("sentences = {")
   if sentence.hasAttribute("id"):
      print ("sentence_id: %s" % sentence.getAttribute("id"))
      print ("}")

           



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



from xml.dom import minidom
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET


### only works when file is in the same directory as XML file ###
tree = ET.parse("21728182.xml")
root = tree.getroot()

sentences = {}
ners = {}


#So far only the first part of assignment done
#Not sure what to do in the second part yet, he wants sa dictionary of
#sentence id as key, which is correct so far, but im not sure what value he wants
for elem in root:
	sentences[elem.attrib.get("id")] = elem.attrib.get("text")
	for subelem in elem:
		ners[elem.attrib.get("id")] = subelem.attrib.get("text")

