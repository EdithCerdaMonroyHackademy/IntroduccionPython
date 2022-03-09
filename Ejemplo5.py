#Ejemplo 5 Python
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

def DiasDelMes(mes):
  for month in months:
    if mes not in months:
      return 0
    return 1
      
def ValidarFecha(mes,dia):
  respuesta=DiasDelMes(mes)
  if respuesta==1:
    if dia>=1 and dia<=30:
      return True
    else:
      return False
  else:
    return False    
    
        
      

m= input("Ingresa el Mes:")
d= int(input("Ingresa el dia:"))
ValidarFecha(m,d)

