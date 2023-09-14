import re
import copy
import xgboost as xgb
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error

from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')

import sys
sys.path.insert(0, r'D:\Dropbox\Empresa\Buydepa\COLOMBIA\PYTHON GENERAL FUNCTIONS')
from elimina_tildes import elimina_tildes

def xgboosting_model(y,X,params,minmax,inputvartest):
    resultados = pd.DataFrame([params])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    dtrain = xgb.DMatrix(X_train, y_train)
    dtest  = xgb.DMatrix(X_test, y_test)
    model  = xgb.train(params, dtrain, num_boost_round=100)
    preds  = model.predict(dtest)
    mape   = mean_absolute_percentage_error(np.exp(y_test), np.exp(preds))
    resultados.loc[0,'mean_absolute_percentage_error'] = mape

    varlist   = list(X_train)
    Xforecast = pd.DataFrame(0, index=np.arange(1), columns=varlist)
    for i in inputvartest:
        value = inputvartest[i]
        idd   = [z==elimina_tildes(i) for z in varlist]
        if sum(idd)==0:
            try:
                idd = [re.findall(elimina_tildes(i)+'#'+str(int(value)), z)!=[] for z in varlist]
            except:
                try:
                    idd = [re.findall(elimina_tildes(i)+'#'+elimina_tildes(value), z)!=[] for z in varlist]
                except:
                    pass
            value = 1
        if sum(idd)>0:
            row                = [j for j, x in enumerate(idd) if x]
            varname            = varlist[row[0]]
            Xforecast[varname] = value
            
    # Transform MinMax
    a = Xforecast.iloc[0]
    a = a[a!=0]
    for i in a.index:
        mini         = minmax[i]['min']
        maxi         = minmax[i]['max']
        Xforecast[i] = (Xforecast[i]-mini)/(maxi-mini)
            
    dpredio     = xgb.DMatrix(Xforecast)
    price_pred  = model.predict(dpredio)    
    resultados.loc[0,'forecast'] = np.exp(price_pred[0])
    model.save_model("modelo_xgb.bin")
    result  = {
           'varlist':list(X_train),
           'minmax':minmax,
           'MAPE': mape}

    return resultados,result


#-----------------------------------------------------------------------------#
# sell price model Bogota
#-----------------------------------------------------------------------------#

mpio_ccdgo   = '11001'
tipoinmueble = 'Apartamento'
valormt2min  = 2000000
valormt2max  = 20000000
datamodel    = pd.read_pickle(r'D:\Dropbox\Empresa\Buydepa\COLOMBIA\DATA\DATA BUCKET\data_market_venta_bogota',compression='gzip')

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
        
datamodeloriginal = copy.deepcopy(datamodel)


#-----------------------------------------------------------------------------#
# Transformacion para el modelo
#-----------------------------------------------------------------------------#

list_dummies  = ['scacodigo','banos','estrato','garajes','habitaciones','tiempodeconstruido']
for i in list_dummies:
    if i in list(datamodel):
        newcol = pd.get_dummies(datamodel[i])
        if newcol.empty is False:
            try:    newcol.columns = [elimina_tildes(i)+'#'+str(int(z)) for z in list(newcol)]
            except: newcol.columns = [elimina_tildes(i)+'#'+elimina_tildes(z) for z in list(newcol)]
            datamodel = datamodel.drop(columns=[i]) 
            datamodel = pd.merge(datamodel, newcol, left_index=True, right_index=True)
                
datamodel["valor"] = datamodel["valor"].apply(lambda x: np.log(x))


y      = datamodel["valor"]
X      = datamodel.drop("valor", axis=1)
minmax = {} 
for i in list(X):
    minvalue = X[i].min()
    maxvalue = X[i].max()
    minmax.update({i:{'min':minvalue,'max':maxvalue}})
    newval   = (X[i]-minvalue)/(maxvalue-minvalue)
    X[i]     = copy.deepcopy(newval)
          
    
params = {
    'max_depth': 100,
    'learning_rate': 0.5,
    'objective': 'reg:squarederror',
    'booster': 'gbtree',
    'n_jobs': -1
}
        

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
       
r = xgboosting_model(y,X,params,minmax,inputvar)


datafinal = pd.DataFrame()
for max_depth in tqdm([5,20,50,100,1000]):
    for learning_rate in [0.001,0.01,0.05,0.1,0.5,1]:
        params['max_depth']     = max_depth
        params['learning_rate'] = learning_rate
        r = xgboosting_model(y,X,params,minmax,inputvar)
        datafinal = datafinal.append(r)
        
data1 = copy.deepcopy(datafinal)

datafinal = pd.DataFrame()
for max_depth in tqdm([20,50,100,150,200]):
    for learning_rate in [0.1,0.2,0.4,0.5,0.6,0.8,1]:
        params['max_depth']     = max_depth
        params['learning_rate'] = learning_rate
        r = xgboosting_model(y,X,params,minmax,inputvar)
        datafinal = datafinal.append(r)
        