import pandas as pd
import matplotlib.pyplot as plt

url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'
data = pd.read_csv(url)

'''Eliminar columnas de un dataset'''
data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)

'''Normalizaciones en columna Departamento'''
data.loc[data['Nombre departamento'] == 'Santander', 'Nombre departamento'] = 'SANTANDER'
data.loc[data['Nombre departamento'] == 'Cundinamarca', 'Nombre departamento'] = 'CUNDINAMARCA'
data.loc[data['Nombre departamento'] == 'Tolima', 'Nombre departamento'] = 'TOLIMA'
data.loc[data['Nombre departamento'] == 'Caldas', 'Nombre departamento'] = 'CALDAS'
data.loc[data['Nombre departamento'] == 'BARRANQUILLA', 'Nombre departamento'] = 'ATLANTICO'
data.loc[data['Nombre departamento'] == 'STA MARTA D.E.', 'Nombre departamento'] = 'MAGDALENA'
data.loc[data['Nombre departamento'] == 'CARTAGENA', 'Nombre departamento'] = 'BOLIVAR'
data.loc[data['Nombre departamento'] == 'BOGOTA', 'Nombre departamento'] = 'CUNDINAMARCA'

'''Normalizaciones en columna Sexo'''
data.loc[data['Sexo'] == 'm','Sexo'] = 'M'
data.loc[data['Sexo'] == 'f','Sexo'] = 'F'

'''Normalizar la columna de Ubicación del caso '''
data.loc[data['Ubicación del caso'] == 'casa','Ubicación del caso'] = 'Casa'
data.loc[data['Ubicación del caso'] == 'CASA','Ubicación del caso'] = 'Casa'

'''Normalizar la columna de Estado '''
data.loc[data['Estado'] == 'leve','Estado'] = 'Leve'
data.loc[data['Estado'] == 'LEVE','Estado'] = 'Leve'

'''Normalizamos la columna Recuperado '''
data.loc[data['Recuperado'] == 'fallecido','Recuperado'] = 'Fallecido'

