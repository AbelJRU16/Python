import xml.etree.ElementTree as ET

fhand = open('cosa.xml', 'r') #get the file

datos = fhand.read()

fhand.close()
cosa = ET.fromstring(datos)
lst = cosa.findall('usuarios/usuario')
print('Total de usuarios:', len(lst))

for item in lst:
    print('Nombre', item.find('nombre').text)
    print('Id', item.find('id').text)
    print('Atributo', item.get('x'))
