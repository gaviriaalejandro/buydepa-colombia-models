import os
import copy
import pandas as pd
import numpy as np
import geopandas as gpd
import pickle
import mysql.connector as sql
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tqdm import tqdm
from shapely.geometry import  Point
from sqlalchemy import create_engine 
from sqlalchemy.types import VARCHAR,INT,DATETIME
from sqlalchemy.dialects.mysql import DOUBLE,LONGTEXT, JSON
from multiprocessing.dummy import Pool
from sklearn.preprocessing import LabelEncoder
tqdm.pandas()

import sys
sys.path.insert(0, r'D:\Dropbox\Empresa\Buydepa\COLOMBIA\PRICING MODEL\ANN')
from ANN import ANN

sys.path.insert(0, r'D:\Dropbox\Empresa\Buydepa\COLOMBIA\PRICING MODEL\XGBOOSTING')
from ModelV2 import xgboostingmodel

path     = [r"D:\Dropbox\Empresa\Buydepa\COLOMBIA\PRICING MODEL\RESULTADOS",
            r"D:\Dropbox\Empresa\Buydepa\PROYECTOS\proceso\appcolombia\data"]

runann   = False

user     = 'buydepa'
password = 'GWc42X887heD'
host     = 'buydepa-market.cy47rcxrw2g5.us-east-1.rds.amazonaws.com'
schema   = 'market'
    

def remove_tz(x):
    try:    return x.replace(tzinfo=None)
    except: return x

def LB(x):
    return x.quantile(0.025)

def UB(x):
    return x.quantile( 0.975)

def getdatafilter(datamarket,tiponegocio,months=15):
    if 'venta' in tiponegocio.lower():
        valormt2min = 2000000
        valormt2max = 20000000
    if 'arriendo' in tiponegocio.lower():
        valormt2min = 10000
        valormt2max = 100000     
    
    datestr     = datetime.today() + relativedelta(months=-months)
    datestr     = datestr.strftime("%Y-%m-%d")
    datamarket['fecha_inicial'] = datamarket['fecha_inicial'].apply(lambda x: remove_tz(x))
    datamarket                  = datamarket[datamarket['fecha_inicial']>=datestr]
    dataconjuntos               = datamarket[(datamarket['valormt2']>=valormt2min) & (datamarket['valormt2']<=valormt2max)]
    
    # Filtro por quantile por barrio
    datapaso         = dataconjuntos.groupby('scacodigo').agg({'valormt2': [LB, UB]})
    datapaso.columns = ['LB','UB']
    datapaso         = datapaso.reset_index()
    dataconjuntos    = dataconjuntos.merge(datapaso,on='scacodigo',how='left',validate='m:1') 
    dataconjuntos    = dataconjuntos[(dataconjuntos['valormt2']>=dataconjuntos['LB']) & (dataconjuntos['valormt2']<=dataconjuntos['UB']) ]
    dataconjuntos.drop(columns=['LB','UB'],inplace=True)
    return dataconjuntos

def truncateddata(datamarket):
    idd        = (datamarket['habitaciones'].isin([1,2,3,4,5,6])) & (datamarket['banos'].isin([1,2,3,4,5,6,7])) & (datamarket['garajes'].isin([0,1,2,3,4,5])) & (datamarket['estrato'].isin([1,2,3,4,5,6]))
    datamarket = datamarket[idd]
    idd        = (datamarket['areaconstruida']>=25) & (datamarket['areaconstruida']<=500)
    datamarket = datamarket[idd]
    return datamarket
    
