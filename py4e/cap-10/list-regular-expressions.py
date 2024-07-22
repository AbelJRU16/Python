import re

#Validar una dirección de correo electrónico:
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

#Validar un número de teléfono:
phone_regex = r'^\+?[1-9]\d{1,14}$'

#Validar una fecha en formato YYYY-MM-DD:
date_regex = r'^\d{4}-\d{2}-\d{2}$'

#Validar una dirección IP (IPv4):
ipv4_regex = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

#Validar una dirección IP (IPv6):
ipv6_regex = r'((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:|((25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])\.)){3}(25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])|:)|(([0-9A-Fa-f]{1,4}:){5}(((:|((25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])\.)){3}(25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])|(:[0-9A-Fa-f]{1,4}|:))|:)|(([0-9A-Fa-f]{1,4}:){4}(:|((25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])\.)){3}(25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])|(:([0-9A-Fa-f]{1,4}:){1,2}|:))|(([0-9A-Fa-f]{1,4}:){3}(((:|((25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])\.)){3}(25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])|(:([0-9A-Fa-f]{1,4}:){1,3}|:))|:)|(([0-9A-Fa-f]{1,4}:){2}(:|((25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])\.)){3}(25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])|(:([0-9A-Fa-f]{1,4}:){1,4}|:))|(([0-9A-Fa-f]{1,4}:){1}(((:|((25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])\.)){3}(25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])|(:([0-9A-Fa-f]{1,4}:){1,5}|:))|:)|(::(((:|((25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])\.)){3}(25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])|(:([0-9A-Fa-f]{1,4}:){1,6}|:))|:)))(%.+)?\s*$'

#Validar una URL:
url_regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

#Validar un código postal (formato general):
postal_code_regex = r'^\d{5}(-\d{4})?$'

#Validar una contraseña (al menos 8 caracteres, una mayúscula, una minúscula, un número y un carácter especial):
password_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'

#Extraer etiquetas HTML:
html_tag_regex = r'<([a-zA-Z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)'

#Encontrar palabras que empiecen con una letra mayúscula:
capital_word_regex = r'\b[A-Z][a-z]*\b'
