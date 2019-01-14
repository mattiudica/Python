import re
str_val = 'Mashim13'

# Validar mediante objeto:
# regex = re.compile('[a-zA-Z0-9]')
# boolVal = regex.match(str_val)
# print(bool(boolVal))

# Validar mediante funcion usando libreria re:
boolVal2 = re.match('[a-zA-Z0-9]',str_val)
print(bool(boolVal2))
