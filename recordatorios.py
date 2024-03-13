

recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]]

# 1. Agregar evento el 2 de Febrero en la segunda ubicacion del diccionario.
recordatorios.append(['2021-02-02', '06:00', 'Empezar el año'])

# 2. Editar el evento del 15 de Julio para que sea el 16 de Julio.
recordatorios[2] = ['2021-07-16', "13:00", "No hacer nada es feriado"]

#for evento in recordatorios:
 #   if evento[0] == '2021-07-15':
  #      evento[0] = '2021-07-16'

# 3. Eliminar el evento del día del trabajo.
del recordatorios [1]

# 4. Agregar una cena de Navidad y de Año Nuevo, ambas a las 22 hrs.
recordatorios.append(['2021-12-24', "22:00", "Cena de Navidad"])
recordatorios.append(['2021-12-31', "22:00", "Cena de Año Nuevo"])

# Orden ascendente lista
recordatorios.sort()

# Output
for evento in recordatorios:
    print(*evento)