import pandas as pd
import matplotlib.pyplot as plt

url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'
data = pd.read_csv(url)

# Eliminar columnas de un dataset
data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Nombre del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)



''' CONSULTAS'''
'''
PUNTO 1:
    Número de casos de Contagiados en el País.
'''
casos = data['fecha reporte web'].count()
print(f'Número de Contagiados en el País : {casos} casos')

'''
PUNTO 2:
    Número de Municipios Afectados
'''
municipios = data['Nombre municipio'].value_counts()
n_municipios = municipios.count()
print(f'Municipio afectados en el País : {n_municipios} municipios')

'''
PUNTO 3:
Liste los municipios afectados (sin repetirlos)
'''
lista_municipios = list(data['Nombre municipio'].drop_duplicates())
print(f'Lista de municipios afectados: {lista_municipios} ')

'''
PUNTO 4:
    Número de personas que se encuentran en atención en casa
'''
# Normalizamos la columna 'Ubicacion del caso' (Casa)
data.loc[data['Ubicación del caso'] == 'casa'] = 'Casa'
data.loc[data['Ubicación del caso'] == 'CASA'] = 'Casa'
atencion_casa = data.loc[(data['Ubicación del caso'] == 'Casa')].shape[0]
print(f'Atendidos en casa: {atencion_casa} personas ')

'''
PUNTO 5:
    Número de personas que se encuentran recuperados
'''
recuperados = data.loc[(data['Recuperado'] == 'Recuperado')].shape[0]
print(f' Recuperados: {recuperados} personas ')

'''
PUNTO 6:
    Número de personas que han fallecido
'''
# Normalizamos la columna 'Recuperado' (Fallecido)
data.loc[data['Recuperado'] == 'fallecido'] = 'Fallecido'
fallecidos = data.loc[(data['Recuperado'] == 'Fallecido')].shape[0]
print(f' Fallecidos: {fallecidos} personas ')

'''
PUNTO 7:
    Ordenar de Mayor a menor por tipo de caso
'''
ordenado_tipo_caso=data['Tipo de contagio'].value_counts().sort_values(ascending=(False))
print(f'Mayor a menor por tipo de caso \n{ordenado_tipo_caso}')

'''
PUNTO 8:
    Número de departamentos afectados
'''
#Normalizamos columna de departamento
data.loc[data['Nombre departamento'] == 'BOGOTA'] = 'CUNDINAMARCA'
data.loc[data['Nombre departamento'] == 'BARRANQUILLA'] = 'ATLANTICO'
data.loc[data['Nombre departamento'] == 'STA MARTA D.E.'] = 'MAGDALENA'
data.loc[data['Nombre departamento'] == 'CARTAGENA'] = 'BOLIVAR'
data.loc[data['Nombre departamento'] == 'Santander'] = 'SANTANDER'
data.loc[data['Nombre departamento'] == 'Cundinamarca'] = 'CUNDINAMARCA'
data.loc[data['Nombre departamento'] == 'Tolima'] = 'TOLIMA'
data.loc[data['Nombre departamento'] == 'Caldas'] = 'CALDAS'
departamentos = data['Nombre departamento'].value_counts()
n_departamentos = departamentos.count()
print(f'Departamentos afectados en el País : {n_departamentos} departamentos')

'''
PUNTO 9:
    Liste los departamentos afectados(sin repetirlos)
'''
lista_departamentos = list(data['Nombre departamento'].drop_duplicates())
print(f'Lista de departamentos afectados: {lista_departamentos} ')

'''
PUNTO 10:
    Ordene de mayor a menor por tipo de atención
'''
data.loc[data['Ubicación del caso'] == 'casa'] = 'Casa'
data.loc[data['Ubicación del caso'] == 'CASA'] = 'Casa'
ordenado_tipo_atencion = data['Ubicación del caso'].value_counts().sort_values(ascending=(False))
print(f'Mayor a menor por tipo de atención \n{ordenado_tipo_atencion}')

'''
PUNTO 11:
Liste de mayor a menor los 10 departamentos con mas casos de
contagiados
'''
departamentos_casos=data['Nombre departamento'].value_counts().head(10)
print(f'TOP 10 DEPARTAMENTOS CON MAS CASOS \n{departamentos_casos}')

'''
PUNTO 12:
   Liste de mayor a menor los 10 departamentos con mas casos de
fallecidos
'''
data[(data['Estado'] == 'Fallecido')].groupby('Nombre departamento').size().sort_values(ascending=(False)).head(10)

'''
13. Liste de mayor a menor los 10 departamentos con mas casos de
recuperados
14. Liste de mayor a menor los 10 municipios con mas casos de
contagiados
15. Liste de mayor a menor los 10 municipios con mas casos de
fallecidos
16. Liste de mayor a menor los 10 municipios con mas casos de
recuperados
17. Liste agrupado por departamento y en orden de Mayor a menor las
ciudades con mas casos de contagiados
18. Número de Mujeres y hombres contagiados por ciudad por
departamento
19. Liste el promedio de edad de contagiados por hombre y mujeres por
ciudad por departamento
20. Liste de mayor a menor el número de contagiados por país de
procedencia
21. Liste de mayor a menor las fechas donde se presentaron mas
contagios
22. Diga cual es la tasa de mortalidad y recuperación que tiene toda
Colombia
23. Liste la tasa de mortalidad y recuperación que tiene cada
departamento
24. Liste la tasa de mortalidad y recuperación que tiene cada ciudad
25. Liste por cada ciudad la cantidad de personas por atención
26. Liste el promedio de edad por sexo por cada ciudad de contagiados
27. Grafique las curvas de contagio, muerte y recuperación de toda
Colombia acumulados
28. Grafique las curvas de contagio, muerte y recuperación de los 10
departamentos con mas casos de contagiados acumulados
29. Grafique las curvas de contagio, muerte y recuperación de las 10
ciudades con mas casos de contagiados acumulados
30. Liste de mayor a menor la cantidad de fallecidos por edad en toda
Colombia.
31. Liste el porcentaje de personas por atención de toda Colombia
32. Haga un gráfico de barras por atención de toda Colombia
33. Haga un gráfico de barras por Sexo de toda Colombia
34. Haga un gráfico de barras por tipo de toda Colombia
35. Haga un gráfico de barras del número de contagiados, recuperados y
fallecidos por fecha de toda Colombia
'''