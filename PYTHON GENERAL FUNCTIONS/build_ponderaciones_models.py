import itertools
import random
import pandas as pd
import pickle
import os

path     = [r"D:\Dropbox\Empresa\Buydepa\COLOMBIA\PRICING MODEL\RESULTADOS",
            r"D:\Dropbox\Empresa\Buydepa\PROYECTOS\proceso\appcolombia\data"]

def generate_valid_combinations(item_list):
    valid_combinations = []
    
    for r in range(2, len(item_list) + 1):
        combinations_r = itertools.combinations(item_list, r)
        valid_combinations.extend(combinations_r)
    return valid_combinations

def getvector(item_list):
    valorinicial       = 0.05
    tasa_decrecimiento = 0.4
    valor_minimo       = 0.05
    terminado          = 0
    k                  = len(item_list)
    while terminado==0:
        vector = [valorinicial]
        for i in range(1,k):
            vector.append(vector[i-1]*(1-tasa_decrecimiento))
        for i in range(len(vector)):
            if vector[i]<valor_minimo: vector[i] = valor_minimo
        if sum(vector)>1: 
            terminado = 1
        valorinicial += 0.01
    return adjust_vector(vector)

def adjust_vector(vector):
    elements_above_01 = [value for value in vector if value > 0.1]
    scaling_factor    = (1 - sum([value for value in vector if value <= 0.1])) / sum(elements_above_01)
    adjusted_vector   = [value * scaling_factor if value > 0.1 else value for value in vector]
    return adjusted_vector

def ajustar_ponderantes_modelo(x):
    
    pondmin_ann = 0.1
    pondmin_xg  = 0.15
    
    p         = pd.DataFrame(x)
    p['type'] = True
    idd       = p['ponderacion']<0.1
    if sum(idd)>0:
        p.loc[idd,'type'] = False
        
    idd = (p['ponderacion']<pondmin_ann) & (p['lista']=='forecast_model')
    if sum(idd)>0:
        p.loc[idd,'type']        = False
        p.loc[idd,'ponderacion'] = pondmin_ann
        
    idd = (p['ponderacion']<pondmin_xg) & (p['lista']=='forecast_xgboosting')
    if sum(idd)>0:
        p.loc[idd,'type']        = False
        p.loc[idd,'ponderacion'] = pondmin_xg
       
    sumelements1 = 0
    try: sumelements1 = p[p['type']==False]['ponderacion'].sum()
    except: pass
    sumelements2 = 0
    try: sumelements2 = p[p['type']==True]['ponderacion'].sum()
    except: pass
    scaling_factor = (1 - sumelements1) / sumelements2
    
    idd = p['type']==True
    if sum(idd)>0:
        p.loc[idd,'ponderacion'] = p.loc[idd,'ponderacion'] *scaling_factor
    
    p['ponderacion'] = p['ponderacion'].round(4)
    del p['type']
    return p.to_dict(orient='list')

def ajustar_2items_modelos(x):
    p   = pd.DataFrame(x)
    idd = p['lista'].isin(['forecast_model','forecast_xgboosting'])
    if len(p)==2 and sum(idd)==2:
        return True
    else: return False
    
item_list          = ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_xgboosting', 'forecast_model', 'forecast_zona', 'forecast_barrio_complemento', 'forecast_barrio']
valid_combinations = generate_valid_combinations(item_list)

data_list = []
for i in valid_combinations:
    data_list.append({'lista': list(i), 'ponderacion': getvector(list(i))})
    
lista_final = []
for i in data_list:
    lista_final.append(ajustar_ponderantes_modelo(i))
    
for i in lista_final:
    if ajustar_2items_modelos(i):
        i['ponderacion'] = [0.5,0.5]
    
# Check
for i in lista_final:
    if abs(1-sum(i['ponderacion']))>1e-3:
        print(sum(i['ponderacion']))
  
for pp in path:
    with open(os.path.join(pp,'ponderacion_modelos.pkl'), "wb") as f:
        pickle.dump(lista_final, f)

lista_final = sorted(lista_final, key=lambda x: len(x['lista']), reverse=True)

for i in lista_final:
    print(f'{i},')