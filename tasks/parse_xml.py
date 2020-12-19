
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
if collection.hasAttribute("shelf"):
   print ("Root element : %s" % collection.getAttribute("shelf"))
# Get all the sentence_id in the collection
sentences = collection.getElementsByTagName("sentence_id")

# Print detail of each sentence_id.
for sentence_id in sentences:
   print ("sentences = {")
   if sentence_id.hasAttribute("title"):
      print ("Title: %s" % sentence_id.getAttribute("title"))

   type = sentence_id.getElementsByTagName('type')[0]
   print ("Type: %s" % type.childNodes[0].data)
   format = sentence_id.getElementsByTagName('format')[0]
   print ("Format: %s" % format.childNodes[0].data)
   rating = sentence_id.getElementsByTagName('rating')[0]
   print ("Rating: %s" % rating.childNodes[0].data)
   description = sentence_id.getElementsByTagName('description')[0]
   print ("Description: %s" % description.childNodes[0].data)
