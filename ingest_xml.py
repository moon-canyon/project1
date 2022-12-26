#first need to install xmltodict:
#pip3 install xmltodict

import xmltodict   

def inxml():

    #get the XML file data
    stream = open('scan.xml','r')

    #parse the XML file into an "OrderedDict"
    xml = xmltodict.parse(stream.read())

    #iterate through items in the XML object
    for e in xml:
        print(e)