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
    print(i)
    
    
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.06, 0.04]}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.15, 0.15, 0.1, 0.1]}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.4, 0.4, 0.1, 0.05, 0.05]}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.2, 0.1, 0.1, 0.1]}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.4, 0.4, 0.1, 0.1]}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.4, 0.4, 0.1, 0.1]}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.4, 0.4, 0.1, 0.1]}
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.1, 0.1]}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.15, 0.15, 0.1]}
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_barrio_complemento', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_barrio', 'forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio_complemento'], 'ponderacion': [0.7, 0.2, 0.1]}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_barrio'], 'ponderacion': [0.7, 0.2, 0.1]}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_zona'], 'ponderacion': [0.7, 0.2, 0.1]}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_model'], 'ponderacion': [0.6, 0.2, 0.2]}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.6, 0.25, 0.15]}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.6, 0.25, 0.15]}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.5, 0.4, 0.1]}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.25, 0.15]}
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.5, 0.4, 0.1]}
{'lista': ['forecast_edificio', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.5, 0.4, 0.1]}
{'lista': ['forecast_edificio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.7, 0.2, 0.1]}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.7, 0.2, 0.1]}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.7, 0.2, 0.1]}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.7, 0.2, 0.1]}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.7, 0.2, 0.1]}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.7, 0.2, 0.1]}
{'lista': ['forecast_edificio_similiar', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_zona'], 'ponderacion': [0.6, 0.3, 0.1]}
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_model'], 'ponderacion': [0.6, 0.3, 0.1]}
{'lista': ['forecast_barrio_complemento', 'forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_barrio_complemento', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.3, 0.1]}
{'lista': ['forecast_barrio_complemento', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_barrio_complemento', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_barrio', 'forecast_zona', 'forecast_model'], 'ponderacion': [0.6, 0.3, 0.1]}
{'lista': ['forecast_barrio', 'forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_barrio', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_zona', 'forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio', 'forecast_edificio_similiar'], 'ponderacion': [0.8, 0.2]}
{'lista': ['forecast_edificio', 'forecast_barrio_complemento'], 'ponderacion': [0.9, 0.1]}
{'lista': ['forecast_edificio', 'forecast_barrio'], 'ponderacion': [0.95, 0.05]}
{'lista': ['forecast_edificio', 'forecast_zona'], 'ponderacion': [0.8, 0.2]}
{'lista': ['forecast_edificio', 'forecast_model'], 'ponderacion': [0.7, 0.3]}
{'lista': ['forecast_edificio', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio_complemento'], 'ponderacion': [0.92, 0.08]}
{'lista': ['forecast_edificio_similiar', 'forecast_barrio'], 'ponderacion': [0.95, 0.05]}
{'lista': ['forecast_edificio_similiar', 'forecast_zona'], 'ponderacion': [0.9, 0.1]}
{'lista': ['forecast_edificio_similiar', 'forecast_model'], 'ponderacion': [0.8, 0.2]}
{'lista': ['forecast_edificio_similiar', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_barrio_complemento', 'forecast_barrio'], 'ponderacion': [0.7, 0.3]}
{'lista': ['forecast_barrio_complemento', 'forecast_zona'], 'ponderacion': [0.7, 0.3]}
{'lista': ['forecast_barrio_complemento', 'forecast_model'], 'ponderacion': [0.8, 0.2]}
{'lista': ['forecast_barrio_complemento', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_barrio', 'forecast_zona'], 'ponderacion': [0.8, 0.2]}
{'lista': ['forecast_barrio', 'forecast_model'], 'ponderacion': [0.9, 0.1]}
{'lista': ['forecast_barrio', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_zona', 'forecast_model'], 'ponderacion': [0.7, 0.3]}
{'lista': ['forecast_zona', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_model', 'forecast_xgboosting'], 'ponderacion': []}
{'lista': ['forecast_edificio'], 'ponderacion': [1]}
{'lista': ['forecast_edificio_similiar'], 'ponderacion': [1]}
{'lista': ['forecast_barrio_complemento'], 'ponderacion': [1]}
{'lista': ['forecast_barrio'], 'ponderacion': [1]}
{'lista': ['forecast_zona'], 'ponderacion': [1]}
{'lista': ['forecast_model'], 'ponderacion': [1]}
{'lista': ['forecast_xgboosting'], 'ponderacion': []}
