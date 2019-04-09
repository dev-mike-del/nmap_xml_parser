#! user/bin/env


# xml.etree.ElementTree — The ElementTree XML API
# https://docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET

# ElementTree function to parse xml and create an xml.etree.ElementTree.Element class instance
def get_root(path):
	return ET.parse(path).getroot()

# Parses xml.etree.ElementTree.Element class instance into a python dictionary
def get_dict(root):
	dict1 = {root.tag: root.attrib,}
	
	for tag in root.findall('.//'):
		if dict1.__contains__(tag.tag):
			key = dict1[tag.tag].__len__() + 1
			dict1[tag.tag][key] = tag.attrib
		else:
			dict1[tag.tag] = {1: tag.attrib}

	return dict1

# Creates a dictionary of the difference between two dictionaries (created from this script)
def get_diff(dict1, dict2):
	dict3 = {}
	for key1,value in dict1.items():
		if dict1[key1] != dict2[key1]:
			if dict3.__contains__(key1):
				if dict1[key1].__len__() > 1:
					for key2,value in dict1[key1].items():
						if dict1[key1][key2] != dict2[key1][key2]:
							dict3[key1]['dict1'] = dict1[key1][key2]
							dict3[key1]['dict2'] = dict2[key1][key2]
				else:
					dict3[key1]['dict1'] = dict1[key1]
					dict3[key1]['dict2'] = dict2[key1]
			else:
				if dict1[key1].__contains__(1):
					for key2,value in dict1[key1].items():
						dict3[key1] = {'dict1': dict1[key1][key2]}
						dict3[key1]['dict2'] = dict2[key1][key2]
				else:
					for key2,value in dict1[key1].items():
						dict3[key1] = {'dict1': {dict1[key1][key2]}}
						dict3[key1]['dict2'] = dict2[key1][key2]
					dict3[key1] = {'dict1': dict1[key1]}
					dict3[key1]['dict2'] = dict2[key1]

	return dict3
