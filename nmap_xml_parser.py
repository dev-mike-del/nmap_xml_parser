#! user/bin/env

import xml.etree.ElementTree as ET


def get_root(path):
	return ET.parse(path).getroot()

def get_dict(root):
	d = {root.tag: root.attrib,}
	
	for tag in root.findall('.//'):
		if d.__contains__(tag.tag):
			key = d[tag.tag].__len__() + 1
			d[tag.tag][key] = tag.attrib
		else:
			d[tag.tag] = {1: tag.attrib}

	return d

def get_diff(d1, d2):
	d = {}
	for k,v in d1.items():
		if d1[k] != d2[k]:
			if d.__contains__(k):
				d[k]['d1'] = d1[k]
				d[k]['d2'] = d2[k]
			else:
				d[k] = {'d1': d1[k]}
				d[k]['d2'] = d2[k]

	return d


r1 = get_root('worldstoryboard.xml')
r2 = get_root('worldstoryboard2.xml')

d1 = get_dict(r1)
d2 = get_dict(r2)
diff = get_diff(d1, d2)

