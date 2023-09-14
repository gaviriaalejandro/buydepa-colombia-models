import re
import copy
import pandas as pd
import geopandas as gpd
import warnings
from elimina_tildes import elimina_tildes


def spatialdata():
    
    # Departamento y municipio
    mpio               = gpd.read_file(r"D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\shape files\BOGOTA\version_2022\mpio",encoding = 'utf-8')
    #mpio               = mpio.to_crs(epsg=4326)
    mpio.columns       = [elimina_tildes(x) for x in list(mpio)]
    mpio['mpio_ccdgo'] = mpio['dpto_ccdgo'] + mpio['mpio_ccdgo']
        
    # Localidad
    localidad         = gpd.read_file(r"D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\shape files\BOGOTA\version_2022\localidad",encoding = 'utf-8')
    #localidad         = localidad.to_crs(epsg=4326)
    localidad.columns = [elimina_tildes(x) for x in list(localidad)]
    
    # UPZ
    upz              = gpd.read_file(r"D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\shape files\BOGOTA\version_2022\upz",encoding = 'utf-8')
    #upz              = upz.to_crs(epsg=4326)
    upz.columns      = [elimina_tildes(x) for x in list(upz)]
    upz['upznumero'] = upz['uplcodigo'].apply(lambda x: re.sub('[^0-9]','',x) if 'UPZ' in x else None)
    upz['upznumero'] = pd.to_numeric(upz['upznumero'],errors='coerce')
    upz.rename(columns={'uplnombre':'upznombre','upltipo':'upztipo','uplcodigo':'upzcodigo','uplaadmini':'upzadmin','uplarea':'area_urbana'},inplace=True)
    
    # Barrio catastral
    barriocatastral         = gpd.read_file(r"D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\shape files\BOGOTA\version_2022\barrio_catastral",encoding = 'utf-8')
    #barriocatastral         = barriocatastral.to_crs(epsg=4326)
    barriocatastral.columns = [elimina_tildes(x) for x in list(barriocatastral)]
    
    # Manzana
    manzana              = gpd.read_file(r"D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\shape files\BOGOTA\version_2022\manzana",encoding = 'utf-8')
    #manzana              = manzana.to_crs(epsg=4326)
    manzana.columns      = [elimina_tildes(x) for x in list(manzana)]
    manzana['scacodigo'] = manzana['seccodigo']
    
    # Lote
    lote              = gpd.read_file(r'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\shape files\BOGOTA\version_2022\lote',encoding = 'utf-8')
    #lote              = lote.to_crs(epsg=4326)
    lote.columns      = [elimina_tildes(x) for x in list(lote)]
    lote['mancodigo'] = lote['manzcodigo']
    lote['barmanpre'] = lote['manzcodigo']
    
    
    # Códigos DANE
    dane         = gpd.read_file(r"D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\shape files\BOGOTA\version_2022\dane-mgn-urb-seccion\MGN_URB_SECCION.shp",encoding = 'utf-8')
    #dane         = dane.to_crs(epsg=4326)
    dane.columns = [elimina_tildes(x) for x in list(dane)]

    if 'cpob_ccdgo' not in dane and 'cod_cpob' in dane:
        dane['cpob_ccdgo'] = copy.deepcopy(dane['cod_cpob'])
    if 'setu_ccnct' not in dane and 'cod_sect' in dane:
        dane['setu_ccnct'] = copy.deepcopy(dane['cod_sect'])
    if 'secu_ccnct' not in dane and 'cod_secc' in dane:
        dane['secu_ccnct'] = copy.deepcopy(dane['cod_secc'])     
        
    return [mpio,localidad,upz,barriocatastral,manzana,lote,dane]