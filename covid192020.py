++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+   #Código adaptado após consulta de varios tuturiais publicados na web
+   #Código para obtenção de dados actuais sobre os casos confirmados de Covid19
+   #Em actualização...
+   ------------------------
+   #Twitter: @lcmadeira / @uedbn
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import pandas as pd
import geopandas as gpd

#Importar dados do https://www.worldometers.info/coronavirus/
dados = pd.read_html('https://www.worldometers.info/coronavirus/')
#print(dados) -> dados do tipo lista

#Converter a Lista para DataFrame
for dados_casos in dados:
    print(dados_casos)

#Limpar os Dados Extraidos
#Ficam apenas as colunas "Country,Other", "TotalCases", "TotalDeaths" e "TotalRecovered"
dados_casos = dados_casos[['Country,Other', 'TotalCases', 'TotalDeaths', 'TotalRecovered']]

#Importar Mapa Mundo(.shp)
mapa_shp = gpd.read_file(r'caminho para o shapefile')

#Verificar concordancia dos nomes dos paises entre os dois ficheiros
for paises in dados_casos['Country,Other'].tolist():
     mapa_shp_lista = mapa_shp['NAME'].tolist()
     if paises in mapa_shp_lista:
         pass
     else:
         print(paises + ' não está na lista de paises do .shp')

#Normalizar os nomes dos países no ficheiro .shp
mapa_shp.replace('Korea, Republic of', 'S. Korea', inplace = True)
mapa_shp.replace('Iran (Islamic Republic of)', 'Iran', inplace = True)
mapa_shp.replace('United States', 'USA', inplace = True)
mapa_shp.replace('United Kingdom', 'U.K.', inplace = True)
mapa_shp.replace('United Arab Emirates', 'U.A.E.', inplace = True)
mapa_shp.replace('Viet Nam', 'Vietnam', inplace = True)
mapa_shp.replace('Macau', 'Macao', inplace = True)
mapa_shp.replace('The former Yugoslav Republic of Macedonia', 'North Macedonia', inplace = True)
mapa_shp.replace('Czech Republic', 'Czechia', inplace = True)
mapa_shp.replace('Palestine', 'State of Palestine', inplace = True)
mapa_shp.replace('Republic of Moldova', 'Moldova', inplace =  True)
mapa_shp.replace('Holy See (Vatican City)', 'Vatican City', inplace = True)

#Renomear o nome da coluna(Paises) no ficheiro dados_casos
dados_casos.rename(columns = {'Country,Other': 'NAME'}, inplace = True)

#Exportar tabela em formato .csv (Opcional)
#dados_casos.to_csv(r'caminho para guardar o ficheiro .csv')

#Merge entre dados_casos e mapa_shp
merge = mapa_shp.merge(dados_casos, on = 'NAME')
#print(merge)

#Exportar o Merge para .shp
merge.to_file(r'caminho onde vai ser guardado o *.shp')