def valorizacion(datavalorizacion):

    plazo        = datetime.today() + relativedelta(years=-1,months=-3)
    minimo       = plazo.strftime("%Y-%m-%d")
    plazo        = datetime.today()  + relativedelta(years=-1)
    maximo       = plazo.strftime("%Y-%m-%d")
    idd          = (datavalorizacion['fecha_inicial']>=minimo) & (datavalorizacion['fecha_inicial']<=maximo)
    datainicial  = datavalorizacion[idd]

    plazo        = datetime.today()  + relativedelta(months=-3)
    minimo       = plazo.strftime("%Y-%m-%d")
    idd          = datavalorizacion['fecha_inicial']>=minimo
    datalast     = datavalorizacion[idd]
    
    dataparte1 = datainicial.groupby(['scacodigo']).agg({'valormt2':['median','count']}).reset_index()
    dataparte1.columns = ['scacodigo','valormt2_inicial','obs_inicial']
    dataparte2 = datalast.groupby(['scacodigo']).agg({'valormt2':['median','count']}).reset_index()
    dataparte2.columns = ['scacodigo','valormt2_final','obs_final']
    datafinal   = dataparte2.merge(dataparte1,on='scacodigo',how='left',validate='1:1')
    datafinal['valorizacion'] = datafinal['valormt2_final']/datafinal['valormt2_inicial']-1
    datafinal['tipo']         = 'barrio'
    
    dataparte1 = datainicial.groupby(['scacodigo','habitaciones','banos','garajes']).agg({'valormt2':['median','count']}).reset_index()
    dataparte1.columns = ['scacodigo','habitaciones','banos','garajes','valormt2_inicial','obs_inicial']
    dataparte2 = datalast.groupby(['scacodigo','habitaciones','banos','garajes']).agg({'valormt2':['median','count']}).reset_index()
    dataparte2.columns = ['scacodigo','habitaciones','banos','garajes','valormt2_final','obs_final']
    datapaso   = dataparte2.merge(dataparte1,on=['scacodigo','habitaciones','banos','garajes'],how='left',validate='1:1')
    datapaso['valorizacion'] = datapaso['valormt2_final']/datapaso['valormt2_inicial']-1
    datapaso['tipo']         = 'complemento'
    idd                       = (datapaso['habitaciones'].isin([1,2,3,4,5])) & (datapaso['banos'].isin([1,2,3,4,5])) & (datapaso['garajes'].isin([0,1,2,3,4]))
    datapaso                  = datapaso[idd]
    datavalorizacion          = datafinal.append(datapaso)

    return datavalorizacion

def valormt2_sector(data):
    datafinal          = data.groupby(['scacodigo']).agg({'valormt2':['median','count']}).reset_index()
    datafinal.columns  = ['scacodigo','valormt2','obs']
    datafinal['tipo']  = 'barrio'
    datapaso           = data.groupby(['scacodigo','habitaciones','banos','garajes']).agg({'valormt2':['median','count']}).reset_index()
    datapaso.columns   = ['scacodigo','habitaciones','banos','garajes','valormt2','obs']
    datapaso['tipo']   = 'complemento'
    idd                = (datapaso['habitaciones'].isin([1,2,3,4,5])) & (datapaso['banos'].isin([1,2,3,4,5])) & (datapaso['garajes'].isin([0,1,2,3,4]))
    datapaso           = datapaso[idd]
    datavalormt2sector = datafinal.append(datapaso)
    return datavalormt2sector

def estadisticas_sector(data):
    plazo        = datetime.today() + relativedelta(years=-1)
    plazo        = plazo.strftime("%Y-%m-%d")
    datapaso     = data[data['fecha_inicial']>=plazo]
    datapaso['rango_area'] = pd.cut(datapaso['areaconstruida'],[0,50,80,100,150,200,300,np.inf],labels=['50 o menos mt2','50 a 80 mt2','80 a 100 mt2','100 a 150 mt2','150 a 200 mt2','200 a 300 mt2','300 o más mt2'])
    datapaso['id'] = 1
    
    # Rango de area
    datafinal         = datapaso.groupby(['scacodigo','rango_area'])['id'].count().reset_index()
    datafinal.columns = ['scacodigo','variable','valor']
    datafinal['tipo'] = 'areaconstruida'
    
    # Habitaciones
    idd = datapaso['habitaciones'].isin([1,2,3,4,5])
    v   = datapaso[idd].groupby(['scacodigo','habitaciones'])['id'].count().reset_index()
    v.columns = ['scacodigo','variable','valor']
    v['tipo'] = 'habitaciones'
    datafinal = datafinal.append(v)
    
    # Banos
    idd = datapaso['banos'].isin([1,2,3,4,5])
    v   = datapaso[idd].groupby(['scacodigo','banos'])['id'].count().reset_index()
    v.columns = ['scacodigo','variable','valor']
    v['tipo'] = 'banos'
    datafinal = datafinal.append(v)
    
    # Garajes
    idd = datapaso['garajes'].isin([0,1,2,3,4,5])
    v   = datapaso[idd].groupby(['scacodigo','garajes'])['id'].count().reset_index()
    v.columns = ['scacodigo','variable','valor']
    v['tipo'] = 'garajes'
    datafinal = datafinal.append(v)    
    
    return datafinal

