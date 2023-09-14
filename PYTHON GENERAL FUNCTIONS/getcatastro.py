import json
import requests
import pandas as pd
import warnings
from datetime import datetime
from multiprocessing.dummy import Pool

def getinfo(chip):
    warnings.filterwarnings("ignore") 
    data = getid(chip)
    data = getcontibuyente(data)
    data = getvalue(data,chip)
    data['chip'] = chip
    return data
    
def getid(chip):
    yyyy   = datetime.now().year
    output = requests.get(f'https://oficinavirtual.shd.gov.co/ConsultaPagos/resources/servicios/relacionPagos?impuesto=1&objeto={chip}', verify=False)
    data   = pd.DataFrame(output.json()['detalles'])
    if 'vigencia' in data:
        yyyy = data['vigencia'].min()-1
    terminado = 0
    while terminado==0:
        try:
            output     = requests.get(f'https://oficinavirtual.shd.gov.co/ConsultaPagos/resources/servicios/relacionPagos?impuesto=1&objeto={chip}&vigencia={yyyy}', verify=False)
            data = data.append(pd.DataFrame(output.json()['detalles']))
        except: pass
        yyyy -= 1
        if yyyy<2010: 
            terminado = 1
    return data

def getcontibuyente(data):
    lista = []
    if 'nroIdentificacion' in data:
        lista = list(data['nroIdentificacion'].unique())
    pool       = Pool(4)
    futures    = []
    dataresult = []
    for i in lista:
        for x in range(1,7):
            futures.append(pool.apply_async(requests.post, ['https://oficinavirtual.shd.gov.co/ServiciosRITDQ/resources/contribuyente/'],dict(data=json.dumps({"codTId": x, "nroId":str(i)}),headers = {"Content-Type":"application/json"},verify=False)))
    for future in futures:
        resultado = future.get().json()
        if 'contribuyente' in resultado:
            dataresult.append(resultado['contribuyente'])

    dataresult = pd.DataFrame(dataresult)
    vardrop    = [x for x in list(dataresult) if x in list(data)]
    if 'nroIdentificacion' in vardrop: 
        vardrop.remove('nroIdentificacion')
    if vardrop!=[]:
        dataresult.drop(columns=vardrop,inplace=True)   
    if data.empty is False and dataresult.empty is False:
        
        # Eliminar los registros duplicados del mismo documento
        conteo     = dataresult['nroIdentificacion'].value_counts().reset_index()
        conteo     = conteo[conteo['nroIdentificacion']==1]
        dataresult = dataresult[dataresult['nroIdentificacion'].isin(conteo['index'])]
        
        data['nroIdentificacion']       = data['nroIdentificacion'].astype(str)
        dataresult['nroIdentificacion'] = dataresult['nroIdentificacion'].astype(str)
        data = data.merge(dataresult,on='nroIdentificacion',how='left',validate='m:1')
    return data
            
def getvalue(data,chip):
    pool       = Pool(4)
    futures    = []
    dataresult = []
    if data.empty:
        year  = datetime.now().year
        years = list(range(year, 2010, -1))
        nid   = "123456"
        nid   = [nid] * len(years)
        data  = pd.DataFrame({'vigencia': years, 'nroIdentificacion': nid})

    idd = data['vigencia']==datetime.now().year
    if sum(idd)==0:
        data = pd.DataFrame([{'vigencia':datetime.now().year,'nroIdentificacion':data['nroIdentificacion'].iloc[0]}]).append(data)

    idd = (data['nroIdentificacion'].isnull()) | (data['nroIdentificacion']=='')
    if sum(idd)>0:
        data.loc[idd,'nroIdentificacion'] = '123456'
    
    for _,items in data.iterrows():
        identificacion = items['nroIdentificacion']
        yyyy           = items['vigencia']
        futures.append(pool.apply_async(requests.get, [f'https://oficinavirtual.shd.gov.co/ServiciosSitII/resources/predial/obtenerInfoDeclaracionPredial?chip={chip}&numeroIdentificacion={identificacion}&codigoVigencia={yyyy}'], dict(verify=False,headers={'id':str(identificacion),'yy':str(yyyy)})))

    for future in futures:
        dataresult.append(future.get().json())
    
    dataresult = pd.DataFrame(dataresult)
    vardrop    = [x for x in list(dataresult) if x in list(data)]
    for j in ['nroIdentificacion','vigencia','codigoVigencia']:
        if j in vardrop: vardrop.remove(j)
    if vardrop!=[]:
        dataresult.drop(columns=vardrop,inplace=True)
    if 'codigoVigencia' in dataresult:
        dataresult.rename(columns={'codigoVigencia':'vigencia'},inplace=True)
    
    if data.empty is False and dataresult.empty is False:
        data['vigencia']       = data['vigencia'].astype(int)
        dataresult['vigencia'] = dataresult['vigencia'].astype(int)
        data = data.merge(dataresult,on='vigencia',how='outer')
    return data