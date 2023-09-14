import pandas as pd
import numpy as np
import pickle
from shapely import wkt
from datetime import datetime

import sys
sys.path.insert(0, r'D:\Dropbox\Empresa\Buydepa\COLOMBIA\PYTHON GENERAL FUNCTIONS')
from coddir import coddir
from getdata import conjuntos_direcciones,getdatanivel1,getdatanivel2,getdatanivel3,getdatanivel4,getdatanivel6,getdatacatastro,obtener_coordenadas,getlatlng,getinfochip,formatofecha,getscacodigo,getdataradio

sys.path.insert(0, r'D:\Dropbox\Empresa\Buydepa\COLOMBIA\PRICING MODEL')
from pricing_ponderador import pricing_ponderador

sys.path.insert(0, r'D:\Dropbox\Empresa\Buydepa\COLOMBIA\PRICING MODEL\ANN')
from ANNtestV2 import pricingforecast

def main(inputvar):
    
    tipoinmueble = inputvar['tipoinmueble']
    forecastlist = {'venta': [],'arriendo': []}
    
    fcoddir,scacodigo = ['']*2
    if 'direccion' in inputvar:
        fcoddir = coddir(inputvar['direccion'])
    
    latitud,longitud = [None]*2
    datamarketventa,datamarketarriendo,datagaleria,databarrio,barriopricing,barriocaracterizacion,barriovalorizacion,dataventazona,dataarriendozona = [pd.DataFrame()]*9
    
    if fcoddir!='':
        dataconjunto,datapredios,datalote              = getdatanivel1(fcoddir)
        datamarketventa,datamarketarriendo,datagaleria = getdatanivel3(fcoddir)
        
        if dataconjunto.empty is False:
            if 'scacodigo' in dataconjunto:
                scacodigo = dataconjunto['scacodigo'].iloc[0]
            if 'vetustez_median' in dataconjunto: 
                try: inputvar['antiguedad'] = datetime.now().year-dataconjunto['vetustez_median'].iloc[0]
                except: pass
            if 'estrato' in dataconjunto:
                if dataconjunto['estrato'].iloc[0]>=1 and dataconjunto['estrato'].iloc[0]<=6:
                    inputvar['estrato'] = dataconjunto['estrato'].iloc[0]

        if datalote.empty is False:
            poly             = wkt.loads(datalote["wkt"].iloc[0])
            latitud,longitud = [poly.centroid.y,poly.centroid.x]
        else:
            latitud, longitud = obtener_coordenadas(dataconjunto, datamarketventa, datamarketarriendo)
    
    if latitud is None or longitud is None:
        latitud, longitud = getlatlng(inputvar['direccion'])
             
    if latitud is not None and longitud is not None:
        inputvar['latitud']  = latitud
        inputvar['longitud'] = longitud
        dataventazona,dataarriendozona  = getdataradio(inputvar)

    if scacodigo=='' and latitud is not None and longitud is not None:
        scacodigo = getscacodigo(latitud,longitud)

    #-------------------------------------------------------------------------#
    # Tiempo de construido
    if 'antiguedad' in inputvar and inputvar['antiguedad']>=0:
        if inputvar['antiguedad']<=1:
            inputvar['tiempodeconstruido'] = 'Menos de 1 año'
        elif inputvar['antiguedad']>1 and inputvar['antiguedad']<=8:
            inputvar['tiempodeconstruido'] = '1 a 8 años'
        elif inputvar['antiguedad']>8 and inputvar['antiguedad']<=15:
            inputvar['tiempodeconstruido'] = '9 a 15 años'
        elif inputvar['antiguedad']>15 and inputvar['antiguedad']<=30:
            inputvar['tiempodeconstruido'] = '16 a 30 años'
        else: inputvar['tiempodeconstruido'] = 'más de 30 años'

    if scacodigo is not None and scacodigo!='':
        
        barriopricing,barriocaracterizacion,barriovalorizacion = getdatanivel6(scacodigo)
        
        #---------------------------------------------------------------------#
        # Codificacion
        pickle_file_path = r"D:\Dropbox\Empresa\Buydepa\COLOMBIA\PRICING MODEL\RESULTADOS\colombia_bogota_scacodigo.pkl"
        with open(pickle_file_path, "rb") as f:
            barrio_codigo = pickle.load(f)
    
        pickle_file_path = r"D:\Dropbox\Empresa\Buydepa\COLOMBIA\PRICING MODEL\RESULTADOS\colombia_bogota_tiempoconstruido.pkl"
        with open(pickle_file_path, "rb") as f:
            tiempodeconstruido_codigo = pickle.load(f)
            
        pickle_file_path = r"D:\Dropbox\Empresa\Buydepa\COLOMBIA\PRICING MODEL\RESULTADOS\colombia_bogota_variables.pkl"
        with open(pickle_file_path, "rb") as f:
            variables = pickle.load(f)
    
        inputvar['scacodigo']          = barrio_codigo.transform([scacodigo])[0]
        inputvar['tiempodeconstruido'] = tiempodeconstruido_codigo.transform([inputvar['tiempodeconstruido']])[0] 
 
        #---------------------------------------------------------------------#
        # Modelo XGboosting
        for tiponegocio in ['Venta','Arriendo']:
            
            pickle_file_path = rf"D:\Dropbox\Empresa\Buydepa\COLOMBIA\PRICING MODEL\RESULTADOS\xgboosting_{tiponegocio.lower()}_{tipoinmueble.lower()}.pkl"
            with open(pickle_file_path, 'rb') as file:
                model = pickle.load(file)
            
            datamodel      = pd.DataFrame([inputvar])
            datamodel      = datamodel[variables]
            prediccion_log = model.predict(datamodel)
            prediccion     = np.exp(prediccion_log)
            forecastlist[tiponegocio.lower()].append({'model':'forecast_xgboosting','value':prediccion[0]})
    
        #---------------------------------------------------------------------#
        # Modelo ANN
        for tiponegocio in ['Venta','Arriendo']:

            pickle_file_path = rf"D:\Dropbox\Empresa\Buydepa\COLOMBIA\PRICING MODEL\RESULTADOS\ANN_bogota_{tiponegocio.lower()}_{tipoinmueble.lower()}"
            model            = pd.read_pickle(pickle_file_path,compression='gzip')
            salida           = model['salida'].iloc[0]
            forecastlist[tiponegocio.lower()].append({'model':'forecast_model','value':pricingforecast(salida,inputvar)['valorestimado']})
        
        #---------------------------------------------------------------------#
        if barriopricing.empty is False:
            for tiponegocio in ['Venta','Arriendo']:
                
                # Forecast: Valor por mt2 del barrio
                datapaso = barriopricing[(barriopricing['tipo']=='barrio') & (barriopricing['obs']>=10) & (barriopricing['tiponegocio']==tiponegocio) ]
                if datapaso.empty is False and 'areaconstruida' in inputvar and inputvar['areaconstruida']>0:
                    precioforecast = datapaso['valormt2'].iloc[0]*inputvar['areaconstruida']
                    forecastlist[tiponegocio.lower()].append({'model':'forecast_barrio','value':precioforecast})
    
                # Forecast: Valor por mt2 del barrio, con mismas habitaciones, baños y garajes
                if 'habitaciones' in inputvar and 'banos' in inputvar and 'garajes' in inputvar:
                    datapaso = barriopricing[(barriopricing['tipo']=='complemento') & (barriopricing['tiponegocio']==tiponegocio) & (barriopricing['obs']>=10) & (barriopricing['habitaciones']==inputvar['habitaciones'])  & (barriopricing['banos']==inputvar['banos'])  & (barriopricing['garajes']==inputvar['garajes']) ]
                    if datapaso.empty is False:
                        precioforecast = datapaso['valormt2'].iloc[0]*inputvar['areaconstruida']
                        forecastlist[tiponegocio.lower()].append({'model':'forecast_barrio_complemento','value':precioforecast})
                 
    #-------------------------------------------------------------------------#
    # Forecast: datos del mismo conjunto
    if datamarketventa.empty is False and 'areaconstruida' in inputvar and inputvar['areaconstruida']>0: 
        forecastlist['venta'].append({'model':'forecast_edificio_similiar','value':datamarketventa['valormt2'].median()*inputvar['areaconstruida']})
        areamin = inputvar['areaconstruida']*0.85
        areamax = inputvar['areaconstruida']*1.15
        idd     = ((datamarketventa['areaconstruida']>=areamin) & (datamarketventa['areaconstruida']<=areamax)) & (datamarketventa['habitaciones']==inputvar['habitaciones'])
        if sum(idd)>4:
            forecastlist['venta'].append({'model':'forecast_edificio','value':datamarketventa[idd]['valormt2'].median()*inputvar['areaconstruida']})
        
    if datamarketarriendo.empty is False and 'areaconstruida' in inputvar and inputvar['areaconstruida']>0: 
        forecastlist['arriendo'].append({'model':'forecast_edificio_similiar','value':datamarketarriendo['valormt2'].median()*inputvar['areaconstruida']})
        areamin = inputvar['areaconstruida']*0.85
        areamax = inputvar['areaconstruida']*1.15
        idd     = ((datamarketarriendo['areaconstruida']>=areamin) & (datamarketarriendo['areaconstruida']<=areamax)) & (datamarketarriendo['habitaciones']==inputvar['habitaciones'])
        if sum(idd)>5:
            forecastlist['arriendo'].append({'model':'forecast_edificio','value':datamarketarriendo[idd]['valormt2'].median()*inputvar['areaconstruida']})
    
    #-------------------------------------------------------------------------#
    # Forecast: datos de inmuebles similares misma zona
    if dataventazona.empty is False  and 'areaconstruida' in inputvar and inputvar['areaconstruida']>0:
        forecastlist['venta'].append({'model':'forecast_zona','value':dataventazona['valormt2'].median()*inputvar['areaconstruida']})
    
    if dataarriendozona.empty is False  and 'areaconstruida' in inputvar and inputvar['areaconstruida']>0:
        forecastlist['arriendo'].append({'model':'forecast_zona','value':dataarriendozona['valormt2'].median()*inputvar['areaconstruida']})
  
    #-------------------------------------------------------------------------#
    # Resultados
    forecast_venta    = pricing_ponderador(forecastlist['venta'])
    forecast_arriendo = pricing_ponderador(forecastlist['arriendo'])
    
    return forecast_venta,forecast_arriendo,forecastlist
    

#-----------------------------------------------------------------------------#
#
#
#-----------------------------------------------------------------------------#
inputvar = {
            'pais':'Colombia',
            'ciudad':'Bogota',
            'direccion':'Carrera 19A # 103A - 62', # 'KR 111A 148 50',
            'tiponegocio':'Venta',
            'tipoinmueble':'Apartamento', # 'Apartamento'
            'areaconstruida': 114, # 60,
            'habitaciones': 2, # 3,
            'banos': 3, # 2,
            'garajes': 2, # 1,
            'estrato': 6, # 3,
            'antiguedad':13, #13,
            'metros': 500
                }

forecast_venta,forecast_arriendo,forecastlist = main(inputvar)

print(['Forecast Venta',forecast_venta])
print(['Forecast Arriendo',forecast_arriendo])
#print(['Forecast models',forecastlist])