def data2gridshp(data,tiponegocio):   
    # Archivo donde se construye el grid: D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\_BUILDING FUNNEL DATA\bogota_grid_shp
    datagrid          = gpd.read_file(r"D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\shape files\BOGOTA\version_2022\bogota-grid\BogotaGrid.shp",encoding = 'utf-8')
    datagrid['id']    = datagrid['id'].astype(int)
    datagrid.to_file(r'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DESARROLLO\proyecto-opensource-buydepa\data\BogotaGrid.shp')
    data              = data[(data['latitud'].notnull()) & (data['longitud'].notnull())]
    data['geometry']  = data.apply(lambda x: Point(x['longitud'],x['latitud']),axis=1)
    data              = gpd.GeoDataFrame(data, geometry='geometry')
    data              = gpd.sjoin(data, datagrid, how="left", op="within")
    data              = data[['id','scacodigo','valormt2','fecha_inicial','areaconstruida','habitaciones','banos','garajes','estrato']]
    return data

def upload_data(df,table,dtype):   
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{schema}')
    df.to_sql(f'{table}_paso',engine,if_exists='append', index=False,chunksize=1000,dtype=dtype)

def data2Mysql(datatosql,table_name):

    dtype      = {}
    formatlist = {'id': 'int', 'scacodigo': 'varchar', 'valormt2': 'double', 'fecha_inicial': 'datetime', 'areaconstruida': 'double', 'habitaciones': 'int', 'banos': 'int', 'garajes': 'int', 'estrato': 'int', 'obs': 'int', 'tipo': 'varchar', 'valormt2_final': 'double', 'obs_final': 'int', 'valormt2_inicial': 'double', 'obs_inicial': 'int', 'valorizacion': 'double', 'variable': 'varchar', 'valor': 'int', 'direccion': 'varchar', 'descripcion': 'longtext', 'fuente': 'varchar', 'codigoweb': 'varchar', 'url': 'longtext', 'available': 'int', 'tipoinmueble': 'varchar', 'tiponegocio': 'varchar', 'antiguedad': 'int', 'vetustez': 'int', 'tiempodeconstruido': 'varchar', 'valorventa': 'double', 'valorarriendo': 'double', 'piso': 'int', 'valoradministracion': 'double', 'latitud': 'double', 'longitud': 'double', 'dpto_ccdgo': 'varchar', 'dpto_cnmbr': 'varchar', 'mpio_ccdgo': 'varchar', 'mpio_cnmbr': 'varchar', 'locnombre': 'varchar', 'loccodigo': 'varchar', 'upzcodigo': 'varchar', 'upznombre': 'varchar', 'upznumero': 'int', 'scanombre': 'varchar', 'cpob_ccdgo': 'varchar', 'setu_ccnct': 'varchar', 'secu_ccnct': 'varchar', 'tipo_cliente': 'varchar', 'inmobiliaria': 'varchar', 'telefono1': 'varchar', 'telefono2': 'varchar', 'telefono3': 'varchar', 'telefono4': 'varchar', 'telefono5': 'varchar', 'email1': 'varchar', 'email2': 'varchar', 'coddir': 'varchar', 'code': 'varchar', 'img1': 'longtext', 'img2': 'longtext', 'img3': 'longtext', 'img4': 'longtext', 'img5': 'longtext', 'img6': 'longtext', 'img7': 'longtext', 'img8': 'longtext', 'img9': 'longtext', 'img10': 'longtext', 'img11': 'longtext', 'img12': 'longtext', 'img13': 'longtext', 'img14': 'longtext', 'img15': 'longtext', 'imagen_principal': 'longtext'}
    for i in list(datatosql):
        if i in list(formatlist):
            value = formatlist[i]
            if value=='varchar':
                nlength = datatosql[i].apply(lambda x: len(str(x))).max()
                if nlength>40: nlength += 10
                dtype.update({i: VARCHAR(nlength)})
            if value=='longtext':
                dtype.update({i: LONGTEXT})
            if value=='double':                
                datatosql[i] = pd.to_numeric(datatosql[i],errors='coerce')
                dtype.update({i: DOUBLE})                
            if value=='int':
                datatosql[i] = pd.to_numeric(datatosql[i],errors='coerce')
                dtype.update({i: INT})            
            if value=='datetime': 
                datatosql[i] = pd.to_datetime(datatosql[i],errors='coerce')
                dtype.update({i: DATETIME}) 
    
    # Si existe la tabla paso, borrarla
    db_connection = sql.connect(user=user, password=password, host=host, database=schema)
    cursor        = db_connection.cursor()
    cursor.execute(f"SHOW TABLES LIKE '{table_name}_paso'")
    table_exists = cursor.fetchone()
    if table_exists:
        cursor.execute(f"DROP TABLE {schema}.{table_name}_paso")
        db_connection.commit()
    db_connection.close()
    
    # Subir la primera fila para crear la tabla
    upload_data(datatosql.iloc[[0]],table_name,dtype)
    db_connection = sql.connect(user=user, password=password, host=host, database=schema)
    cursor        = db_connection.cursor()
    cursor.execute(f"TRUNCATE {schema}.{table_name}_paso")
    db_connection.commit()
    db_connection.close()

    # Subir toda la data
    pool          = Pool(10)
    db_connection = sql.connect(user=user, password=password, host=host, database=schema)
    futures       = [] 
    datadivided   = [datatosql[i:i + datatosql.shape[0]//10] for i in range(0, datatosql.shape[0], datatosql.shape[0]//10)]
    for x in datadivided:
        futures.append(pool.apply_async(upload_data,args = (x,table_name,dtype, )))
    for future in tqdm(futures):
        future.get()

    lista = [
        f"DROP TABLE `{schema}`.`{table_name}`",
        f"ALTER TABLE `{schema}`.`{table_name}_paso` RENAME TO  `{schema}`.`{table_name}`",
        ]
    db_connection = sql.connect(user=user, password=password, host=host, database=schema)
    cursor        = db_connection.cursor()
    for i in tqdm(lista): 
        try:
            cursor.execute(i)
            db_connection.commit()
        except: pass
    db_connection.close()
    
    # Indice autoincremental
    if 'id' not in datatosql:
        try:
            db_connection = sql.connect(user=user, password=password, host=host, database=schema)
            cursor        = db_connection.cursor()
            cursor.execute(f"ALTER TABLE {schema}.{table} ADD COLUMN id INT AUTO_INCREMENT FIRST, ADD PRIMARY KEY (id);")
            db_connection.commit()
            db_connection.close()
        except: pass
    
    # Indices
    formato = {
               "code":f"CREATE INDEX `idx_code`  ON `{schema}`.`{table_name}` (code)",
               "scacodigo":f"CREATE INDEX `idx_scacodigo`  ON `{schema}`.`{table_name}` (scacodigo)",
               "coddir":f"CREATE INDEX `idx_coddir`  ON `{schema}`.`{table_name}` (coddir)"
               }
    db_connection = sql.connect(user=user, password=password, host=host, database=schema)
    cursor        = db_connection.cursor()
    for key,value in formato.items(): 
        if key in datatosql:
            try:
                cursor.execute(value)
                db_connection.commit()
            except: pass
    db_connection.close()

    if '_market' in table_name:
        lista = [
            f"CREATE INDEX `idx_estrato` `{schema}`.`{table}` (estrato)",
            f"CREATE INDEX `idx_habitaciones` `{schema}`.`{table}` (habitaciones)",
            f"CREATE INDEX `idx_banos` `{schema}`.`{table}` (banos)",
            f"CREATE INDEX `idx_garajes` `{schema}`.`{table}` (garajes)",
            f"CREATE INDEX `idx_areaconstruida` `{schema}`.`{table}` (areaconstruida)",
            ]
        db_connection = sql.connect(user=user, password=password, host=host, database=schema)
        cursor        = db_connection.cursor()
        for i in tqdm(lista): 
            try:
                cursor.execute(i)
                db_connection.commit()
            except: pass
        db_connection.close()        

    # Indice espacial
    if 'latitud' in datatosql and 'longitud' in datatosql:
        lista = [
            f"UPDATE `{schema}`.`{table}` SET `latitud` = '0', `longitud` = '0' WHERE `latitud` IS NULL OR `longitud` IS NULL",
            f"ALTER TABLE `{schema}`.`{table}` ADD COLUMN `geometry` POINT NULL ",
            f"UPDATE  `{schema}`.`{table}` SET geometry = Point(longitud, latitud);",
            f"ALTER TABLE `{schema}`.`{table}` CHANGE COLUMN `geometry` `geometry` POINT NOT NULL ;",
            f"CREATE SPATIAL INDEX `idx_geometry`  ON `{schema}`.`{table}` (geometry)",
            f"UPDATE `{schema}`.`{table}` SET `latitud`= NULL , `longitud`= NULL WHERE `latitud`=0 OR `longitud`=0",
            ]
        db_connection = sql.connect(user=user, password=password, host=host, database=schema)
        cursor        = db_connection.cursor()
        for i in tqdm(lista): 
            try:
                cursor.execute(i)
                db_connection.commit()
            except: pass
        db_connection.close()
        
        
#-----------------------------------------------------------------------------#
# Data market y catastro / Bogota
#-----------------------------------------------------------------------------#
datamarket = pd.read_pickle(r'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\datatotalstock_image',compression='gzip')
   
for i in ['valorventa','valorarriendo','areaconstruida']:
    datamarket[i] = pd.to_numeric(datamarket[i],errors='coerce')
datamarket                  = datamarket[datamarket['areaconstruida']>0]
datamarket['fecha_inicial'] = datamarket['fecha_inicial'].apply(lambda x: remove_tz(x))
idd                         = (datamarket['habitaciones'].isin([1,2,3,4,5,6])) & (datamarket['banos'].isin([1,2,3,4,5,6])) & (datamarket['garajes'].isin([0,1,2,3,4,5]))
datamarket                  = datamarket[idd]

#-------------------------------------------------------------------------#
# Imagen principal
datamarket.index = range(len(datamarket))
default_text     = "https://personal-data-bucket-online.s3.us-east-2.amazonaws.com/sin_imagen.png"
imgvariables     = [x for x in datamarket if 'img' in x]
datamarket['imagen_principal'] = datamarket.apply(lambda x: next((x[col] for col in imgvariables if 'http' in str(x[col]) ), None), axis=1)
idd              = datamarket['imagen_principal'].isnull()
if sum(idd)>0:
    datamarket.loc[idd,'imagen_principal'] = default_text
        
for img in imgvariables:
    idd = datamarket[img].isnull()
    if sum(idd)>0:
        datamarket.loc[idd,img] = default_text
        
for tipoinmueble in datamarket['tipoinmueble'].unique():
    
    #-------------------------------------------------------------------------#
    # Venta
    dataventa                  = datamarket[(datamarket['valorventa']>0) & (datamarket['tipoinmueble']==tipoinmueble)]
    dataventa['fecha_inicial'] = pd.to_datetime(dataventa['fecha_inicial'],errors='coerce',utc=True)
    dataventa                  = dataventa.sort_values(by='fecha_inicial',ascending=False)
    dataventa['valormt2']      = dataventa['valorventa']/dataventa['areaconstruida']
    dataventa['tiponegocio']   ='Venta'
    dataventafilter            = getdatafilter(dataventa,'venta',months=15)
 
    #-----------------------------------------------------------------------------#
    # Arriendo
    datarriendo                  = datamarket[(datamarket['valorarriendo']>0)  & (datamarket['tipoinmueble']==tipoinmueble)]
    datarriendo['fecha_inicial'] = pd.to_datetime(datarriendo['fecha_inicial'],errors='coerce',utc=True)
    datarriendo                  = datarriendo.sort_values(by='fecha_inicial',ascending=False)
    datarriendo['valormt2']      = datarriendo['valorarriendo']/datarriendo['areaconstruida']
    datarriendo['tiponegocio']   ='Arriendo'
    datarriendofilter            = getdatafilter(datarriendo,'arriendo',months=15)

    #-------------------------------------------------------------------------#
    # Data Mapa Grid
    data2grid = data2gridshp(dataventafilter,'Venta')
    data2grid.to_pickle(fr'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA APLICATIVOS STREAMLIT\data_bogota_venta_{tipoinmueble.lower()}_grid',compression='gzip')
    table = f'data_colombia_bogota_venta_{tipoinmueble.lower()}_grid'
    data2Mysql(data2grid,table)
    
    data2grid = data2gridshp(datarriendofilter,'Arriendo')
    data2grid.to_pickle(fr'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA APLICATIVOS STREAMLIT\data_bogota_arriendo_{tipoinmueble.lower()}_grid',compression='gzip')
    table = f'data_colombia_bogota_arriendo_{tipoinmueble.lower()}_grid'
    data2Mysql(data2grid,table)

    #-------------------------------------------------------------------------#
    # Data MLS
    
        # Venta
    dataventamls = copy.deepcopy(dataventa)
    idd = (dataventamls['available_merge']==0) & (dataventamls['available']==1)
    if sum(idd)>0:
        dataventamls.loc[idd,'available'] = 0
        
    idd                = dataventamls['available']==0
    dataventamls       = dataventamls[~idd]
    dataventamls.index = range(len(dataventamls))
    dataventamls.drop(columns=[x for x in ['available_merge','antiguedad_original'] if x in dataventamls],inplace=True)
    dataventamls.to_pickle(fr'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA APLICATIVOS STREAMLIT\data_bogota_venta_{tipoinmueble.lower()}_market',compression='gzip')
    table = f'data_colombia_bogota_venta_{tipoinmueble.lower()}_market'
    data2Mysql(dataventamls,table)
    
    dataventamls['geometry'] = dataventamls.apply(lambda x: Point(x['longitud'],x['latitud']),axis=1)
    dataventamls.to_pickle(fr'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA APLICATIVOS STREAMLIT\data_bogota_venta_{tipoinmueble.lower()}_market_geometry',compression='gzip')

        # Arriendo
    datarriendomls = copy.deepcopy(datarriendo)
    idd = (datarriendomls['available_merge']==0) & (datarriendomls['available']==1)
    if sum(idd)>0:
        datarriendomls.loc[idd,'available'] = 0
        
    idd                  = datarriendomls['available']==0
    datarriendomls       = datarriendomls[~idd]
    datarriendomls.index = range(len(datarriendomls))
    datarriendomls.drop(columns=[x for x in ['available_merge','antiguedad_original'] if x in datarriendomls],inplace=True)
    datarriendomls.to_pickle(fr'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA APLICATIVOS STREAMLIT\data_bogota_arriendo_{tipoinmueble.lower()}_market',compression='gzip')
    table = f'data_colombia_bogota_arriendo_{tipoinmueble.lower()}_market'
    data2Mysql(datarriendomls,table)
        
    datarriendomls['geometry'] = datarriendomls.apply(lambda x: Point(x['longitud'],x['latitud']),axis=1)
    datarriendomls.to_pickle(fr'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA APLICATIVOS STREAMLIT\data_bogota_arriendo_{tipoinmueble.lower()}_market_geometry',compression='gzip')

    #-----------------------------------------------------------------------------#
    # Data precio por mt2 por barrios
    #-----------------------------------------------------------------------------#
    databarriosventa         = dataventafilter.groupby(['scacodigo']).agg({'valormt2':['median','count']}).reset_index()
    databarriosventa.columns = ['scacodigo','valormt2','obs']
    databarriosventa['tipo'] = 'barrio'
    datapaso                 = dataventafilter.groupby(['scacodigo','habitaciones','banos','garajes']).agg({'valormt2':['median','count']}).reset_index()
    datapaso.columns         = ['scacodigo','habitaciones','banos','garajes','valormt2','obs']
    idd                      = (datapaso['habitaciones'].isin([1,2,3,4,5])) & (datapaso['banos'].isin([1,2,3,4,5])) & (datapaso['garajes'].isin([0,1,2,3,4]))
    datapaso                 = datapaso[idd]
    datapaso['tipo']         = 'complemento'
    databarriosventa         = databarriosventa.append(datapaso)
    databarriosventa.to_pickle(fr'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA APLICATIVOS STREAMLIT\data_bogota_venta_{tipoinmueble.lower()}_barrio',compression='gzip')
    table = f'data_colombia_bogota_venta_{tipoinmueble.lower()}_barrio'
    data2Mysql(databarriosventa,table)
    
    databarriosarriendo         = datarriendofilter.groupby(['scacodigo']).agg({'valormt2':['median','count']}).reset_index()
    databarriosarriendo.columns = ['scacodigo','valormt2','obs']
    databarriosarriendo['tipo'] = 'barrio'
    datapaso                    = datarriendofilter.groupby(['scacodigo','habitaciones','banos','garajes']).agg({'valormt2':['median','count']}).reset_index()
    datapaso.columns            = ['scacodigo','habitaciones','banos','garajes','valormt2','obs']
    idd                         = (datapaso['habitaciones'].isin([1,2,3,4,5])) & (datapaso['banos'].isin([1,2,3,4,5])) & (datapaso['garajes'].isin([0,1,2,3,4]))
    datapaso                    = datapaso[idd]
    datapaso['tipo']            = 'complemento'
    databarriosarriendo         = databarriosarriendo.append(datapaso)
    databarriosarriendo.to_pickle(fr'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA APLICATIVOS STREAMLIT\data_bogota_arriendo_{tipoinmueble.lower()}_barrio',compression='gzip')
    table = f'data_colombia_bogota_arriendo_{tipoinmueble.lower()}_barrio'
    data2Mysql(databarriosarriendo,table)
    
    #-----------------------------------------------------------------------------#
    # Valor x mt2 en el sector
    #-----------------------------------------------------------------------------#    
    datavalorm2venta = valormt2_sector(dataventafilter)
    datavalorm2venta.to_pickle(fr'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA APLICATIVOS STREAMLIT\data_bogota_venta_{tipoinmueble.lower()}_valormt2sector',compression='gzip')
    table = f'data_colombia_bogota_venta_{tipoinmueble.lower()}_valormt2sector'
    data2Mysql(datavalorm2venta,table)
    
    datavalorm2arriendo = valormt2_sector(datarriendofilter)
    datavalorm2arriendo.to_pickle(fr'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA APLICATIVOS STREAMLIT\data_bogota_arriendo_{tipoinmueble.lower()}_valormt2sector',compression='gzip')
    table = f'data_colombia_bogota_arriendo_{tipoinmueble.lower()}_valormt2sector'
    data2Mysql(datavalorm2arriendo,table)
    
    #-----------------------------------------------------------------------------#
    # Valorizacion
    #-----------------------------------------------------------------------------#
    datavalorizacionventa = valorizacion(dataventafilter)
    datavalorizacionventa = datavalorizacionventa[datavalorizacionventa['valorizacion'].notnull()]
    datavalorizacionventa.to_pickle(fr'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA APLICATIVOS STREAMLIT\data_bogota_venta_{tipoinmueble.lower()}_valorizacion',compression='gzip')
    table = f'data_colombia_bogota_venta_{tipoinmueble.lower()}_valorizacion'
    data2Mysql(datavalorizacionventa,table)
    
    datavalorizacionarriendo = valorizacion(datarriendofilter)
    datavalorizacionarriendo = datavalorizacionarriendo[datavalorizacionarriendo['valorizacion'].notnull()]
    datavalorizacionarriendo.to_pickle(fr'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA APLICATIVOS STREAMLIT\data_bogota_arriendo_{tipoinmueble.lower()}_valorizacion',compression='gzip')
    table = f'data_colombia_bogota_arriendo_{tipoinmueble.lower()}_valorizacion'
    data2Mysql(datavalorizacionarriendo,table)

    #-----------------------------------------------------------------------------#
    # Caracterizacion por zona
    #-----------------------------------------------------------------------------#
    datacaracterizacionventa = estadisticas_sector(dataventafilter)
    datacaracterizacionventa.to_pickle(fr'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA APLICATIVOS STREAMLIT\data_bogota_venta_{tipoinmueble.lower()}_caracterizacion',compression='gzip')
    table = f'data_colombia_bogota_venta_{tipoinmueble.lower()}_caracterizacion'
    data2Mysql(datacaracterizacionventa,table)
    
    datacaracterizacionarriendo = estadisticas_sector(datarriendofilter)
    datacaracterizacionarriendo.to_pickle(fr'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA APLICATIVOS STREAMLIT\data_bogota_arriendo_{tipoinmueble.lower()}_caracterizacion',compression='gzip')
    table = f'data_colombia_bogota_arriendo_{tipoinmueble.lower()}_caracterizacion'
    data2Mysql(datacaracterizacionarriendo,table)
    
#-----------------------------------------------------------------------------#
# Modelos
#-----------------------------------------------------------------------------#
if runann:
    
    for i in ['areaconstruida', 'banos', 'estrato', 'garajes', 'habitaciones','valorventa','valorarriendo']:
        datamarket[i] = pd.to_numeric(datamarket[i],errors='coerce')
       
    for i in ['areaconstruida', 'banos', 'estrato', 'garajes', 'habitaciones', 'tiempodeconstruido', 'scacodigo']:
        idd = datamarket[i].isnull()
        if sum(idd)>0:
            datamarket = datamarket[~idd]
            
    for i in ['habitaciones', 'banos', 'garajes', 'estrato']:
        datamarket[i] = datamarket[i].astype(int)
        
    barrio_codigo                    = LabelEncoder()   
    datamarket['scacodigo']          = barrio_codigo.fit_transform(datamarket['scacodigo'])
    tdc_codigo                       = LabelEncoder()
    datamarket['tiempodeconstruido'] = tdc_codigo.fit_transform(datamarket['tiempodeconstruido'])
    variables                        = ['areaconstruida','habitaciones','banos','garajes','estrato','scacodigo','tiempodeconstruido']

    for pp in path:
        with open(os.path.join(pp,'colombia_bogota_scacodigo.pkl'), "wb") as f:
            pickle.dump(barrio_codigo, f)

        with open(os.path.join(pp,'colombia_bogota_tiempoconstruido.pkl'), "wb") as f:
            pickle.dump(tdc_codigo, f)

        with open(os.path.join(pp,'colombia_bogota_variables.pkl'), "wb") as file:
            pickle.dump(variables, file)

    variables.append('valor')
    modelresult = pd.DataFrame()
    
    for tipoinmueble in datamarket['tipoinmueble'].unique():
        for tiponegocio in ['Venta','Arriendo']:
            
            if tiponegocio.lower()=='venta':
                vardep = 'valorventa'
            elif tiponegocio.lower()=='arriendo':
                vardep = 'valorarriendo'    
                
            datamodel                  = datamarket[(datamarket[vardep]>0) & (datamarket['tipoinmueble']==tipoinmueble)]
            datamodel.rename(columns={vardep:'valor'},inplace=True)
            datamodel                  = datamodel[datamodel['valor'].notnull()]  
            datamodel['fecha_inicial'] = pd.to_datetime(datamodel['fecha_inicial'],errors='coerce',utc=True)
            datamodel                  = datamodel.sort_values(by='fecha_inicial',ascending=False)
            datamodel['valormt2']      = datamodel['valor']/datamodel['areaconstruida']
            datamodel                  = getdatafilter(datamodel,tiponegocio.lower(),months=15)
            datamodel                  = datamodel[variables]
            
            vcod      = datamodel['scacodigo'].value_counts().reset_index()
            vcod      = vcod[vcod['scacodigo']>10]
            idd       = datamodel['scacodigo'].isin(vcod['index'])
            datamodel = datamodel[idd]            
            
            # ANN
            result      = ANN(datamodel)
            salida      = pd.DataFrame([{'mpio_ccdgo':'11001','tipoinmueble':tipoinmueble,'tiponegocio':tiponegocio,'fecha':datetime.now(),'salida':result}])
            modelresult = modelresult.append(salida)
            for pp in path:
                salida.to_pickle(os.path.join(pp,f'ANN_bogota_{tiponegocio.lower()}_{tipoinmueble.lower()}'),compression='gzip')
            
            # XGboosting
            model = xgboostingmodel(datamodel, test_size=0.1, n_splits=10)
            for pp in path:
                with open(os.path.join(pp,f'xgboosting_{tiponegocio.lower()}_{tipoinmueble.lower()}.pkl'), "wb") as f:
                    pickle.dump(model, f)

    # Guardar los resultados en MySQL
    modelresult_copy  = modelresult.copy()
    modelresult.index = range(len(modelresult))
    for i in range(len(modelresult)):
        modelresult.loc[i,'salida'] = pd.io.json.dumps(modelresult.loc[i,'salida'])
        
    dtype  = {'mpio_ccdgo':VARCHAR(5), 'tipoinmueble':VARCHAR(11), 'tiponegocio':VARCHAR(8), 'fecha':DATETIME, 'salida':JSON}
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{schema}')   
    modelresult.to_sql('model_result_colombia_ann',engine,if_exists='append', index=False,chunksize=1,dtype=dtype)