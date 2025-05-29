#Fechas

from datetime import datetime, timedelta #, time (para zonas horarias)

now = datetime.now()
print(f"Fecha y hora actual: {now}")

specific_date = datetime(2025, 10, 4)
print(f"Fecha y hora específica: {specific_date}")

#Formatear fechas
#metodo strftime()

format_date = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"Fecha formateada: {format_date}")

#Operaciones con fechas
yesterday = datetime.now() - timedelta(days=1)
print(f"Ayer: {yesterday}")

last_week = datetime.now() - timedelta(weeks=1)
print(f"La semana pasada: {last_week}")

#Obtener componentes de una fecha

year = now.year
print(year)

month = now.month
print(month)

#Calcular diferencia entre fechas

date1 = datetime.now()
date2 = datetime(2025,2,12,15,30,0) 
difference = date1 - date2
print(f"Diferencia entre las fechas: {difference}")

#Fechas en otro idioma

import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

format_date = now.strftime("%A/%B/%Y %H:%M:%S")
print(f"Fecha formateada: {format_date}")