import re,sys
from xml.dom import minidom

if len(sys.argv) != 2:
    print('usage : wireize-svg.py <path_to_originFile> \nYou must specify the path to the origin file as the first arg')
    sys.exit(1)

doc = minidom.parse(sys.argv[1])
path_strings = [path.getAttribute('d') for path
                in doc.getElementsByTagName('path')]
doc.unlink()

pattern = ('(?=.{1,})([a-zA-Z]|-?[\d]{,3}\.?[\d]{,3})')

for path in path_strings:
	vertices = re.split(pattern, path)
	for i in range(len(vertices)):
		print(vertices[i])
	
