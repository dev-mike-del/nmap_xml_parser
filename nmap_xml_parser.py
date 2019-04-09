#! user/bin/env


# This Python3 script parses an xml file created by the Nmap 
# command "nmap -A -T4 -oX path_to/xml_file_name.xml your_research_target.com"
#
# Substitute "path_to/xml_file_name.xml" and "your_research_target.com" with the 
# correct information.
#
# You can use this script to turn an nmap xml file (specified above) into a python dictionary 
# or you can use it to create a python dictionary of the differences between two different 
# Nmap xml file. 
#
# Once you have an xml file you can run this file in the interactive mode 
# (python3 -i this_script_name.py). Then, use your xml path with the 'get_root(path)'
# function and the result of that with the 'get_dict(root)' function.


# xml.etree.ElementTree — The ElementTree XML API
# https://docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET

# ElementTree function to parse xml and create an xml.etree.ElementTree.Element class instance
def get_root(path):
	return ET.parse(path).getroot()

# Parses xml.etree.ElementTree.Element class instance into a python dictionary
def get_dict(root):
	d = {root.tag: root.attrib,}
	
	for tag in root.findall('.//'):
		if d.__contains__(tag.tag):
			key = d[tag.tag].__len__() + 1
			d[tag.tag][key] = tag.attrib
		else:
			d[tag.tag] = {1: tag.attrib}

	return d

# Creates a dictionary of the difference between two dictionaries (created from this script)
def get_diff(d1, d2):
	d = {}
	for k1,v in d1.items():
		if d1[k1] != d2[k1]:
			if d.__contains__(k1):
				if d1[k1].__len__() > 1:
					for k2,v in d1[k1].items():
						if d1[k1][k2] != d2[k1][k2]:
							d[k1]['d1'] = d1[k1][k2]
							d[k1]['d2'] = d2[k1][k2]
				else:
					d[k1]['d1'] = d1[k1]
					d[k1]['d2'] = d2[k1]
			else:
				if d1[k1].__contains__(1):
					for k2,v in d1[k1].items():
						d[k1] = {'d1': d1[k1][k2]}
						d[k1]['d2'] = d2[k1][k2]
				else:
					for k2,v in d1[k1].items():
						d[k1] = {'d1': {d1[k1][k2]}}
						d[k1]['d2'] = d2[k1][k2]
					d[k1] = {'d1': d1[k1]}
					d[k1]['d2'] = d2[k1]

	return d
