import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from sqlalchemy import create_engine 
from ANN import ANN
from ANNtest import pricingforecast


mpio_ccdgo   = '11001'
tipoinmueble = 'Apartamento'
datemodel    = datetime.today().strftime("%Y-%m-%d")

#-----------------------------------------------------------------------------#
# sell price model Bogota
#-----------------------------------------------------------------------------#
datamodel   = pd.read_pickle(r'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA BUCKET\data_market_venta_bogota',compression='gzip')
valormt2min = 2000000
valormt2max = 20000000

datamodel['valormt2'] = datamodel['valorventa']/datamodel['areaconstruida']
datamodel             = datamodel[(datamodel['valormt2']>=valormt2min) & (datamodel['valormt2']<=valormt2max)]

datamodel.rename(columns={'valorventa':'valor'},inplace=True)
variables = ['areaconstruida','banos','estrato','garajes','habitaciones','tiempodeconstruido','scacodigo','valor']
datamodel = datamodel[variables]

formato = {'habitaciones':[1,2,3,4,5,6],'banos':[1,2,3,4,5,6],'garajes':[0,1,2,3,4,5],'estrato':[1,2,3,4,5,6],'tiempodeconstruido':['Menos de 1 año','1 a 8 años','9 a 15 años','16 a 30 años','más de 30 años']}
for key, value in formato.items():
    idd = datamodel[key].isin(value)
    if sum(idd)>0:
        datamodel = datamodel[idd]
        
result       = ANN(datamodel)
salida_venta = pd.DataFrame([{'mpio_ccdgo':mpio_ccdgo,'tipoinmueble':tipoinmueble,'tiponegocio':'sell','fecha':datemodel,'salida':pd.io.json.dumps(result)}])

#-----------------------------------------------------------------------------#
# rent price model
#-----------------------------------------------------------------------------#
datamodel   = pd.read_pickle(r'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA BUCKET\data_market_arriendo_bogota',compression='gzip')
valormt2min = 10000
valormt2max = 100000

datamodel['valormt2'] = datamodel['valorarriendo']/datamodel['areaconstruida']
datamodel             = datamodel[(datamodel['valormt2']>=valormt2min) & (datamodel['valormt2']<=valormt2max)]

datamodel.rename(columns={'valorarriendo':'valor'},inplace=True)
variables = ['areaconstruida','banos','estrato','garajes','habitaciones','tiempodeconstruido','scacodigo','valor']
datamodel = datamodel[variables]

formato = {'habitaciones':[1,2,3,4,5,6],'banos':[1,2,3,4,5,6],'garajes':[0,1,2,3,4,5],'estrato':[1,2,3,4,5,6],'tiempodeconstruido':['Menos de 1 año','1 a 8 años','9 a 15 años','16 a 30 años','más de 30 años']}
for key, value in formato.items():
    idd = datamodel[key].isin(value)
    if sum(idd)>0:
        datamodel = datamodel[idd]
        
result       = ANN(datamodel)
salida_renta = pd.DataFrame([{'mpio_ccdgo':mpio_ccdgo,'tipoinmueble':tipoinmueble,'tiponegocio':'rent','fecha':datemodel,'salida':pd.io.json.dumps(result)}])

#-----------------------------------------------------------------------------#
# Exportar
salida_venta.to_pickle(r'D:\Dropbox\Empresa\Buydepa\COLOMBIA\PRICING MODEL\RESULTADOS\ANN_bogota_venta_apartamento',compression='gzip')
salida_renta.to_pickle(r'D:\Dropbox\Empresa\Buydepa\COLOMBIA\PRICING MODEL\RESULTADOS\ANN_bogota_arriendo_apartamento',compression='gzip')


inputvar = {
             'direccion':"Carrera 19a 103a 62, Bogota",
             'areaconstruida':114,
             'habitaciones':2,                     # [1,2,3,4,5,6] 
             'banos':3,                            # [1,2,3,4,5,6]
             'garajes':2,                          # [0,1,2,3,4]
             'estrato':6,                          # [1,2,3,4,5,6]
             'tiempodeconstruido':'9 a 15 años',   # ['menor a 1 año','1 a 8 años','9 a 15 años','16 a 30 años','más de 30 años']
             'scacodigo':'008412',
             'tiponegocio':'sell',                 # [rent,sell]
             'mpio_ccdgo':'11001',
             'tipoinmueble':'Apartamento'
             }

result_sell = pricingforecast(inputvar)
print(result_sell)

inputvar['tiponegocio'] = 'rent'
result_rent = pricingforecast(inputvar)
print(result_rent)