print('*'*50)
print("                   CONSULTAS                     ")
print('*'*50)
''' CONSULTAS'''
'''
PUNTO 1:
    Número de casos de Contagiados en el País.
'''
casos = data['fecha reporte web'].count()
print(f'Número de Contagiados en el País : {casos} casos')
print('*'*50)
'''
PUNTO 2:
    Número de Municipios Afectados
'''
municipios = data['Nombre municipio'].value_counts()
n_municipios = municipios.count()
print(f'Municipio afectados en el País : {n_municipios} municipios')
print('*'*50)
'''
PUNTO 3:
Liste los municipios afectados (sin repetirlos)
'''
lista_municipios = list(data['Nombre municipio'].drop_duplicates())
print(f'Lista de municipios afectados: {lista_municipios} ')
print('*'*50)
'''
PUNTO 4:
    Número de personas que se encuentran en atención en casa
'''
atencion_casa = data.loc[(data['Ubicación del caso'] == 'Casa')].shape[0]
print(f'Atendidos en casa: {atencion_casa} personas ')
print('*'*50)
'''
PUNTO 5:
    Número de personas que se encuentran recuperados
'''
recuperados = data.loc[(data['Recuperado'] == 'Recuperado')].shape[0]
print(f' Recuperados: {recuperados} personas ')
print('*'*50)
'''
PUNTO 6:
    Número de personas que han fallecido
'''
fallecidos = data.loc[(data['Recuperado'] == 'Fallecido')].shape[0]
print(f' Fallecidos: {fallecidos} personas ')
print('*'*50)
'''
PUNTO 7:
    Ordenar de Mayor a menor por tipo de caso
'''
ordenado_tipo_caso=data['Tipo de contagio'].value_counts().sort_values(ascending=(False))
print(f'Mayor a menor por tipo de caso \n{ordenado_tipo_caso}')
print('*'*50)
'''
PUNTO 8:
    Número de departamentos afectados
'''
departamentos = data['Nombre departamento'].value_counts()
n_departamentos = departamentos.count()
print(f'Departamentos afectados en el País : {n_departamentos} departamentos')
print('*'*50)
'''
PUNTO 9:
    Liste los departamentos afectados(sin repetirlos)
'''
lista_departamentos = list(data['Nombre departamento'].drop_duplicates())
print(f'Lista de departamentos afectados: {lista_departamentos} ')
print('*'*50)
'''
PUNTO 10:
    Ordene de mayor a menor por tipo de atención
'''
ordenado_tipo_atencion = data['Ubicación del caso'].value_counts().sort_values(ascending=(False))
print(f'Mayor a menor por tipo de atención \n{ordenado_tipo_atencion}')
print('*'*50)
'''
PUNTO 11:
Liste de mayor a menor los 10 departamentos con mas casos de
contagiados
'''
departamentos_casos=data['Nombre departamento'].value_counts().head(10)
print(f'TOP 10 DEPARTAMENTOS CON MÁS CASOS \n{departamentos_casos}')
print('*'*50)
'''
PUNTO 12:
   Liste de mayor a menor los 10 departamentos con mas casos de
fallecidos
'''
departamentos_muertos=data[(data['Estado'] == 'Fallecido')].groupby(['Nombre departamento']).size().sort_values(ascending=(False)).head(10)
print(f'TOP 10 DEPARTAMENTOS CON MÁS FALLECIDOS \n{departamentos_muertos}')
print('*'*50)
'''
PUNTO 13:
 Liste de mayor a menor los 10 departamentos con mas casos de
recuperados
'''
departamentos_recuperados=data[(data['Recuperado'] == 'Recuperado')].groupby(['Nombre departamento']).size().sort_values(ascending=(False)).head(10)
print(f'TOP 10 DEPARTAMENTOS CON MÁS RECUPERADOS \n{departamentos_recuperados}')
print('*'*50)
'''
PUNTO 14: 
Liste de mayor a menor los 10 municipios con mas casos de
contagiados
'''
municipios_casos=data['Nombre municipio'].value_counts().head(10)
print(f'TOP 10 MUNICIPIOS CON MÁS CASOS \n{municipios_casos}')
print('*'*50)
'''
 PUNTO 15:
Liste de mayor a menor los 10 municipios con mas casos de
fallecidos
'''
municipios_muertos=data[(data['Estado'] == 'Fallecido')].groupby(['Nombre municipio']).size().sort_values(ascending=(False)).head(10)
print(f'TOP 10 MUNICIPIOS CON MÁS FALLECIDOS \n{municipios_muertos}')
print('*'*50)
'''
PUNTO 16:
Liste de mayor a menor los 10 municipios con mas casos de
recuperados
'''
municipios_recuperados=data[(data['Recuperado'] == 'Recuperado')].groupby(['Nombre municipio']).size().sort_values(ascending=(False)).head(10)
print(f'TOP 10 MUNICIPIOS CON MÁS RECUPERADOS \n{municipios_recuperados}')
print('*'*50)
'''
PUNTO 17: 
Liste agrupado por departamento y en orden de Mayor a menor las
ciudades con mas casos de contagiados
'''
casos_agrupados=data.groupby(['Nombre departamento','Nombre municipio']).size().sort_values(ascending=(False)).head(10)
print(casos_agrupados)
print('*'*50)
'''
PUNTO 18:
Número de Mujeres y hombres contagiados por ciudad por
departamento
'''
casos_agrupados_sexos=data.groupby(['Nombre departamento','Nombre municipio','Sexo']).size().sort_values(ascending=(False)).head(10)
print(casos_agrupados_sexos)
print('*'*50)
'''
PUNTO 19:
Liste el promedio de edad de contagiados por hombre y mujeres por
ciudad por departamento'''
edades_prom = data.groupby(['Nombre departamento','Nombre municipio','Sexo'])['Edad'].agg(['mean'])
#Source: stackoverflow 
#https://stackoverflow.com/questions/41040132/pandas-groupby-count-and-mean-combined
print(f'Promedio de edad de contagiados por hombre y mujeres:\n{edades_prom}')
'''
PUNTO 20:
Liste de mayor a menor el número de contagiados por país de
procedencia
'''
ordenado_contagios_exterior = data['Nombre del país'].value_counts().sort_values(ascending=(False))
print(f'Mayor a menor por contagiados por país de procedencia \n{ordenado_contagios_exterior}')
print('*'*50)
'''
PUNTO 21:
Liste de mayor a menor las fechas donde se presentaron mas
contagios
'''
ordenado_fecha_contagios = data['fecha reporte web'].value_counts().sort_values(ascending=(False))
print(f'Mayor a menor por contagiados por fecha \n{ordenado_fecha_contagios}')
print('*'*50)
'''
PUNTO 22:
Diga cual es la tasa de mortalidad y recuperación que tiene toda
Colombia
'''
cantidad_casos = data.shape[0]
tasa_mortalidad =  fallecidos / cantidad_casos * 100
tasa_recuperacion = recuperados / cantidad_casos * 100
print("Colombia")
print(f'Tasa de mortalidad: {tasa_mortalidad}\nTasa de recuperación: {tasa_recuperacion}')
print('*'*50)
'''
23. Liste la tasa de mortalidad y recuperación que tiene cada
departamento
'''
departamento_mortalidad = (data[data['Estado'] == 'Fallecido'].groupby('Nombre departamento').size() / len(data)) * 100
print(f'Tasa de mortalidad por Departamento:\n{departamento_mortalidad}')
departamento_recuperacion = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size() / len(data)) * 100
print(f'Tasa de recuperación por departamento:\n{departamento_recuperacion}')
print('*'*50)
'''
24. Liste la tasa de mortalidad y recuperación que tiene cada ciudad
'''
municipio_mortalidad = (data[data['Estado'] == 'Fallecido'].groupby('Nombre municipio').size() / len(data)) * 100
print(f'Tasa de mortalidad por municipio:\n{municipio_mortalidad}')
municipio_recuperacion = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size() / len(data)) * 100
print(f'Tasa de recuperación por municipio:\n{municipio_recuperacion}')
print('*'*50)

