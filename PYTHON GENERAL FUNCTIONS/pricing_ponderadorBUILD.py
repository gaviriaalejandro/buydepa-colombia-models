
#-----------------------------------------------------------------------------#
# ARMAR TODAS LAS COMBINACIONES DE PONDERACIONES
#-----------------------------------------------------------------------------#

from itertools import combinations

model_list = ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting']

all_combinations = []

# Genera todas las combinaciones posibles de 1 a 7 elementos en la lista
for r in range(1, len(model_list) + 1):
    for combo in combinations(model_list, r):
        all_combinations.append(list(combo))
sorted_models = sorted(all_combinations, key=len, reverse=True)
for i in sorted_models:
    a = f"--'lista':{str(i)},'ponderacion':[]##,"
    a = a.replace("--","{").replace("##","}")
    print(a)
    
    
new_list  = [{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio', 'forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio', 'forecast_zona'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento', 'forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_barrio', 'forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_barrio', 'forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_barrio', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_zona', 'forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_edificio_similiar'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio_complemento'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_barrio'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_zona'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_barrio'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_zona'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento', 'forecast_barrio'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento', 'forecast_zona'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_barrio', 'forecast_zona'],'ponderacion':[]},
{'lista':['forecast_barrio', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_barrio', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_zona', 'forecast_model'],'ponderacion':[]},
{'lista':['forecast_zona', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_model', 'forecast_xgboosting'],'ponderacion':[]},
{'lista':['forecast_edificio'],'ponderacion':[]},
{'lista':['forecast_edificio_similiar'],'ponderacion':[]},
{'lista':['forecast_barrio_complemento'],'ponderacion':[]},
{'lista':['forecast_barrio'],'ponderacion':[]},
{'lista':['forecast_zona'],'ponderacion':[]},
{'lista':['forecast_model'],'ponderacion':[]},
{'lista':['forecast_xgboosting'],'ponderacion':[]},]

#-----------------------------------------------------------------------------#
# A PARTIR DE LA LISTA ANTERIOR, PEGAR LAS PONDERACIONES YA EXISTENTES EN LA NUEVA LISTA
#-----------------------------------------------------------------------------#
old_list  = [
    {'lista':['forecast_edificio_similiar', 'forecast_edificio', 'forecast_model', 'forecast_zona', 'forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.5,0.15,0.15,0.1,0.06,0.04]},
    {'lista':['forecast_edificio', 'forecast_model', 'forecast_zona', 'forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.4,0.4,0.1,0.05,0.05]},
    {'lista':['forecast_edificio_similiar', 'forecast_model', 'forecast_zona', 'forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.5,0.2,0.1,0.1,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_edificio', 'forecast_zona', 'forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.5,0.15,0.15,0.1,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_edificio', 'forecast_model', 'forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.5,0.15,0.15,0.1,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_edificio', 'forecast_model', 'forecast_zona', 'forecast_barrio'] ,'ponderacion':[0.5,0.15,0.15,0.1,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_edificio', 'forecast_model', 'forecast_zona', 'forecast_barrio_complemento'] ,'ponderacion':[0.5,0.15,0.15,0.1,0.1]},
    {'lista':['forecast_model', 'forecast_zona', 'forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.6,0.15,0.15,0.1]},
    {'lista':['forecast_edificio', 'forecast_zona', 'forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.6,0.15,0.15,0.1]},
    {'lista':['forecast_edificio', 'forecast_model', 'forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.4,0.4,0.1,0.1]},
    {'lista':['forecast_edificio', 'forecast_model', 'forecast_zona', 'forecast_barrio'] ,'ponderacion':[0.4,0.4,0.1,0.1]},
    {'lista':['forecast_edificio', 'forecast_model', 'forecast_zona', 'forecast_barrio_complemento'] ,'ponderacion':[0.4,0.4,0.1,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_zona', 'forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.6,0.2,0.1,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_model', 'forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.6,0.2,0.1,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_model', 'forecast_zona', 'forecast_barrio'] ,'ponderacion':[0.6,0.2,0.1,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_model', 'forecast_zona', 'forecast_barrio_complemento'] ,'ponderacion':[0.6,0.2,0.1,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.6,0.2,0.1,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_edificio', 'forecast_zona', 'forecast_barrio'] ,'ponderacion':[0.6,0.2,0.1,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_edificio', 'forecast_zona', 'forecast_barrio_complemento'] ,'ponderacion':[0.6,0.2,0.1,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_edificio', 'forecast_model', 'forecast_barrio'] ,'ponderacion':[0.6,0.15,0.15,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_edificio', 'forecast_model', 'forecast_barrio_complemento'] ,'ponderacion':[0.6,0.15,0.15,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_edificio', 'forecast_model', 'forecast_zona'] ,'ponderacion':[0.6,0.15,0.15,0.1]},
    {'lista':['forecast_zona', 'forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.6,0.3,0.1]},
    {'lista':['forecast_model', 'forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.6,0.3,0.1]},
    {'lista':['forecast_model', 'forecast_zona', 'forecast_barrio'] ,'ponderacion':[0.6,0.3,0.1]},
    {'lista':['forecast_model', 'forecast_zona', 'forecast_barrio_complemento'] ,'ponderacion':[0.6,0.3,0.1]},
    {'lista':['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.6,0.25,0.15]},
    {'lista':['forecast_edificio', 'forecast_zona', 'forecast_barrio'] ,'ponderacion':[0.6,0.25,0.15]},
    {'lista':['forecast_edificio', 'forecast_zona', 'forecast_barrio_complemento'] ,'ponderacion':[0.6,0.25,0.15]},
    {'lista':['forecast_edificio', 'forecast_model', 'forecast_barrio'] ,'ponderacion':[0.5,0.4,0.1]},
    {'lista':['forecast_edificio', 'forecast_model', 'forecast_barrio_complemento'] ,'ponderacion':[0.5,0.4,0.1]},
    {'lista':['forecast_edificio', 'forecast_model', 'forecast_zona'] ,'ponderacion':[0.5,0.4,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.7,0.2,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_zona', 'forecast_barrio'] ,'ponderacion':[0.7,0.2,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_zona', 'forecast_barrio_complemento'] ,'ponderacion':[0.7,0.2,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_model', 'forecast_barrio'] ,'ponderacion':[0.7,0.2,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_model', 'forecast_barrio_complemento'] ,'ponderacion':[0.7,0.2,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_model', 'forecast_zona'] ,'ponderacion':[0.7,0.2,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_edificio', 'forecast_barrio'] ,'ponderacion':[0.7,0.2,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_edificio', 'forecast_barrio_complemento'] ,'ponderacion':[0.7,0.2,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_edificio', 'forecast_zona'] ,'ponderacion':[0.7,0.2,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_edificio', 'forecast_model'] ,'ponderacion':[0.6,0.2,0.2]},
    {'lista':['forecast_barrio_complemento', 'forecast_barrio'] ,'ponderacion':[0.7,0.3]},
    {'lista':['forecast_zona', 'forecast_barrio'] ,'ponderacion':[0.8,0.2]},
    {'lista':['forecast_zona', 'forecast_barrio_complemento'] ,'ponderacion':[0.7,0.3]},
    {'lista':['forecast_model', 'forecast_barrio'] ,'ponderacion':[0.9,0.1]},
    {'lista':['forecast_model', 'forecast_barrio_complemento'] ,'ponderacion':[0.8,0.2]},
    {'lista':['forecast_model', 'forecast_zona'] ,'ponderacion':[0.7,0.3]},
    {'lista':['forecast_edificio', 'forecast_barrio'] ,'ponderacion':[0.95,0.05]},
    {'lista':['forecast_edificio', 'forecast_barrio_complemento'] ,'ponderacion':[0.9,0.1]},
    {'lista':['forecast_edificio', 'forecast_zona'] ,'ponderacion':[0.8,0.2]},
    {'lista':['forecast_edificio', 'forecast_model'] ,'ponderacion':[0.7,0.3]},
    {'lista':['forecast_edificio_similiar', 'forecast_barrio'] ,'ponderacion':[0.95,0.05]},
    {'lista':['forecast_edificio_similiar', 'forecast_barrio_complemento'] ,'ponderacion':[0.92,0.08]},
    {'lista':['forecast_edificio_similiar', 'forecast_zona'] ,'ponderacion':[0.9,0.1]},
    {'lista':['forecast_edificio_similiar', 'forecast_model'] ,'ponderacion':[0.8,0.2]},
    {'lista':['forecast_edificio_similiar', 'forecast_edificio'] ,'ponderacion':[0.8,0.2]},
    {'lista':['forecast_barrio'] ,'ponderacion':[1]},
    {'lista':['forecast_barrio_complemento'] ,'ponderacion':[1]},
    {'lista':['forecast_zona'] ,'ponderacion':[1]},
    {'lista':['forecast_model'] ,'ponderacion':[1]},
    {'lista':['forecast_edificio'] ,'ponderacion':[1]},
    {'lista':['forecast_edificio_similiar'] ,'ponderacion':[1]}
    ]

for old_entry in old_list:
    old_list_elements = old_entry['lista']
    for new_entry in new_list:
        new_list_elements = new_entry['lista']
        if set(old_list_elements) == set(new_list_elements):
            new_entry['ponderacion'] = old_entry['ponderacion']
            break
for i in new_list:
    print(f'{i},')
    
    
#-----------------------------------------------------------------------------#
# A PARTIR DE LA NUEVA LISTA, ASIGNAR LAS PONDERACIONES PARA EL XGBOOSTING
#-----------------------------------------------------------------------------#

data_list = [
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.06, 0.04]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.4, 0.4, 0.1, 0.05, 0.05]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.2, 0.1, 0.1, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.4, 0.4, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.4, 0.4, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.4, 0.4, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.2]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.6, 0.25, 0.15]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.6, 0.25, 0.15]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.5, 0.4, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.25, 0.15]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.5, 0.4, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.4, 0.1]},
{'lista': ['forecast_edificio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.3, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.6, 0.3, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.3, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.3, 0.1]},
{'lista': ['forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar'], 'ponderacion': [0.8, 0.2]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento'], 'ponderacion': [0.9, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio'], 'ponderacion': [0.95, 0.05]},
{'lista': ['forecast_edificio', 'forecast_zona'], 'ponderacion': [0.8, 0.2]},
{'lista': ['forecast_edificio', 'forecast_model'], 'ponderacion': [0.7, 0.3]},
{'lista': ['forecast_edificio', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento'], 'ponderacion': [0.92, 0.08]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio'], 'ponderacion': [0.95, 0.05]},
{'lista': ['forecast_edificio_similiar', 'forecast_zona'], 'ponderacion': [0.9, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_model'], 'ponderacion': [0.8, 0.2]},
{'lista': ['forecast_edificio_similiar', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.7, 0.3]},
{'lista': ['forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.7, 0.3]},
{'lista': ['forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.8, 0.2]},
{'lista': ['forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_barrio', 'forecast_zona'], 'ponderacion': [0.8, 0.2]},
{'lista': ['forecast_barrio', 'forecast_model'], 'ponderacion': [0.9, 0.1]},
{'lista': ['forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_zona', 'forecast_model'], 'ponderacion': [0.7, 0.3]},
{'lista': ['forecast_zona', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_model', 'forecast_xgboosting'], 'ponderacion': []},
{'lista': ['forecast_edificio'], 'ponderacion': [1]},
{'lista': ['forecast_edificio_similiar'], 'ponderacion': [1]},
{'lista': ['forecast_barrio_complemento'], 'ponderacion': [1]},
{'lista': ['forecast_barrio'], 'ponderacion': [1]},
{'lista': ['forecast_zona'], 'ponderacion': [1]},
{'lista': ['forecast_model'], 'ponderacion': [1]},
{'lista': ['forecast_xgboosting'], 'ponderacion': []},
]

import copy

def adjust_ponderations(ponderations, last_value):
    total = sum(ponderations)
    if total == 1:
        return [round(ponderation, 2) for ponderation in ponderations]

    scaling_factor = (1 - last_value) / (total - last_value)
    adjusted_ponderations = [round(ponderation * scaling_factor, 2) for ponderation in ponderations[:-1]]
    adjusted_total = sum(adjusted_ponderations) + last_value
    
    if adjusted_total > 1:
        diff = adjusted_total - 1
        max_adjusted_index = adjusted_ponderations.index(max(adjusted_ponderations))
        adjusted_ponderations[max_adjusted_index] = max(0, adjusted_ponderations[max_adjusted_index] - diff)

    adjusted_ponderations.append(last_value)

    return [round(ponderation, 2) for ponderation in adjusted_ponderations]

def all_elements_in_list(list1, list2):
    for element in list1:
        if element not in list2:
            return False
    return True

data_list_copy1 = data_list.copy()
for i in data_list:
    if 'forecast_xgboosting' in i['lista'] and not i['ponderacion']:
        lista_obj = i['lista']
        lista_obj.remove('forecast_xgboosting')
        if lista_obj!=[]:
            for j in data_list_copy1:
                if set(lista_obj) == set(j['lista']) and j['ponderacion']!=[]:
                #if all_elements_in_list(lista_obj,j['lista']) and j['ponderacion']!=[]:
                    i['ponderacion'] = adjust_ponderations(copy.deepcopy(j['ponderacion'])+[0.1], 0.1)
                    lista_obj.append('forecast_xgboosting')
                    break
        else: 
            lista_obj.append('forecast_xgboosting')
            i['ponderacion'] = [1]
    
# Check
for i in data_list:
    if len(i['lista'])!=len(i['ponderacion']):
        print(i)
    if abs(1-sum(i['ponderacion']))>1e-3:
        print(i)
  
for i in data_list:
    print(f'{i},')


#-----------------------------------------------------------------------------#
# A PARTIR DE LAS PONDERACIONES AJUSTAR PONDERACIONES PARA EL MODELO ANN Y XGBOOSTING
#-----------------------------------------------------------------------------#

data_list = [
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.44, 0.14, 0.14, 0.09, 0.05, 0.04, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.06, 0.04]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.44, 0.14, 0.14, 0.09, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.44, 0.14, 0.14, 0.09, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.44, 0.14, 0.14, 0.09, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.44, 0.14, 0.14, 0.09, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.35, 0.36, 0.09, 0.05, 0.05, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.45, 0.18, 0.09, 0.09, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.54, 0.18, 0.09, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.54, 0.18, 0.09, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.53, 0.14, 0.14, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.54, 0.18, 0.09, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.53, 0.14, 0.14, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.53, 0.14, 0.14, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.4, 0.4, 0.1, 0.05, 0.05]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.53, 0.14, 0.14, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.36, 0.36, 0.09, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.36, 0.36, 0.09, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.36, 0.36, 0.09, 0.09, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.2, 0.1, 0.1, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.54, 0.18, 0.09, 0.09, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.54, 0.18, 0.09, 0.09, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.54, 0.18, 0.09, 0.09, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.54, 0.18, 0.09, 0.09, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.53, 0.14, 0.14, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': [0.63, 0.18, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.63, 0.18, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.63, 0.18, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.54, 0.18, 0.18, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.4, 0.4, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.53, 0.23, 0.14, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.4, 0.4, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.53, 0.23, 0.14, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.45, 0.36, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.4, 0.4, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.53, 0.23, 0.14, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.45, 0.36, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.45, 0.36, 0.09, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.63, 0.18, 0.09, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.63, 0.18, 0.09, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.63, 0.18, 0.09, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.63, 0.18, 0.09, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.63, 0.18, 0.09, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.63, 0.18, 0.09, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.54, 0.27, 0.09, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.54, 0.27, 0.09, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.54, 0.27, 0.09, 0.1]},
{'lista': ['forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.54, 0.27, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.2]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_xgboosting'], 'ponderacion': [0.72, 0.18, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.6, 0.25, 0.15]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.6, 0.25, 0.15]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.5, 0.4, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': [0.81, 0.09, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.25, 0.15]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.5, 0.4, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.85, 0.05, 0.1]},
{'lista': ['forecast_edificio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.4, 0.1]},
{'lista': ['forecast_edificio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.72, 0.18, 0.1]},
{'lista': ['forecast_edificio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.63, 0.27, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': [0.83, 0.07, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.85, 0.05, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.81, 0.09, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.72, 0.18, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.3, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.6, 0.3, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.63, 0.27, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.3, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.63, 0.27, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.72, 0.18, 0.1]},
{'lista': ['forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.3, 0.1]},
{'lista': ['forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.72, 0.18, 0.1]},
{'lista': ['forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.81, 0.09, 0.1]},
{'lista': ['forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.63, 0.27, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar'], 'ponderacion': [0.8, 0.2]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento'], 'ponderacion': [0.9, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio'], 'ponderacion': [0.95, 0.05]},
{'lista': ['forecast_edificio', 'forecast_zona'], 'ponderacion': [0.8, 0.2]},
{'lista': ['forecast_edificio', 'forecast_model'], 'ponderacion': [0.7, 0.3]},
{'lista': ['forecast_edificio', 'forecast_xgboosting'], 'ponderacion': [0.9, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento'], 'ponderacion': [0.92, 0.08]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio'], 'ponderacion': [0.95, 0.05]},
{'lista': ['forecast_edificio_similiar', 'forecast_zona'], 'ponderacion': [0.9, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_model'], 'ponderacion': [0.8, 0.2]},
{'lista': ['forecast_edificio_similiar', 'forecast_xgboosting'], 'ponderacion': [0.9, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.7, 0.3]},
{'lista': ['forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.7, 0.3]},
{'lista': ['forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.8, 0.2]},
{'lista': ['forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': [0.9, 0.1]},
{'lista': ['forecast_barrio', 'forecast_zona'], 'ponderacion': [0.8, 0.2]},
{'lista': ['forecast_barrio', 'forecast_model'], 'ponderacion': [0.9, 0.1]},
{'lista': ['forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.9, 0.1]},
{'lista': ['forecast_zona', 'forecast_model'], 'ponderacion': [0.7, 0.3]},
{'lista': ['forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.9, 0.1]},
{'lista': ['forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.9, 0.1]},
{'lista': ['forecast_edificio'], 'ponderacion': [1]},
{'lista': ['forecast_edificio_similiar'], 'ponderacion': [1]},
{'lista': ['forecast_barrio_complemento'], 'ponderacion': [1]},
{'lista': ['forecast_barrio'], 'ponderacion': [1]},
{'lista': ['forecast_zona'], 'ponderacion': [1]},
{'lista': ['forecast_model'], 'ponderacion': [1]},
{'lista': ['forecast_xgboosting'], 'ponderacion': [1]},
    ]


"""
chatgpt
ayudame a armar un codigo en python para ajustar 'forecast_model' a 0.1 cuando tenga un valor menor asignado y a 'forecast_xgboosting' 0.15 cuando tenga un valor menor asignado, pero que solo disminuya la ponderacion de aquellos valores que sean estrictamente mayores a 0.1, sin alterar los que sean igual o menor a 0.1. 
"""
def adjust_vector(vector):
    total = sum(vector)
    
    if total == 1:
        return [round(value, 2) for value in vector]
    
    scaling_factor = 1 / total
    adjusted_vector = [round(value * scaling_factor, 2) for value in vector]
    
    total_adjusted = sum(adjusted_vector)
    adjustment = 1 - total_adjusted
    
    # Distribuir el ajuste en el valor más grande del vector
    max_value = max(adjusted_vector)
    index_max_value = adjusted_vector.index(max_value)
    adjusted_vector[index_max_value] = round(max_value + adjustment, 2)
    
    return adjusted_vector

for entry in data_list:
    lista = entry['lista']
    ponderacion = entry['ponderacion']
    
    if len(lista) == 2 and ('forecast_model' in lista or 'forecast_xgboosting' in lista):
        ponderacion = [0.5, 0.5]
    else:
        if 'forecast_model' in lista:
            model_index = lista.index('forecast_model')
            if ponderacion[model_index] < 0.1:
                ponderacion[model_index] = 0.1
        
        if 'forecast_xgboosting' in lista:
            xgboosting_index = lista.index('forecast_xgboosting')
            if ponderacion[xgboosting_index] < 0.15:
                ponderacion[xgboosting_index] = 0.15
        
    entry['ponderacion'] = adjust_vector(ponderacion)

for i in data_list:
    i['ponderacion'] = adjust_vector(i['ponderacion'])
for i in data_list:
    print(f'{i},')



data_list = [
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.38, 0.13, 0.13, 0.08, 0.05, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.48, 0.14, 0.14, 0.09, 0.06, 0.09]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.42, 0.13, 0.13, 0.09, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.43, 0.13, 0.13, 0.08, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.43, 0.13, 0.13, 0.08, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.43, 0.13, 0.13, 0.08, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.32, 0.32, 0.08, 0.05, 0.09, 0.14]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.44, 0.17, 0.08, 0.08, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.51, 0.17, 0.09, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.51, 0.17, 0.09, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.51, 0.13, 0.13, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.51, 0.17, 0.09, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.51, 0.13, 0.13, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.51, 0.13, 0.13, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.37, 0.38, 0.1, 0.05, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.51, 0.13, 0.13, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.35, 0.34, 0.08, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.35, 0.34, 0.08, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.35, 0.34, 0.08, 0.09, 0.14]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.2, 0.1, 0.1, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.51, 0.17, 0.09, 0.09, 0.14]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.52, 0.17, 0.08, 0.09, 0.14]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.52, 0.17, 0.08, 0.09, 0.14]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.52, 0.17, 0.08, 0.09, 0.14]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.51, 0.13, 0.13, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': [0.6, 0.17, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.6, 0.17, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.6, 0.17, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.52, 0.17, 0.17, 0.14]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.4, 0.4, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.51, 0.22, 0.13, 0.14]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.4, 0.4, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.51, 0.22, 0.13, 0.14]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.43, 0.34, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.4, 0.4, 0.1, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.51, 0.22, 0.13, 0.14]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.43, 0.34, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.43, 0.34, 0.09, 0.14]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.6, 0.17, 0.09, 0.14]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.6, 0.17, 0.09, 0.14]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.6, 0.17, 0.09, 0.14]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.6, 0.17, 0.09, 0.14]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.6, 0.17, 0.09, 0.14]},
{'lista': ['forecast_edificio_similiar', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.6, 0.17, 0.09, 0.14]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.51, 0.26, 0.09, 0.14]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.52, 0.25, 0.09, 0.14]},
{'lista': ['forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.52, 0.25, 0.09, 0.14]},
{'lista': ['forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.52, 0.25, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.2]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_xgboosting'], 'ponderacion': [0.69, 0.17, 0.14]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.6, 0.25, 0.15]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.6, 0.25, 0.15]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.5, 0.4, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': [0.77, 0.09, 0.14]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.25, 0.15]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.5, 0.4, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.81, 0.05, 0.14]},
{'lista': ['forecast_edificio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.4, 0.1]},
{'lista': ['forecast_edificio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.69, 0.17, 0.14]},
{'lista': ['forecast_edificio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.6, 0.26, 0.14]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': [0.79, 0.07, 0.14]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.81, 0.05, 0.14]},
{'lista': ['forecast_edificio_similiar', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.7, 0.2, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.77, 0.09, 0.14]},
{'lista': ['forecast_edificio_similiar', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.69, 0.17, 0.14]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.3, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.6, 0.3, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.6, 0.26, 0.14]},
{'lista': ['forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.3, 0.1]},
{'lista': ['forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.6, 0.26, 0.14]},
{'lista': ['forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.69, 0.17, 0.14]},
{'lista': ['forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.3, 0.1]},
{'lista': ['forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.69, 0.17, 0.14]},
{'lista': ['forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.77, 0.09, 0.14]},
{'lista': ['forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.6, 0.26, 0.14]},
{'lista': ['forecast_edificio', 'forecast_edificio_similiar'], 'ponderacion': [0.8, 0.2]},
{'lista': ['forecast_edificio', 'forecast_barrio_complemento'], 'ponderacion': [0.9, 0.1]},
{'lista': ['forecast_edificio', 'forecast_barrio'], 'ponderacion': [0.95, 0.05]},
{'lista': ['forecast_edificio', 'forecast_zona'], 'ponderacion': [0.8, 0.2]},
{'lista': ['forecast_edificio', 'forecast_model'], 'ponderacion': [0.5, 0.5]},
{'lista': ['forecast_edificio', 'forecast_xgboosting'], 'ponderacion': [0.5, 0.5]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento'], 'ponderacion': [0.92, 0.08]},
{'lista': ['forecast_edificio_similiar', 'forecast_barrio'], 'ponderacion': [0.95, 0.05]},
{'lista': ['forecast_edificio_similiar', 'forecast_zona'], 'ponderacion': [0.9, 0.1]},
{'lista': ['forecast_edificio_similiar', 'forecast_model'], 'ponderacion': [0.5, 0.5]},
{'lista': ['forecast_edificio_similiar', 'forecast_xgboosting'], 'ponderacion': [0.5, 0.5]},
{'lista': ['forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.7, 0.3]},
{'lista': ['forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.7, 0.3]},
{'lista': ['forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.5, 0.5]},
{'lista': ['forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': [0.5, 0.5]},
{'lista': ['forecast_barrio', 'forecast_zona'], 'ponderacion': [0.8, 0.2]},
{'lista': ['forecast_barrio', 'forecast_model'], 'ponderacion': [0.5, 0.5]},
{'lista': ['forecast_barrio', 'forecast_xgboosting'], 'ponderacion': [0.5, 0.5]},
{'lista': ['forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.5]},
{'lista': ['forecast_zona', 'forecast_xgboosting'], 'ponderacion': [0.5, 0.5]},
{'lista': ['forecast_model', 'forecast_xgboosting'], 'ponderacion': [0.5, 0.5]},
{'lista': ['forecast_edificio'], 'ponderacion': [1]},
{'lista': ['forecast_edificio_similiar'], 'ponderacion': [1]},
{'lista': ['forecast_barrio_complemento'], 'ponderacion': [1]},
{'lista': ['forecast_barrio'], 'ponderacion': [1]},
{'lista': ['forecast_zona'], 'ponderacion': [1]},
{'lista': ['forecast_model'], 'ponderacion': [1]},
{'lista': ['forecast_xgboosting'], 'ponderacion': [1]},
    ]


for i in data_list:
    if abs(1-sum(i['ponderacion']))>1e-3:
        print(sum(i['ponderacion']))
  
for i in data_list:
    if len(i['lista'])!=len(i['ponderacion']):
        print(i)







