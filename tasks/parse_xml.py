
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
sentences = collection.getElementsByTagName("sentence_id")

# Print detail of each sentence_id.
for sentence in sentences:
   print ("sentences = {")
   if sentence.hasAttribute("id"):
      print ("sentence_id: %s" % sentence.getAttribute("id"))
      print ("}")