'''
25. Liste por cada ciudad la cantidad de personas por atención
'''
tipo_atencion = data.groupby(['Nombre municipio','Ubicación del caso']).size()
print(f'Ciudad la cantidad de personas por atención \n{tipo_atencion}')
print('*'*50)
'''
PUNTO 26:
 Liste el promedio de edad por sexo por cada ciudad de contagiados
'''
edades_prom_ciudad = data.groupby(['Nombre municipio','Sexo'])['Edad'].agg(['mean'])
#Source: stackoverflow 
#https://stackoverflow.com/questions/41040132/pandas-groupby-count-and-mean-combined
print(f'Promedio de edad de contagiados por ciudad:\n{edades_prom_ciudad}')
'''
PUNTO 27:
 Grafique las curvas de contagio, muerte y recuperación de toda
Colombia acumulados
'''
plt.title('Las curva de contagio en colombia')
data.groupby('Fecha de diagnóstico').size().plot()
plt.title('Las curva de muerte en colombia')
data[ (data['Estado'] == 'Fallecido')].groupby('Fecha de diagnóstico').size().plot()
plt.title('Las curva de recuperacion en colombia')
data[ (data['Recuperado'] == 'Recuperado')].groupby('Fecha de diagnóstico').size().plot()
'''
PUNTO 28:
Grafique las curvas de contagio, muerte y recuperación de los 10
departamentos con mas casos de contagiados acumulados
'''
plt.title('Las curva de contagio en colombia: TOP 10 DEPARTAMENTOS')
data['Nombre departamento'].value_counts().head(10).plot()
plt.title('Las curva de muerte en colombia: TOP 10 DEPARTAMENTOS')
data[(data['Estado'] == 'Fallecido')].groupby(['Nombre departamento']).size().sort_values(ascending=(False)).head(10).plot()
plt.title('Las curva de recuperacion en colombia: TOP 10 DEPARTAMENTOS')
data[(data['Recuperado'] == 'Recuperado')].groupby(['Nombre departamento']).size().sort_values(ascending=(False)).head(10).plot()
'''
PUNTO 29:
Grafique las curvas de contagio, muerte y recuperación de las 10
ciudades con mas casos de contagiados acumulados
'''
plt.title('Las curva de contagio en colombia: TOP 10 CIUDADES')
data['Nombre municipio'].value_counts().head(10).plot()
plt.title('Las curva de muerte en colombia: TOP 10 CIUDADES')
data[(data['Estado'] == 'Fallecido')].groupby(['Nombre municipio']).size().sort_values(ascending=(False)).head(10).plot()
plt.title('Las curva de recuperacion en colombia: TOP 10 CIUDADES')
data[(data['Recuperado'] == 'Recuperado')].groupby(['Nombre municipio']).size().sort_values(ascending=(False)).head(10).plot()
'''
PUNTO 30:
    Liste de mayor a menor la cantidad de fallecidos por edad en toda
Colombia.
'''
fallecidos_edad=data[(data['Estado'] == 'Fallecido')].groupby(['Edad']).size().sort_values(ascending=(False))
print(f'Fallecidos por edad en toda Colombia. \n{fallecidos_edad}')
print('*'*50)
'''
PUNTO 31:
Liste el porcentaje de personas por atención de toda Colombia
'''
porcentajes_atencion = data.groupby('Ubicación del caso').size() / len(data) * 100
print(f'Porcentaje de personas por atención de toda Colombia:\n{porcentajes_atencion}')
print('*'*50)
'''
32. Haga un gráfico de barras por atención de toda Colombia
'''
plt.title('tipo de  atencion por covid de toda Colombia')
atencion = ['Casa','Fallecidos','Hospital','UCI']
cantidad_casos=[data.loc[(data['Ubicación del caso'] == 'Casa')].shape[0],data.loc[(data['Ubicación del caso'] == 'Fallecido')].shape[0],data.loc[(data['Ubicación del caso'] == 'Hospital')].shape[0],data.loc[(data['Ubicación del caso'] == 'Hospital UCI')].shape[0]]
plt.barh(atencion,cantidad_casos, color="green")
plt.ylabel('Tipo de atencion')
plt.xlabel('Casos')
plt.show()
'''
33. Haga un gráfico de barras por Sexo de toda Colombia
'''
plt.title('Contagiados por sexo')
sexo = ['F','M']
cantidad = [data.loc[(data['Sexo'] == 'F')].shape[0],data.loc[(data['Sexo'] == 'M')].shape[0]]
plt.barh(sexo,cantidad, color="green")
plt.ylabel('Generos')
plt.xlabel('Casos')
plt.show()
'''
34. Haga un gráfico de barras por tipo de toda Colombia
'''
plt.title('Por tipo ')
atencion_tipo = ['Tiempo','PCR']
cantidad_tipo=[data.loc[(data['Tipo de recuperación'] == 'Tiempo')].shape[0],data.loc[(data['Tipo de recuperación'] == 'PCR')].shape[0]]
plt.barh(atencion_tipo,cantidad_tipo, color="green")
plt.ylabel('Tipo')
plt.xlabel('Cantidad')
plt.show()
'''
35. Haga un gráfico de barras del número de contagiados, recuperados y
fallecidos por fecha de toda Colombia
'''
plt.title('Múmero de contagiados, recuperados y fallecidos por fecha de toda Colombia')
tipo = ['Contagiados','Fallecidos','Recuperados']
datos=[data.shape[0],data.loc[(data['Estado'] == 'Fallecido')].shape[0],data.loc[(data['Recuperado'] == 'Recuperado')].shape[0]]
plt.barh(tipo,datos, color="green")
plt.ylabel('Personas')
plt.xlabel('Casos')
plt.show()
